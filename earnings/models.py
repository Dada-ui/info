from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Register_Model(User):

    def __str__(self):
        return self.username


class App_Model(models.Model):
    photo = models.ImageField(upload_to='app_image')
    app_name = models.CharField(max_length=100)
    app_link = models.URLField(max_length=50)
    app_category = models.CharField(max_length=100)
    point = models.IntegerField()

    def __str__(self):
        return self.app_name


class Task_Model(models.Model):
    screenshot = models.ImageField(upload_to='images_upload')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    app = models.ForeignKey(App_Model, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user


class User_Model(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return self.user.username