from django.db import models


class Blog(models.Model):
    text_limit = 150
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    pub_date = models.DateTimeField()
    body = models.TextField()

    def summary(self):
        if len(self.body) > self.text_limit:
            return self.body[:self.text_limit] + '...'
        else:
            return self.body
