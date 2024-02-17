from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
from .forms import CreateNewList

# Create your views here.
def index(response, id):
    ls = ToDoList.objects.get(id=id)

    if response.method == "POST":
        print(response.POST)
        if response.POST.get("save"):
            for item in ls.item_set.all():
                if response.POST.get("c"+str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False
                
                item.save()
        elif response.POST.get("newItem"):
            txt = response.POST.get("new_text")

            if len(txt) > 2:
                ls.item_set.create(text=txt, complete=False)
            else:
                print("input invalid")

    return render(response, "main/list.html", {"ls": ls})

def home(response):
    return render(response, "main/home.html", {})

def create(response):
    form = CreateNewList()
    return render(response, "main/create.html", {"form": form})