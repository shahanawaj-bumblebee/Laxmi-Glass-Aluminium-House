from django.shortcuts import render
from .models import Service, Testimonial

def home(request):
    services = Service.objects.all()
    testimonials = Testimonial.objects.all()

    return render(request, "website/index.html", {
        "services": services,
        "testimonials": testimonials
    })


def about(request):
    return render(request, 'website/about.html')

def products(request):
    return render(request, 'website/products.html')

def services(request):
    return render(request, 'website/services.html')

def contact(request):
    return render(request, 'website/contact.html')

def portfolio(request):
    return render(request, 'website/portfolio.html')




# Create your views here.
