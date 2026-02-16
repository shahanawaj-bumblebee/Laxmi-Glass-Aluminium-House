from django.shortcuts import render
from .models import Service, Testimonial

def home(request):
    services = Service.objects.all()
    testimonials = Testimonial.objects.all()

    return render(request, 'website/index.html', {
        "services": services,
        "testimonials": testimonials
    })

def services(request):
    services = Service.objects.all()
    return render(request, 'website/services.html', {
        'services': services
    })

def about(request):
    return render(request, 'website/about.html')

def products(request):
    return render(request, 'website/products.html')

def contact(request):
    return render(request, 'website/contact.html')

def portfolio(request):
    return render(request, 'website/portfolio.html')
