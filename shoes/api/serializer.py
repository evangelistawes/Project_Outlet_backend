from rest_framework import serializers
from shoes.models import Shoes


class ShoesSerializer(serializers.ModelSerializer):
    good_avaliations = serializers.SerializerMethodField()
    bad_avaliations = serializers.SerializerMethodField()
    photo = serializers.ImageField(max_length=None, allow_empty_file=False, use_url=True)
        
    class Meta:
        model = Shoes
        fields= '__all__'


    def get_good_avaliations(self,obj):
        avaliations=obj.rating_set.all()
        if avaliations is not None:
            good_avaliations = avaliations.filter(grade__gt=6)
            return good_avaliations.count()
        
    def get_bad_avaliations(self,obj):
        avaliations=obj.rating_set.all()
        if avaliations is not None:
            bad_avaliations = avaliations.filter(grade__lt=6)
            return bad_avaliations.count()