from djongo import models
# Create your models here.

"""
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
"""
class Posts(models.Model):
    _id=models.ObjectIdField()
    Date=models.DateTimeField(auto_now_add=True)
    NPK_Date=models.CharField(max_length=20,blank=True)
    NDvi=models.FloatField(blank=True)
    NDvi_Date=models.CharField(max_length=20,blank=True)
    objects=models.DjongoManager()
    N=models.FloatField(blank=True)
    N_lat=models.FloatField(blank=True)
    N_long=models.FloatField(blank=True)
    N_alt=models.FloatField(blank=True)
    N_Date=models.CharField(max_length=20,blank=True)
    P_lat=models.FloatField(blank=True)
    P_long=models.FloatField(blank=True)
    P_alt=models.FloatField(blank=True)
    P_Date=models.CharField(max_length=20,blank=True)
    P=models.FloatField(blank=True)
    K=models.FloatField(blank=True)
    K_lat=models.FloatField(blank=True)
    K_long=models.FloatField(blank=True)
    K_alt=models.FloatField(blank=True)
    K_Date=models.CharField(max_length=20,blank=True)
    NPkard_Value1=models.FloatField(blank=True)
    NPkard_Value2=models.FloatField(blank=True)
    NPkard_Value3=models.FloatField(blank=True)
    NPkard_Value4=models.FloatField(blank=True)
    NPkard_Value5=models.FloatField(blank=True)
    NPkard_Value6=models.FloatField(blank=True)
    NPkard_Value7=models.FloatField(blank=True)
    NPKard_Date=models.CharField(max_length=20,blank=True)
    NPKard_long=models.FloatField(blank=True)
    NPKard_lat=models.FloatField(blank=True)
    NPKard_alt=models.FloatField(blank=True)
    NDvi_long=models.FloatField(blank=True)
    NDvi_lat=models.FloatField(blank=True)
    NDvi_alt=models.FloatField(blank=True)
    #Camera=models.CharField(max_length=1000,blank=True)
    #Camera_long=models.FloatField(blank=True)
    #Camera_lat=models.FloatField(blank=True)
    #Camera_alt=models.FloatField(blank=True)
    #Camera_date=models.CharField(max_length=20,blank=True)
    #id_user=models.IntegerField()