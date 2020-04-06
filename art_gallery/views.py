from django.shortcuts import render

# Create your views here.
def art_gallery(request):
    return render(request, 'art_gallery.html', {})
