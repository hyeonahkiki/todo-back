# 직렬화 작업. 수정, 삭제를 여기서 작업
# serializer는 queryset과 모델 인스턴스와 같은 복잡한데이터를
# JSON 또는 다른 콘텐츠 유형으로 쉽게 변환. 또한 serializer는 받은 데이터의
# 유효서을 검사한 다음 복잡한 타입으로 형변환 할 수 있도록 serialization제공
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