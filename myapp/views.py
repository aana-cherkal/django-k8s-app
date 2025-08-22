from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm

# Create your views here.
def index(request):
    item_list = Item.objects.all()
    return render(request, 'myapp/index.html', {'item_list':item_list})

def detail(request, id):
    i = Item.objects.get(id = id)
    context = {'item': i}
    return render(request, 'myapp/detail.html', context)
    #return HttpResponse(f"detail of {i}")

def create_item(request):
    form = ItemForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('myapp:index')
    
    context = {
        'form': form
    }
    return render(request, 'myapp/item-form.html', context)

def update_item(request, id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance= item)
    if form.is_valid():
        form.save()
        return redirect('myapp:index')
    context = {
        'form': form
    }
    return render(request, 'myapp/item-form.html',context)

def delete_item(request, id):
    item = Item.objects.get(id = id)
    if request.method == 'POST':
        item.delete()
        return redirect('myapp:index')
    return render(request, 'myapp/item-delete.html')


