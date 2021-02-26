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

class Uploadvideo(models.Model):
    name= models.CharField(max_length=500,blank=True)
    recfile= models.FileField(upload_to='diybbp/')

    def __str__(self):
        return self.name + ": " + str(self.recfile)

class Uploadrefer(models.Model):
    refername= models.CharField(max_length=500,blank=True)
    refervideo= models.FileField(upload_to='diybbp/')

    def __str__(self):
        return self.refername + ": " + str(self.refervideo)

class Uploaddo(models.Model):
    doname= models.CharField(max_length=500,blank=True)
    dovideo= models.FileField(upload_to='diybbp/')

    def __str__(self):
        return self.doname + ": " + str(self.dovideo)

class Uploadlive(models.Model):
    livename= models.CharField(max_length=500,blank=True)
    livevideo= models.FileField(upload_to='diybbp/')

    def __str__(self):
        return self.livename + ": " + str(self.livevideo)

class Uploadboundary(models.Model):
    boundaryname= models.CharField(max_length=500,blank=True)
    boundaryvideo= models.FileField(upload_to='diybbp/')

    def __str__(self):
        return self.boundaryname+ ": " + str(self.boundaryvideo)
