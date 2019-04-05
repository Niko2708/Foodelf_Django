from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static
#from .views import *

app_name = 'manageTables'
urlpatterns = [
        path('', views.index, name='index'),
        path('<int:table_id>/', views.summary, name='summary'),
        path('<int:table_id>/menu/', views.sendToMenu, name='sendToMenu'),
        path('<int:table_id>/<int:item_id>/addItemToBill/', views.addItemToBill, name='addItemToBill'),
        path('createTable/', views.createTable, name='createTable'),
        #path('menu/', views.menu, name='menu'),
]