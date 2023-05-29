from django.shortcuts import render
from .models import myprc

# Create your views here.
def home (request):
    item = myprc.objects.all()
    title='welcome'
    desc='this platform is for nothing'
    context = {'title':title,'description':desc,'item':item}
    return render (request,'index.html',context)
    
def about (request):
    
    title ='About page'
    desc = """ onekkichu likhte hobe"""
    context= {
        'title':title,
        'aboutdesc':desc,
    }
    return render(request,'demo/about.html',context)
def contact (request):
    return render (request,'contact.html')


