from rest_framework import serializers

from loads.models import Load, LoadImage

class LoadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Load
        fields = ['start_street', 'start_city', 'start_zip', 'loaded_distance', 'hazmat', 'load_reference']


class LoadImageSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        load_id = self.context['load_id']
        return LoadImage.objects.create(load_id = load_id, **validated_data)

    class Meta:
        model = LoadImage
        fields = ['id', 'image']
