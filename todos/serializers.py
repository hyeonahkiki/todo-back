# 직렬화 작업. 수정, 삭제를 여기서 작업
from rest_framework import serializers
from .models import Todo

# 모델폼과 비슷한 역할과 구조
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'user', 'title', 'completed', )