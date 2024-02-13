from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    # path('bert-classifier/<path:path>/', views.bert_classifier, name='bert_classifier'),
    path('bert-classifier/media/<path:path>/', views.bert_classifier, name='bert_classifier'),
]
