from django.shortcuts import render

def main(request):
    return render(request, 'posts/main.html')
# Create your views here.
