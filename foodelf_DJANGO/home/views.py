from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from .models import Item, Choice
#from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
#
#simpler way of doing index function with 'render', but really only saves one line of code
#it automatically sends an HttpResponse
#
#def index(request):
#   item_list = Item.objects.all()
#   context = {'item_list':item_list}
#   return render(request, 'home/index.html',context)

def index(request):
    item_list = Item.objects.order_by('item_id')
    context = {'item_list':item_list,}
    return render(request, 'home/index.html', context)

def menu(request):
    item_list = Item.objects.order_by('item_id')
    context = {'item_list':item_list,}
    return render(request, 'home/menu.html', context)    

def detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'home/detail.html', {'item':item})
    #return render(request, 'home/detail.html', {'item':item})

def results(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    choice_history = Choice.objects.all()
    return render(request, 'home/results.html', {'item':item,'choice_history':choice_history})

def purchase(request, item_id):
    if request.method == 'POST':
        item = get_object_or_404(Item, pk=item_id)
        try:
            quantity_text = request.POST['textfield']
            choice_quantity = int(quantity_text)
        except(KeyError, Choice.DoesNotExist):
            return render(request, 'home/detail.html',{'item':item,'error_message':"You didn't select a choice.",}) 
        else:
            item.choice_set.create(quantity=choice_quantity,date=timezone.now())
            return HttpResponseRedirect(reverse('home:results', args=(item.id,)))
    else:
        return HttpResponseRedirect(reverse('home:detail', args=(item.id,)))

# Create your views here.
