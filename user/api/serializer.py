from rest_framework import serializers
from user.models import User


class UserSerializer(serializers.ModelSerializer):
    avaliations = serializers.SerializerMethodField()
    class Meta:
        model= User
        fields = '__all__'

    def get_avaliations(self, obj):
        if obj.rating_set.all() is not None:
            print(obj.rating_set.all().values_list())
            return obj.rating_set.all().values()