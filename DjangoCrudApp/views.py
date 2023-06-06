from bson import ObjectId
from django.http import HttpResponse
from rest_framework import viewsets
from django.views import View
# Create your views here.
from DjangoCrudApp.models import Posts
from django.views.decorators.csrf import csrf_exempt
import datetime
from datetime import datetime, timedelta
###
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import  DataSerializer,RegisterSerializer,BookSerializer,JsonSerializer
from django.http.response import JsonResponse
###
from django.shortcuts import redirect
import uuid
import time
#users
from .models import Posts,Excel,ExcelNPK
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.files.storage import FileSystemStorage
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken 
import os
from .models import Book
from django.conf import settings
from django.http import JsonResponse
import matplotlib.pyplot as plt
import numpy as np
from django.views.decorators.csrf import csrf_exempt
from asgiref.sync import async_to_sync
import asyncio
import threading
import matplotlib
matplotlib.use('agg')
@api_view(['POST'])  
def upload_file(request):
        if request.method == 'POST':
            file = request.FILES['file']
            file_data = file.read().decode('utf-8')
            data = json.loads(file_data)
            with open(data,'r') as f:
                data=json.load(f)
                obj=Excel(data=data)
                obj.save()
            return JsonResponse({'status': obj})
        else:
            return JsonResponse({'error': 'Invalid request method'})
        
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


class JsonUploadView(APIView):
    def post(self, request, *args, **kwargs):
        json_data = json.loads(request.body)
        my_model = Excel( data=json_data['data'])
        my_model.save()
        return JsonResponse({'status': 'success'})
    def get(self, request, *args, **kwargs):
        my_model = Excel.objects.all()
        data = [my_models.data for my_models in my_model]
        if my_model:
            return JsonResponse(data, safe=False)
        else:
            return JsonResponse({'error': 'No data found'})


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    def post(self, request, *args, **kwargs):
        cover = request.data['cover']
        imgName = request.data['title']
        #Book.objects.create(title=title, cover=cover)
        Book.objects.create(cover=cover)
        return HttpResponse({'message': 'Book created'}, status=200)
    def get_images(request):
        media_path = os.path.join(settings.MEDIA_ROOT, 'media')
        images = []
        for filename in os.listdir(media_path):
            if filename.endswith('.jpg') or filename.endswith('.png'):
                images.append(os.path.join(settings.MEDIA_URL, 'media', filename))
        return JsonResponse({'images': images})

@csrf_exempt
def create_graph(request):
        if request.method == 'POST':
            data = json.loads(request.body)
            x_values = data.get('x_values')
            y_values = data.get('y_values')
            x = np.array(x_values, dtype=float)
            y = np.array(y_values, dtype=float)
            plt.plot(x, y)
            plt.xlabel('X-axis')
            plt.ylabel('Y-axis')
            plt.title('Graph Title')
            filename = f'graph_{uuid.uuid4().hex}.png'
            folder_path = os.path.join(settings.MEDIA_ROOT, 'graph')
            graph_path = os.path.join(folder_path, filename)
            plt.savefig(graph_path)
            return HttpResponse('Graph created successfully')
        return JsonResponse({'error': 'Invalid request method'}) 

@csrf_exempt
def generate_graph_view(request):
    t = threading.Thread(target=create_graph, args=(request,))
    t.start()
    return JsonResponse({'message': 'Graph generation started'})

def get_graph_images(request):
    image_urls = []

    # Path to the media folder where the graph images are saved
    media_path = os.path.join(settings.MEDIA_ROOT, 'graph')

    # Get a list of all image files in the media folder
    image_files = [f for f in os.listdir(media_path) if os.path.isfile(os.path.join(media_path, f))]

    # Construct the image URLs
    for image_file in image_files:
        image_url = f"{settings.MEDIA_URL}graph/{image_file}"
        image_urls.append(image_url)

    return JsonResponse({'image_urls': image_urls})
def draw_curve(N_values, dates):
    dates = [int(date) for date in dates]
    plt.plot(dates, N_values)
    plt.xlabel('Date')
    plt.ylabel('N Value')
    plt.title('N Value Over Time')
    plt.show()
@csrf_exempt
def get_n_data(request):
    data = json.loads(request.body)
    Type = data.get('type')
    min_date = data.get('min_date')
    max_date = data.get('max_date')      
    #min_date = "05-05-2021"  # Replace with your actual min_date
    #max_date = "12-12-2023"  # Replace with your actual max_date
    data = Posts.objects.filter(NPK_Date__range=[min_date, max_date]).values(Type, 'NPK_Date')
    #dates = Posts.objects.filter(NPK_Date__range=[min_date, max_date]).values_list('NPK_Date', flat=True)

    N_values = [item[Type] for item in data]
    dates = [datetime.strptime(item['NPK_Date'], '%d-%m-%Y').date().strftime("%Y%m%d") for item in data]
    #draw_curve(N_values, dates)
    dates = [int(date) for date in dates]
    plt.plot(dates, N_values)
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.title(' Value Over Time')
    plt.show()
    #filename = f'graph_{uuid.uuid4().hex}.png'
    filename='ssss'
    folder_path = os.path.join(settings.MEDIA_ROOT, 'graph')
    graph_path = os.path.join(folder_path, filename)
    plt.savefig(graph_path)
    plt.close()
    return HttpResponse('Graph created successfully')    

class JsonUploadNPKView(APIView):
    def post(self, request, *args, **kwargs):
        json_data = json.loads(request.body)
        my_model = ExcelNPK( data=json_data['data'])
        my_model.save()
        return JsonResponse({'status': 'success'})
    def get(self, request, *args, **kwargs):
        my_model = ExcelNPK.objects.all()
        data = [my_models.data for my_models in my_model]
        if my_model:
            return JsonResponse(data, safe=False)
        else:
            return JsonResponse({'error': 'No data found'})