from django.shortcuts import render

def index(request):
    context = {"nama": "Johannes Nichola Simatupang", "kelas": "PBP A"}
    return render(request, "main/index.html", context)
