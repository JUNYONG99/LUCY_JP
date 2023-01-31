from .models import Review
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    rating = serializers.StringRelatedField(many=True)

    class Meta:
        model = Review
        fields = ['signature_img', 'title', 'price',
                  'qty', 'info', 'description', 'like_count', 'rating']