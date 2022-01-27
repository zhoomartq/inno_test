from rest_framework import serializers
from .models import Document


class DocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Document
        fields = '__all__'

    def create(self, validated_data):
        review = Document.objects.create(**validated_data)
        return review

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return representation

    
class SearchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Document
        fields = ('id', 'text')