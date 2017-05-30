from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404
from django.utils import timezone
from blog.models import Suche
from .models import Post

# def post_list(request):
#     posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#     return render(request, 'blog/stadt_suchen.html', {'posts': posts})

def stadt_suchen(request):
    suchen = Suche.objects.all()
    return render(request,  'blog/stadt_suchen.html', {'suchen': suchen})

def suche_speichern(request):
    stadt_input = request.POST.get('suchanfrage', '')
    s = Suche.objects.create(text = stadt_input)
    s.save()
    return s # hier gebe ich definitiv das falsche zurück, muss irgend ein Render bla sein...



