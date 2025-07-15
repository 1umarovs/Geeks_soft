from django.db import models

# Create your models here.
class CustomerOpinion(models.Model):
    name = models.CharField(max_length=100)
    opinion = models.TextField()

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    title = models.CharField(max_length=100 , blank=True , null=True)
    link = models.URLField(max_length=200 , blank=True , null=True)
    image = models.ImageField(upload_to='portfolio_images/')

    def __str__(self):
        return self.title
    

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question
    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"

class OurContact(models.Model):
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=18)
    email = models.EmailField()
    telegram_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    tik_tok_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.address