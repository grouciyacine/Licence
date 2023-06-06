from django.urls import path
from . import views
from .views import create_graph ,get_graph_images,generate_graph_view,get_n_data
urlpatterns = [
    path('login/',views.login_api),
    path('graph/', generate_graph_view, name='graph'),
    path('api/graph_images/', get_graph_images, name='graph_images'),
    path('api/N',get_n_data,name='n')
]
