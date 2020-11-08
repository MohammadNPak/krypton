from django.shortcuts import render

# Create your views here.


def krypton_main(request):
    context = {}
    return render(request,'krypton_main\index.html ', context)