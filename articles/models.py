from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField()
	body = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	thumb = models.ImageField(default='default.png', blank=True)
	author = models.ForeignKey(User, default=1, on_delete=models.SET_DEFAULT)

	def __str__(self):
		return self.title

	def snippet(self):
		return self.body[:20] + ' ...'

	def snippet_title(self):
		return self.title[:10] + ' ...'

class Comment(models.Model):
	Blogs = models.ForeignKey(Article, default=1, on_delete=models.SET_DEFAULT)
	user1 = models.CharField(max_length=100)
	Body = models.TextField(max_length=250)
	timestamp = models.DateTimeField(auto_now_add=True)
	approved = models.BooleanField(default=False)
