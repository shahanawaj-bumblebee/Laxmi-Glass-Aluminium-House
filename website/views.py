from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Service, Testimonial
from .forms import ContactForm, QuoteRequestForm


def home(request):
    services = Service.objects.all()
    testimonials = Testimonial.objects.all()
    return render(request, 'website/index.html', {
        'services': services,
        'testimonials': testimonials,
    })


def services(request):
    services = Service.objects.all()
    return render(request, 'website/services.html', {
        'services': services,
    })


def about(request):
    return render(request, 'website/about.html')


def products(request):
    return render(request, 'website/products.html')


def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you! Your message has been received. We will get back to you soon.')
            return redirect('contact_us')
        else:
            messages.error(request, 'Please correct the errors below.')
    return render(request, 'website/contact.html', {'form': form})


def portfolio(request):
    return render(request, 'website/portfolio.html')


def get_quote(request):
    form = QuoteRequestForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you! Your quote request has been submitted. We will contact you shortly.')
            return redirect('get_quote')
        else:
            messages.error(request, 'Please correct the errors below.')
    return render(request, 'website/get_quote.html', {'form': form})
