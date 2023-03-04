from rest_framework import serializers

from .models import Stock,Posts,NPK,Camera,NDvi,NPKard,GPS
class GPS(serializers.ModelSerializer):
    class Meta:
        model=GPS,
        fields='__all__'
class NPKSerializer(serializers.ModelSerializer):
    #GPS=GPS
    class Meta: 
        model=NPK
        fields='__all__'
class NDvi(serializers.ModelSerializer):
    GPS=GPS
    class Meta:
        model=NDvi
        fields='__all__' 
class NPKard(serializers.ModelSerializer):
    GPS=GPS
    class Meta:
        model=NPKard
        fields='__all__' 
class Camera(serializers.ModelSerializer):
    GPS=GPS
    class Meta:
        
        model=Camera
        fields='__all__'                    

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model=Stock
        #fields=('ticker','volume')
        fields='__all__'
        
class DataSerializer(serializers.ModelSerializer):
   
    NPKard=NPKard
    Camera=Camera
    NDvi=NDvi
    NPK=NPK
    class Meta:
        model=Posts
        #fields=('ticker','volume')
        fields='__all__'