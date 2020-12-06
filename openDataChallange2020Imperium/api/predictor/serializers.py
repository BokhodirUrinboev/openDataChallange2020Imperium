from rest_framework import serializers


class TAMSAMSOMSerializer(serializers.ModelSerializer):
    regions = serializers.ListSerializer()
    education = serializers.IntegerField()
    has_computer = serializers.IntegerField()
    has_phone = serializers.IntegerField()
    has_internet = serializers.IntegerField()
    can_internet = serializers.IntegerField()
    has_house = serializers.IntegerField()
    no_of_children = serializers.IntegerField()
    has_under_16 = serializers.IntegerField()
