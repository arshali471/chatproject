from django.shortcuts import render
from testapp.models import MessageModel

# Create your views here.
def home_view(request):
    
    return render(request,'home.html')
