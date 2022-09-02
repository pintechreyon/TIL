from django.db import models

# Create your models here.
class Movie(models.Model):
    # 제목과 내용 field (column) 생성
    # schema title  Text(50)
    title = models.CharField(max_length=20)
    audience = models.IntegerField()
    release_date = models.DateField()
    genre = models.CharField(max_length=30)
    score = models.FloatField()
    poster_url = models.TextField()
    description = models.TextField()
    

    def __str__(self):
        return self.title