from django.http import HttpResponse
from django.shortcuts import render

menu=["О сайте", "Добавить статью", "Обратная связь","Войти"]

def index(request):
   return render(request,'women/index.html',{'menu':menu,'title':'Главная страница'})

def about(request):
   return render(request,'women/about.html',{'menu':menu,'title':'О сайте'})

def categories(request, catid):
   return HttpResponse(f"<h1>Страница приложения</h1><b>{catid}</b>")
