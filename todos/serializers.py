# 직렬화 작업. 수정, 삭제를 여기서 작업
# 직렬화????????????????????????????
from rest_framework import serializers
from .models import Todo, User

# todo 하나를 조작하기위한 serializer
# 모델폼과 비슷한 역할과 구조
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'user', 'title', 'completed', )

# todo_list를 만들기 위해서 user의 todo목록을 가져옴
class UserSerializer(serializers.ModelSerializer):
    todo_set = TodoSerializer(many=True)
    class Meta:
        model = User
        # user가 작성한 todo목록을 다 보여주기 위해 todo_set
        fields = ('id', 'username', 'todo_set',)