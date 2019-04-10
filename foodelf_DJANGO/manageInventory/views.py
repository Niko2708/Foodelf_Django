from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
#from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
# Create your views here.
from .models import Inventory
from .forms import PreferenceForm
from home.models import Item
###############################################################
from keras import models
import numpy as np
from keras.utils import to_categorical
import os
###############################################################

def inventoryMain(request):
    inventory = Inventory.objects.all()
    context = {"inventory":inventory}
    return render(request,"mainInventory.html",context)

def preferencesForm(request):
    form = PreferenceForm()
    context = {"form":form}
    return render(request,"detail.html",context)

def prefOut(request):
    if request.method =='POST':
        form = PreferenceForm(request.POST)
        if form.is_valid():
            price = form.cleaned_data['highPrice']
            cal = form.cleaned_data['highCal']
            ing = form.cleaned_data['ingredient']
            ##################LOAD MODEL AND WEIGHTS#####################
            #load json and create model
            json_file_dir = os.path.dirname(__file__)  # get current directory
            file_path = os.path.join(json_file_dir, 'model.json')
            
            json_file = open(file_path,'r')
            loaded_model_json = json_file.read()
            json_file.close()
            loaded_model = models.model_from_json(loaded_model_json)
            
            #load weights into new model
            weights_path = os.path.join(json_file_dir, 'weights.h5')
            loaded_model.load_weights(weights_path)
            
            
            ####################EVALUATE MODEL###########################
            #Evaluate model on test data
            loaded_model.compile(loss='categorical_crossentropy', # Cross-entropy
                            optimizer='rmsprop', # Root Mean Square Propagation
                            metrics=['accuracy']) # Accuracy performance metric
            
            x = []
            y = []
            y_items = []
            
            for i in range(-1,2):
                for j in range(-50,100,50):
                    x.append([(float(price)+(i*1.0))/8.00,(int(cal)+ j)/1500,int(ing)])
            x = np.array(x)
            output = loaded_model.predict(x)
            
            for out in output:
                max_output = -1.00
                output_itemID = -1                
                for i in range(len(out)):
                    if out[i] > max_output:
                        max_output = out[i]
                        output_itemID = i
                output_itemID+=1
                y.append(output_itemID)
            y = set(y)  #turns into a set of only unique elements
            y = list(y) #turn back into a list
            
            for id_of_item in y:
                y_items.append(Item.objects.get(pk=id_of_item))
            
            context = {"output":y_items}
            return render(request,"netOutput.html",context)  

def testComms(request):
   if request.method == "GET":
       num = random.randint(100,500)
       num = str(num)
       char = random.choice(["A","B","C","D","E","F"])
       code = char + num
       return HttpResponse(code,content_type="text/plain")

def testJSON(request):
   if request.method == "GET":
       json_dict = {}
       for item in list(Item.objects.all()):
           json_dict.update({(f'Item {item.id}'):{
                             "Item Name":item.item_name,
                             "Price":item.price,
                             "Ingredients":item.ingredients}})

       return JsonResponse(json_dict)
