from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


def validate_pdf(value):
    if value.name.split('.')[-1] != 'pdf':
        raise ValidationError('File type not supported. Only Pdf is allowed')
    

class Document(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    document = models.FileField(validators=[validate_pdf])

    def __str__(self):
        return self.document.name
