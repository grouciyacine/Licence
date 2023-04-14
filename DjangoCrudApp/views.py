from bson import ObjectId
from django.http import HttpResponse

# Create your views here.
from DjangoCrudApp.models import Posts
from django.views.decorators.csrf import csrf_exempt
###
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import  DataSerializer,RegisterSerializer
from django.http.response import JsonResponse
###
from django.shortcuts import redirect
#users
from .models import Posts
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken
@api_view(['POST'])
def login_api(request):
    serializer=AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user=serializer.validated_data['user']
    __,token=AuthToken.objects.create(user)
    request.session['id'] = user.id
    return Response({
        'user_info':{
                'id':user.id,
                'userName':user.username,
                'email':user.email
        },
        'token':token
    })
@api_view(['GET'])
def get_user_data(request):
    user=request.user
    if user.is_authenticated:
        return Response({
            'user_info':{
            'id':user.id,
            'username':user.username,
            'email':user.email
            }
        })
    return Response({'error':'not authenticated'},status=400)
@api_view(['POST'])
def register_api(request):
    serializer=RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user=serializer.save()
    _,token=AuthToken.objects.create(user)
    return Response({
                'user_info':{
                'id':user.id,
                'userName':user.username,
                'email':user.email,
                'first_name':user.first_name,
                'last_name':user.last_name,
        },
        'token':token
    })
@csrf_exempt
def read_post_all(request):
    posts = Posts.objects.all()
    stringval = ""
    for post in posts:
        stringval += "First Name : " + post.NPK['N'] + " Last name : " + post.NPK[
            'P'] + " Post Title "+"<br>"
    return HttpResponse(posts)
class PostsList(APIView):
    def get(self, request):
        if request.method == 'GET':
            posts = Posts.objects.all()
            #print(posts)
            id = request.session.get('id')
            serializer = DataSerializer(posts,many=True)
            #print(serializer.data)
           #serializer.data['id']=id
            return JsonResponse(serializer.data, safe=False)
    def post(self, request):
        if request.method == 'POST':
            id = request.session.get('id')
            #mymodel=Posts(id_user=id)
            #mymodel.save()
            serializer = DataSerializer(data=request.data)
            #setattr(serializer,Posts.id_user,str(id))
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    def departmentApi(request, id=0):
        if request.method == 'GET':
            departments = Posts.objects.all()
            departments_serializer = DataSerializer(departments, many=True)
            return JsonResponse(departments_serializer.data, safe=False)

