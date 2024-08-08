from django.shortcuts import render
from .models import *
# Create your views here.


def home(request):
    last_picture = Photo.objects.last()
    last_pictures = Photo.objects.all().order_by('-id')
    categories = Category.objects.all()
    data = {'last_pictures':last_pictures, 'categories':categories}
    return render(request, 'index.html', data)


def category(request, category_id):
    photos = Photo.objects.filter(category_id=category_id)
    data = {'photos': photos, 'category': category}
    return render(request, 'category.html', data)


def picture(request, picture_id):
    picture = Photo.objects.get(id=picture_id)
    data = {'picture': picture}    
    if not request.session.get('picture'):
        request.session['picture'] = []
        request.session['picture'].append(picture.id)
        picture.views += 1
    elif picture.id not in request.session['picture']:
        picture.views += 1
        request.session['picture'].append(picture.id)
        request.session.save()
    picture.save()
    return render(request, 'picture.html', data)
