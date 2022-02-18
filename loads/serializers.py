from rest_framework import serializers

from loads.models import Load, LoadImage



class LoadImageSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        load_id = self.context['load_id']
        return LoadImage.objects.create(load_id = load_id, **validated_data)

    class Meta:
        model = LoadImage
        fields = ['id', 'image']
        # extra_kwargs = {
        #     'url': {'view_name': 'loadimage'}
        # }

class LoadSerializer(serializers.HyperlinkedModelSerializer):
    loadimage = LoadImageSerializer(many=True, read_only=True)
    # loadImages = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='loadImages')
    class Meta:
        model = Load
        fields = ['url', 'start_street', 'start_city', 'start_zip', 'loaded_distance', 'hazmat', 'load_reference', 'loadimage']