from django.shortcuts import render, redirect

from myhome.models import Article
from myhome.forms import ArticleForm

# Create your views here.
def index(request):
    return render(request, 'myhome/index.html')

def board(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'myhome/board.html', context)

def new(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            new_article = form.save()
            return redirect('board')
    else:
        form = ArticleForm()
        context = {
            'form': form
        }
        return render(request, 'myhome/forms.html', context)

def detail(request, id):
    article = Article.objects.get(id=id)
    context = {
        'article': article
    }
    return render(request, 'myhome/detail.html', context)

def update(request, id):
    article = Article.objects.get(id=id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            new_article = form.save()
            return redirect('detail', id=article.id)
    else:
        form = ArticleForm(instance=article)
        context = {
            'form': form
        }
        return render(request, 'myhome/forms.html', context)

def delete(request, id):
    article = Article.objects.get(id=id)
    if request.method == 'POST':
        article.delete()
        return redirect('board')
