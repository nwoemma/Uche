from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
def header_view(request, page_name):
    titles = {
        'home':"Tasty - Home",
        'authenticated_home':"Tasty - Home",
        'about': 'Tasty - About Us',
        'gallery':'Tasty - Our Gallery',
        'menu':'Tasty - Our Menu',
        'contact':'Tasty - Contact Us',
        'reservation':"Tasty - Our Reservation",    
    }
    titles.get(page_name,"Default titles")
    return render(request, f"{page_name}.html", {"page_titles":titles})
def index(request):
    return render(request, 'pages/index.html', {'page_title': 'Tasty - Home'})
@login_required
def authenticated_home(request):
    return render(request, 'pages/authenticated_home.html', {'page_title': 'Tasty - Home'})
def about(request):
    return render(request, "pages/about.html",{'page_title': 'Tasty - About Us'})
def gallery(request):
    return render(request, 'pages/gallery.html',{'page_title': 'Tasty - Our Gallery'})
def menu(request):
    return render(request, 'pages/menu.html',{'page_title': 'Tasty - Our Menu'})
def contact(request):
    return render(request, 'pages/contact.html',{'page_title': 'Tasty - Contact Us'})
def reservation(request):
    return render(request, 'pages/reservation.html',{'page_title': 'Tasty - Our Reservation'})