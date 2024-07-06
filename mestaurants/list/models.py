from django.db import models #Django 모델 사용!!

class Restaurant(models.Model): #Django 모델 만들었음
    name = models.CharField(max_length=100) #식당 이름
    location = models.CharField(max_length=100) # 위치
    description = models.TextField(blank=True, null=True) #설명
    category = models.CharField(max_length=50, blank=True) #카테고리
    average_rating = models.FloatField(default=0.0) #평점
    created_at = models.DateTimeField(auto_now_add=True)  # 생성 일자
    updated_at = models.DateTimeField(auto_now=True)  # 수정 일자

    def __str__(self):
        return self.name

# blank와 null의 차이점이 뭐죠????
