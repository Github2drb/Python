from django.shortcuts import render, redirect
from .forms import ItemForm
from .models import Item
def index(request):
    items=Item.objects.all()
    return render(request,'myapp/index.html',{'items':items})
    
def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('myapp/index.html')  # Redirect to the index page or another page
    else:
        form = ItemForm()
    return render(request, 'myapp/add_item.html', {'form': form})
