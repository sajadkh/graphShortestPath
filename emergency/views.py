from rest_framework.views import APIView
from emergency.serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet


class PathView(ModelViewSet):
    """
    get transaction list
    """
    serializer_class = PathSerializer
    queryset = Path.objects.all()


class SourceView(APIView):
    """
     get path between two nodes
    """

    def get(self, request, format=None):
        graph = {}
        nodes = Path.objects.all().filter(graph="computerSalon")
        fire = self.get_fire()
        for n in nodes:
            graph[n.source] = []
        for n in nodes:
            if n.source in fire and n.destination in fire:
                continue
            graph[n.source].append(n.destination)
        source_req_serializer = SourceSerializer(data=request.data)
        if source_req_serializer.is_valid():
            path1 = self.find_path(graph, source_req_serializer.validated_data["source"], 'exit1')
            path2 = self.find_path(graph, source_req_serializer.validated_data["source"], 'exit2')
            if len(path1) == 0 and len(path2) > 0:
                return Response(path2, status.HTTP_200_OK)
            elif len(path2) == 0 and len(path1) > 0:
                return Response(path1, status.HTTP_200_OK)
            elif len(path1) == 0 and len(path2) == 0:
                return Response("error in calculate path", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            elif len(path1) <= len(path2):
                return Response(path1, status=status.HTTP_200_OK)
            elif len(path1) > len(path2):
                return Response(path2, status=status.HTTP_200_OK)

    def find_path(self, graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if start not in graph:
            return []
        for node in graph[start]:
            if node not in path:
                newpath = self.find_path(graph, node, end, path)
                if newpath:
                    return newpath
        return []

    def get_fire(self):
        return []


