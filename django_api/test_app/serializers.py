from rest_framework import serializers


class SimpleObject():
    def __init__(self, name):
        self.name = name


class SimpleObjectSerializer(serializers.Serializer):
    name = serializers.CharField()


def run_data():
    simple_var = SimpleObject("Henry")
    simple_var_serializer = SimpleObjectSerializer(simple_var)
    print(simple_var_serializer.data)
