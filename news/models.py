from django.db import models


class Section(models.Model):
    section_name = models.CharField(max_length=250)
    number_of_articles = models.PositiveIntegerField()
    views = models.PositiveIntegerField()

    def __str__(self):
        return self.section_name + ' ' + self.number_of_articles

class Article(models.Model):
    Section = models.ForeignKey(Section, on_delete = models.CASCADE)
    title = models.CharField(max_length =250)
    author = models.CharField(max_length= 250)
    publication_date = models.DateField()
    summary = models.CharField(max_length=5000)
    article_image = models.CharField(max_length=100)
    article_url = models.CharField(max_length = 100)

    def __str__(self):
        return self.title + ' ' + self.summary + ' ' + self.url
