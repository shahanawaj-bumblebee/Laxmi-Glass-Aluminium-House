from django.contrib import admin
from .models import Service, Testimonial, ContactMessage, QuoteRequest


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating')
    search_fields = ('name',)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile', 'submitted_at')
    search_fields = ('name', 'email', 'mobile')
    readonly_fields = ('name', 'email', 'mobile', 'message', 'submitted_at')


@admin.register(QuoteRequest)
class QuoteRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'service_type', 'mobile', 'submitted_at', 'is_resolved')
    list_filter = ('service_type', 'is_resolved')
    search_fields = ('name', 'email', 'mobile')
    list_editable = ('is_resolved',)
