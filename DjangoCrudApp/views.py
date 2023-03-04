from bson import ObjectId
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from DjangoCrudApp.models import Posts
from django.views.decorators.csrf import csrf_exempt
###
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Stock
from .serializer import StockSerializer,DataSerializer
from django.http.response import JsonResponse
###
@csrf_exempt
def add_post(request):
    GPS={"Latitude":request.POST.get('Latitude'),"Longitude":request.POST.get('Longitude'),"Altitude":request.POST.get('Altitude')}
    NPK={"N":request.POST.get("N"),
        "P":request.POST.get("P"),
        "K":request.POST.get("K"),
        "GPS":{"Latitude":request.POST.get('LatitudeNP'),"Longitude":request.POST.get('LongitudeNP'),"Altitude":request.POST.get('AltitudeNP')},
        "Date":request.POST.get("DateNPK")
        }
    NDvi={"Value":request.POST.get("NDvi"),
        "GPS":{"Latitude":request.POST.get('LatitudeNDvi'),"Longitude":request.POST.get('LongitudeNDvi'),"Altitude":request.POST.get('AltitudeNDvi')},
        "Date":request.POST.get("DateNDvi")
        }
    NPKard={"Value1":request.POST.get("NP1"),
            "Value2":request.POST.get("NP2"),
            "Value3":request.POST.get("NP3"),
            "Value4":request.POST.get("NP4"),
            "Value5":request.POST.get("NP5"),
            "Value6":request.POST.get("NP6"),
            "Value7":request.POST.get("NP7"),
            "GPS":{"Latitude":request.POST.get('LatitudeKard'),"Longitude":request.POST.get('LongitudeKard'),"Altitude":request.POST.get('AltitudeKard')},
            "Date":request.POST.get("DateKard")
            }
    Camera={"Image":request.POST.get('Image'),
            "GPS":{"Latitude":request.POST.get('LatitudeImg'),"Longitude":request.POST.get('LongitudeImg'),"Altitude":request.POST.get('AltitudeImg')},
            "Date":request.POST.get("DateImg")
            }
    """
    comment=request.POST.get("comment").split(",")
    tags=request.POST.get("tags").split(",")
    user_details={"first_name":request.POST.get("first_name"),"last_name":request.POST.get("last_name")}
    post=Posts(post_title=request.POST.get("post_title"),post_description=request.POST.get("post_description"),comment=comment,tags=tags,user_details=user_details)
    """
    post=Posts(NDvi=NDvi,GPS=GPS,NPK=NPK,NPKard=NPKard,Camera=Camera)
    post.save()
    return HttpResponse("Inserted")



def read_post(request,id):
    post=Posts.objects.get(_id=ObjectId(id))
    stringval="First Name : "+post.user_details['first_name']+" Last name : "+post.user_details['last_name']+" Post Title "+post.post_title+" Comment "+post.comment[0]
    return HttpResponse(stringval)

def read_post_all(request):
    posts=Posts.objects.all()
    stringval=""
    for post in posts:
        stringval += "First Name : " + post.NPK['N'] + " Last name : " + post.NPK[
            'P'] + " Post Title "+"<br>"
    return HttpResponse(posts)


class PostsList(APIView):
    def get(self,request):
        if request.method=='GET':
            posts=Posts.objects.all()
            serializer=DataSerializer(posts,many=True)
            return JsonResponse(serializer.data,safe=False)
        
    
    def post(self,request):
        serializer = DataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    def departmentApi(request,id=0):
        if request.method=='GET':
            departments = Posts.objects.all()
            departments_serializer=DataSerializer(departments,many=True)
            return JsonResponse(departments_serializer.data,safe=False)
    
class StockList(APIView):
    def get(self,request):
        stocks=Stock.objects.all()
        serializer=StockSerializer(stocks,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = StockSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

