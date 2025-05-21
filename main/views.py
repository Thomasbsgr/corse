from django.shortcuts import render
#from .models import ObjectName

def index(request):
 #name1 = ObjectName.objects.all().order_by('')
 return render(request, 'main/index.html')#, {'pizzas': pizzas})
