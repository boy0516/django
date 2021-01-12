from django.db import models
from django.utils import timezone

class Post(models.Model):
    # 작성자
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # 글제목
    title = models.CharField(max_length=200)
    # 글내용
    text = models.TextField()
    # 작성일
    created_date = models.DateTimeField(default=timezone.now)
    # 게시일
    published_date = models.DateTimeField(blank=True, null=True)
# Create your models here.

    # migration test용 필드
    # test = models.TextField()


    def __str__(self):
        return self.title

    def publish(self):
        self.published_date = timezone.now()
        self.save()

