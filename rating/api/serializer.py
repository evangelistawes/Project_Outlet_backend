from rest_framework import serializers
from rating.models import Rating

class RatingSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.username')

    class Meta:
        model= Rating
        fields = '__all__'
        