from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about_us/",views.about_us, name="about_us"),
    path("contact_us/",views.contact_us, name="contact_us"),
    path("property_list/", views.property_list, name="property_list"),
    path('property_detail/<str:property_title>/', views.property_detail, name='property_detail'),
    path('land_list/', views.land_list, name='land_list'),
    path('land_detail/<int:land_id>/', views.land_detail, name='land_detail')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)