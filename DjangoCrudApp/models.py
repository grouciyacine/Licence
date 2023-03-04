from djongo import models
# Create your models here.


class NPK(models.Model):
    _id=models.ObjectIdField()
    N=models.FloatField()
    P=models.FloatField()
    K=models.FloatField()
    Date=models.CharField(max_length=10)
    def __str__(self):
        return self.P    
class NDvi(models.Model):
    _id=models.ObjectIdField()
    Value=models.FloatField()
    Date=models.CharField(max_length=10)
    def __str__(self):
        return self.Value    
class NPKard(models.Model):
    _id=models.ObjectIdField()
    Value1=models.FloatField()
    Value2=models.FloatField()
    Value3=models.FloatField()
    Value4=models.FloatField()
    Value5=models.FloatField()
    Value6=models.FloatField()
    Value7=models.FloatField()
    Date=models.CharField(max_length=10)
    def __str__(self):
        return self.Value1    
class Camera(models.Model):
    _id=models.ObjectIdField()
    Img=models.CharField(max_length=255)
    Date=models.CharField(max_length=10)
    def __str__(self):
        return self.Img
class GPS(models.Model):
    _id=models.ObjectIdField()
    Latitude=models.FloatField()
    Altitude=models.FloatField()
    Longitude=models.FloatField()
    def __str__(self):
        return self.Latitude
class Stock(models.Model):
    _id=models.ObjectIdField()
    ticker=models.CharField(max_length=10)
    open=models.FloatField()
    close=models.FloatField()
    volume=models.IntegerField()
    def __str__(self):
        return self.ticker
class Posts(models.Model):

    _id=models.ObjectIdField()
   # GPS=models.JSONField()
    Date=models.DateTimeField(auto_now_add=True)
    #Date1=models.DateTimeField(auto_now_add=False)
    #NDvi=models.JSONField()
    NPK=models.JSONField(NPK)
    objects=models.DjongoManager()
    #NPKard=models.JSONField()
    #Camera=models.JSONField()