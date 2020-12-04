from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
#from .models import gallery, gallery_type, article, news
#from .forms import GalleryForm, GalleryTypeForm, ArticleForm, NewsForm


def index(request):
    #return HttpResponse("We are starting a new website. Wish good luck!")
    return render(request, 'index.html')
