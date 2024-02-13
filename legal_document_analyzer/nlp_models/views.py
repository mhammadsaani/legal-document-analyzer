from django.shortcuts import render
from django.http import HttpResponse
from .bert_classifier import extract_text_from_pdf, predict_ndas
from .constants import BASE_DIR


def bert_classifier(request, path):
    absolute_path = BASE_DIR + path
    text = extract_text_from_pdf(absolute_path)
    result = predict_ndas(text)
    predicted_label = result['File']['predicted_label']
    probabilities = result['File']['probabilities'][::-1]
    predicted_label = "NDA" if predicted_label == 1 else 'Not NDA'
    return render(request, 'nlp_models/bert_classifier.html', {'predicted_label': predicted_label, 'probabilities': probabilities, 'path': path})