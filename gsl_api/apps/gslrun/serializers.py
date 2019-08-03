from rest_framework import serializers


class CompilerRequestSerializer(serializers.Serializer):
    code = serializers.CharField()
