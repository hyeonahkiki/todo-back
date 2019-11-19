# 각각 json응답, http응답
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .serializers import TodoSerializer
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


# Create your views here.


# 게시물을 생성하는 함수이기 때문에 POST요청만 받아야함
@api_view(['POST'])
# 조건에 맞는 사람만 허가(인증된 사용자만 허가하겠다)
@permission_classes((IsAuthenticated,))
# 나는 jsonweb로 인증을 할거고 그거에 맞는 사람만 허가하겠다.
# 튜플형태로 쓰면 뒤에 꼭 , 쓰기!!!!!!!!!!!!!!                                                                
@authentication_classes((JSONWebTokenAuthentication,))
def todo_create(request):
    # 사용자가 입력한 정보를 받아와야하기 때문에
    serializer = TodoSerializer(data=request.POST)
    if serializer.is_valid():
        serializer.save()
        # 다른곳에서도 사용하기 위해서 jsonresponse로 리턴해야한다
        # 그냥 serializer.data만 리턴하면 파이썬에서만 사용할 수 있다.
        return JsonResponse(serializer.data)
    return HttpResponse(status=400)