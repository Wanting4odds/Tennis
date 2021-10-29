from rest_framework import serializers
from .models import ResultsData


class ResultsDataSerializer(serializers.ModelSerializer):
    atp = serializers.IntegerField(default=0)
    location = serializers.CharField(max_length=100)
    b365w = serializers.FloatField()
    tournament = serializers.CharField(max_length=200)
    date = serializers.DateTimeField(format="%d/%b/%Y")
    series = serializers.CharField(max_length=100)
    tier = serializers.CharField(max_length=100)

    # TODO: Serialize the rest of field

    class Meta:
        model = ResultsData
        fields = '__all__'

    def create(self, validated_data):
        return ResultsData.objects.create(**validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
