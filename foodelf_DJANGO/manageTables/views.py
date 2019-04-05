from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from home.models import Item, Choice
from .models import Customer, ActiveTables, Server
#from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from .forms import NewTableForm
# Create your views here.

def index(request):
    table_list = ActiveTables.objects.order_by('id')
    form = NewTableForm()
    context = {'table_list':table_list,'form':form}
    return render(request, 'tableView.html', context)

def summary(request, table_id):
    table = get_object_or_404(ActiveTables, pk=table_id)
    ordered_items = []
    subtotal = 0.0
    customer_list=[]
    menu_list = Item.objects.order_by('item_id')
    
    for customer in table.customer_set.all():
        customer_list.append(customer)
        for choice in customer.choice_set.all():
            ordered_items.append(choice.item)
            
    for choice in table.choice_set.all():
        ordered_items.append(choice.item)
            
    for p in ordered_items:
        subtotal += p.price
        
    context = {'ordered_items':ordered_items,'subtotal':subtotal,'table_id':table_id,'customer_list':customer_list, 'menu_list':menu_list}
    return render(request, 'summary.html',context)

def sendToMenu(request, table_id):
    item_list = Item.objects.order_by('item_id')
    table = get_object_or_404(ActiveTables, pk=table_id)
    context = {'item_list':item_list, 'table':table}
    return render(request, 'menu.html', context)

def addItemToBill(request, table_id, item_id):
    table = get_object_or_404(ActiveTables, pk=table_id)
    table.choice_set.create(item=Item.objects.get(pk=item_id), quantity=1, date=timezone.now())
    return HttpResponseRedirect(reverse('manageTables:summary', args=(table.id,)))

def createTable(request):
    if request.method =='POST':
        form = NewTableForm(request.POST)
        if form.is_valid():
            server_name = form.cleaned_data['server_name']
            table_number = form.cleaned_data['table_number']
            try:
                ActiveTables.objects.create(tableNumber=int(table_number),server=Server.objects.get(name=server_name),time=timezone.now())
            except(KeyError, Server.DoesNotExist):
                return render(request, 'tableView.html',{'error_message':"Server Does not exist.",})     
            return HttpResponseRedirect(reverse('manageTables:index', args=()))