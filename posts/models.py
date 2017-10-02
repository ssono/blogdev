from django.db import models

class Post(models.Model):
    date = models.DateField()
    text = models.TextField()
    title = models.CharField(max_length=100)
    quote = models.TextField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']

class Comment(models.Model):
    text = models.TextField()
    likes = models.IntegerField()
    date = models.DateTimeField(auto_now_add = True)
    parent_post = models.ForeignKey(Post)

    def __str__(self):
        return self.text
    class Meta:
        ordering = ['-likes']


class News(models.Model):
    text = models.TextField()
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

        class Meta:
            ordering = ['-date']
