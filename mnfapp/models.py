from django.db import models
from django.contrib.auth.models import User

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Scripts(models.Model):
    script_title = models.CharField(max_length=100, null=True)
    author_name = models.CharField(max_length=100, null=True)
    genre = models.CharField(max_length=100, null=True)
    document_name = models.CharField(max_length=225)
    script = models.FileField(upload_to='scripts/')
    # address = models.TextField()
    # image = models.ImageField(default="default.jpg", upload_to="media")
    # capacity = models.IntegerField()
    # city = models.CharField(max_length=100)
    # description = models.TextField()
    # price = models.CharField(default='Not Available', max_length=50)

    def __str__(self):
        return self.document_name


class Uploads(models.Model):
    # upload_date = models.DateField()
    uploaded_script = models.ForeignKey(Scripts, on_delete=models.CASCADE)
    user_uploaded = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.uploaded_script)
