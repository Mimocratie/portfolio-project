from django.db import models

class Blog(models.Model):
    image = models.ImageField(upload_to='images/')
    body = models.TextField(max_length=200)
    title = models.CharField(max_length=25)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
