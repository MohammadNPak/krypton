from django.shortcuts import render

# Create your views here.


def krypton_index(request):
    context = {"salam": "dddd"}
    return render(request,'krypton_main\index.html ', context)


