from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'manageInventory'
urlpatterns = [
        path('', views.inventoryMain, name='inventoryMain'),
        path('prefForm/', views.preferencesForm, name='preferencesForm'),
        path('outputForm/', views.prefOut, name='prefOut'),
        path('testComms/', views.testComms, name='testComms'),
        path('testJSON/', views.testJSON, name='testJSON'),

]
