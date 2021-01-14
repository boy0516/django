from django.db import models
from django.utils import timezone
from django.forms import forms

# title 입력필드의 길이 체크 <3
def min_length_3_validator(value):
    if len(value) < 3 :
        raise forms.ValidationError('글제목은 3글자 이상 입력해 주세요')


class Post(models.Model):
    # 작성자
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # 글제목
    title = models.CharField(max_length=200, validators=[min_length_3_validator])
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

# Post에 달린 댓글
class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def __str__(self):
        return self.text

    def approve(self):
        self.approved_comment = True
        self.save()
