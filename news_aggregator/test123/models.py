from django.db import models

class News_data(models.Model):
    headline =models.CharField(max_length=500)
    url =models.URLField(max_length=500)
    source =models.CharField(max_length=50)
    search_word = models.CharField( max_length=50,null=True)
    pub_date = models.DateTimeField('date publish')

class Favourite(models.Model):
    news_id=models.ForeignKey(News_data,on_delete=models.CASCADE)
    favourite = models.BooleanField(default=False)
    user_name = models.CharField(("user"), max_length=50)