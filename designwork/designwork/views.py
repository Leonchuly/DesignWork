from django.shortcuts import render
from gallery.models import Gallery

def main(request):
    gallerys = Gallery.objects
    return render(request,'main.html',{'gallerys': gallerys})