from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# 원래 accounts로 빼는 것이 맞음
# 원래 user모델에서 확장해서 사용하려면 AbstractUser에 칼럼을 추가해서 사용해야한다.
class User(AbstractUser):
    pass

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    # true, false값만 나옴
    completed = models.BooleanField(default=False)
