from rest_framework import serializers

class MyDataSerializer(serializers.Serializer):
    message = serializers.CharField()