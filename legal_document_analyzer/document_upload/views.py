from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import DocumentForm
from .models import Document
from user_authentication.decorators import is_authenticated


@is_authenticated
def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.user = request.user
            document.save()
            messages.success(request, 'Document uploaded successfully')
        form= DocumentForm(request.POST, request.FILES)
    else:
        form = DocumentForm()
    return render(request, 'document_upload/upload_documents.html', {'form': form})


@is_authenticated
def fetch_documents(request):
    documents = Document.objects.filter(user=request.user)
    return render(request, 'document_upload/fetch_documents.html', {'documents': documents})


# @is_authenticated
def open_document(request, pk):
    document = Document.objects.get(pk=pk)
    path = document.document.path
    path = path.split('legal_document_analyzer/')[-1]
    return render(request, 'document_upload/open_document.html', {'document': document, 'path': path})



# @is_authenticated
def classify_document(request, pk):
    document = Document.objects.get(pk=pk)
    return render(request, 'document_upload/classify_document.html', {'document': document})

