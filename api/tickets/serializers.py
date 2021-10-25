import os 
from rest_framework import serializers
from .models import Section, Rank, Seat


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'


class RankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rank
        fields = '__all__'


class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields='__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['section'] = SectionSerializer(instance.section).data
        response['rank'] = RankSerializer(instance.rank).data
        return response

class AssignSeatsSerializer(serializers.Serializer):
    groups = serializers.ListField()

    def create(self, validated_data):
        return validated_data

class GetSeatsSerializer(serializers.Serializer):
    group = serializers.IntegerField()

    def create(self, validated_data):
        return validated_data