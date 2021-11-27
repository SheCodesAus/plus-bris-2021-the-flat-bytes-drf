from rest_framework import serializers
from .models import SavedRecommendation

class SavedRecommendationSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    product_id = serializers.IntegerField()
    owner = serializers.IntegerField()

    def create(self, validated_data):
        return SavedRecommendation.objects.create(**validated_data)

class SavedRecommendationDetailSerializer(SavedRecommendationSerializer):
    def update(self, instance, validated_data):
        instance.product_id = validated_data.get('product_id', instance.product_id)
        instance.owner = validated_data.get('owner', instance.owner)
    
        instance.save() 
        return instance