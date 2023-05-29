from django.db import models

# Create your models here.
class myprc(models.Model):
    image = models.ImageField(upload_to='prcimage/')
    Title = models. CharField(max_length=50,blank=False)
    Desc = models. TextField(max_length=500,blank=True)
    datetime = models.DateTimeField(auto_now_add=True)
def summary(self):
    return self.desc[0:100]

    def __str__(self):
        return self.Title


