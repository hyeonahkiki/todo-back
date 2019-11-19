from django.urls import path
from . import views

urlpatterns = [
    # localhost:8000/api/v1/todos
    path('todos/', views.todo_create),
    # 게시물 하나가지고 할 수 있는 모든것을 할것임
    path('todos/<int:id>/', views.todo_detail),
    path('users/<int:id>/', views.user_detail),
]
