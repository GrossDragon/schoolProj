from email.policy import default
from django.db import models
from matplotlib.pyplot import annotate, cla

# Create your models here.

# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)



class Pokupka(models.Model):
    email= models.CharField(max_length=70)
    way= models.CharField(max_length=70)
    date= models.DateField()
    books=models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.email} {self.date}"




class Author(models.Model):
    name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    date_of=models.DateField()
    country=models.CharField(max_length=25)
    image=models.ImageField(upload_to='authors/%Y-%m-%d/',default='default.jpg')
    annotation=models.CharField(max_length=8000)

    def __str__(self):
        return f"{self.name} {self.last_name}"


class Publisher(models.Model):
    name=models.CharField(max_length=50)
    city=models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}, {self.city}"



class Book(models.Model):
    name= models.CharField(max_length=100)
    author=models.ForeignKey(Author, on_delete=models.CASCADE)
    year_of_publish=models.DateField()
    publisher=models.ForeignKey(Publisher,on_delete=models.CASCADE)
    size=models.IntegerField()
    price=models.FloatField()
    image=models.ImageField(upload_to='books/%Y-%m-%d/',default='default.jpg')
    annotation=models.CharField(max_length=400)

    def __str__(self):
        return f"{self.name} - {self.author} - {self.publisher}"








