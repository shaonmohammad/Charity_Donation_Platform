from rest_framework import serializers
from feedback.models import Feedback


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'comment','created_at']

# class FeedbackSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=100)
#     email = serializers.EmailField(max_length=50)
#     comment = serializers.CharField(max_length=300)
    
#     def create(self, validated_data):
#         return Feedback.objects.create(validated_data)
    
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.email = validated_data.get('email', instance.email)
#         instance.comment = validated_data.get('comment', instance.comment)
#         instance.save()
#         return instance