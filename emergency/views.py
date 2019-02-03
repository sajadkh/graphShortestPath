from rest_framework.views import APIView
from emergency.serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from collections import defaultdict


class SensorView(ModelViewSet):
    """
    get Sensor list
    """
    serializer_class = SensorSerializer
    queryset = Sensor.objects.all()


class PathView(APIView):
    """
     get path between two nodes
    """

    def get(self, request, format=None):
        nodes = Path.objects.all().filter(graph="eng_uni_ferdowsi")
        fire = self.get_fire()
        graph = Graph()
        fire_path = ''
        for n in nodes:
            if n.source in fire and n.destination in fire:
                fire_path = n.source + ',' + n.destination
                continue
            elif n.source == n.destination:
                continue
            graph.add_edge(n.source, n.destination, n.distance)
        source_req_serializer = SourceSerializer(data=request.query_params)
        if source_req_serializer.is_valid():
            path1 = self.dijsktra(graph, source_req_serializer.validated_data['source'], '1')
            path2 = self.dijsktra(graph, source_req_serializer.validated_data['source'], '5')
            data = {}
            if (path2 == 'Error' and path1 == 'Error') or len(path1) == 0 and len(path2) == 0:
                data = {
                    'message': "I'm so sorry for you, you were a good guy. God bless you!",
                    'error': "PathNotFound",
                    'status': 'error'
                }
                return Response(data, status=status.HTTP_404_NOT_FOUND)
            elif len(path1) == 0 and len(path2) > 0:
                data = {
                    'path': path2,
                    'fire': fire_path,
                    'status': 'success'
                }
            elif len(path2) == 0 and len(path1) > 0:
                data = {
                    'path': path1,
                    'fire': fire_path,
                    'status': 'success'
                }
            elif len(path1) <= len(path2):
                data = {
                    'path': path1,
                    'fire': fire_path,
                    'status': 'success'
                }
            elif len(path1) > len(path2):
                data = {
                    'path': path2,
                    'fire': fire_path,
                    'status': 'success'
                }
            return Response(data, status=status.HTTP_200_OK)

    def dijsktra(self, graph, initial, end):
        # shortest paths is a dict of nodes
        # whose value is a tuple of (previous node, weight)
        shortest_paths = {initial: (None, 0)}
        current_node = initial
        visited = set()

        while current_node != end:
            visited.add(current_node)
            destinations = graph.edges[current_node]
            weight_to_current_node = shortest_paths[current_node][1]

            for next_node in destinations:
                weight = graph.weights[(current_node, next_node)] + weight_to_current_node
                if next_node not in shortest_paths:
                    shortest_paths[next_node] = (current_node, weight)
                else:
                    current_shortest_weight = shortest_paths[next_node][1]
                    if current_shortest_weight > weight:
                        shortest_paths[next_node] = (current_node, weight)

            next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
            if not next_destinations:
                return "Error"
            # next node is the destination with the lowest weight
            current_node = min(next_destinations, key=lambda k: next_destinations[k][1])

        # Work back through destinations in shortest path
        path = []
        while current_node is not None:
            path.append(current_node)
            next_node = shortest_paths[current_node][0]
            current_node = next_node
        # Reverse path
        path = path[::-1]
        return path

    def get_fire(self):
        fire_paths = Sensor.objects.all().filter(alarm=True)
        fire_nodes = []
        if len(fire_paths) != 0:
            for fire_path in fire_paths:
                fire_nodes.append(fire_path.path.source)
                fire_nodes.append(fire_path.path.destination)
        return fire_nodes


class Graph:
    def __init__(self):
        """
        self.edges is a dict of all possible next nodes
        e.g. {'X': ['A', 'B', 'C', 'E'], ...}
        self.weights has all the weights between two nodes,
        with the two nodes as a tuple as the key
        e.g. {('X', 'A'): 7, ('X', 'B'): 2, ...}
        """
        self.edges = defaultdict(list)
        self.weights = {}

    def add_edge(self, from_node, to_node, weight):
        # Note: assumes edges are bi-directional
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight
