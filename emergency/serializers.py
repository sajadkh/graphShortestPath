from rest_framework import serializers
from emergency.models import *


class SourceSerializer(serializers.Serializer):
    source = serializers.CharField(required=True, allow_blank=False, max_length=100)

    def create(self, validated_data):
        return Source.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.source = validated_data.get('source', instance.source)
        instance.save()
        return instance


class PathSerializer(serializers.Serializer):
    graph = serializers.CharField(required=True, allow_blank=False, max_length=100)
    source = serializers.CharField(required=True, allow_blank=False, max_length=100)
    destination = serializers.CharField(required=True, allow_blank=False, max_length=100)
    distance = serializers.IntegerField(required=True)

    def create(self, validated_data):
        return Path.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.graph = validated_data.get('graph', instance.graph)
        instance.source = validated_data.get('source', instance.source)
        instance.destination = validated_data.get('destination', instance.destination)
        instance.distance = validated_data.get('distance', instance.distance)
        instance.save()
        return instance
