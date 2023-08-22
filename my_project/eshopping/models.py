
from django.db import models

class Author(models.Model):
  firstname = models.CharField(max_length=100)
  lastname = models.CharField(max_length=100)
  address = models.CharField(max_length=200, null=True)
  zipcode = models.IntegerField(null=True)
  telephone = models.CharField(max_length=100, null=True)
  recommendedby = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='recommended_authors', related_query_name='recommended_authors', null=True, blank=True)
  joindate = models.DateField()
  popularity_score = models.IntegerField()
  followers = models.ManyToManyField('User', related_name='followed_authors', related_query_name='followed_authors', null=True, blank=True)
  def __str__(self):
    return self.firstname + ' ' + self.lastname
  
class Publisher(models.Model):
  firstname = models.CharField(max_length=100)
  lastname = models.CharField(max_length=100)
  recommendedby = models.ForeignKey('Publisher', on_delete=models.CASCADE, null=True, blank=True)
  joindate = models.DateField()
  popularity_score = models.IntegerField()
  
  def __str__(self):
    return self.firstname + ' ' + self.lastname

class Books(models.Model):
  title = models.CharField(max_length=100)
  genre = models.CharField(max_length=200)
  price = models.IntegerField(null=True)
  published_date = models.DateField()
  author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='books', related_query_name='books',null=True, blank=True)
  publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE, related_name='books', related_query_name='books', null=True, blank=True)
  def __str__(self):
    return self.title



class User(models.Model):
  username = models.CharField(max_length=100)
  email = models.CharField(max_length=100)
  def __str__(self):
    return self.username
  


class Course(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
      return self.name

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    enrolled_courses = models.ForeignKey(Course, on_delete=models.CASCADE)
    
    def __str__(self):
      return self.name
