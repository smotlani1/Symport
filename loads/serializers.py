from rest_framework import serializers

from loads.models import Load, LoadImage



class LoadImageSerializer(serializers.ModelSerializer):

    #Override create function to allow users to upload images corresponding to a particular load#
    def create(self, validated_data):
        load_id = self.context['load_id']
        return LoadImage.objects.create(load_id = load_id, **validated_data)

    class Meta:
        model = LoadImage
        fields = ['id', 'image']
        

class LoadSerializer(serializers.HyperlinkedModelSerializer):
    loadimage = LoadImageSerializer(many=True, read_only=True)
    class Meta:
        model = Load
        fields = ['id','start_street', 'start_city','start_state', 'start_zip', 'end_street', 'end_city','end_state', 'end_zip', 'loaded_distance', 'hazmat', 'load_reference', 'loadimage']