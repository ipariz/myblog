from django.db import models


class Author(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=40)
	email = models.EmailField()
	created_date = models.DateTimeField()
	
	def __str__(self):
		return self.first_name + " " + self.last_name

class Comment(models.Model):
	text = models.TextField()
	author = models.ForeignKey(Author)
	created_date = models.DateTimeField()
	
	def __str__(self):
		return self.text

class Post(models.Model):
	title = models.CharField(max_length=100)
	text = models.TextField("post text")
	comments = models.ManyToManyField(Comment)
	author = models.ForeignKey(Author)
	created_date = models.DateTimeField()
	
	def __str__(self):
		return self.title