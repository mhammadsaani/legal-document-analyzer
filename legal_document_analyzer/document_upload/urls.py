from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from . import views


urlpatterns = [
    path('upload/', views.upload_document, name='upload_document'),
    path('fetch-documents/', views.fetch_documents, name='fetch_documents'),
    path('open-document/<int:pk>/', views.open_document, name='open_document'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    


