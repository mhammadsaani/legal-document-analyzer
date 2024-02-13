from django.contrib import admin
from django.urls import path, include
import user_authentication

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user_authentication.urls')),
    path('auth/', include('user_authentication.urls')),
    path('doc/', include('document_upload.urls')),
    path('model/', include('nlp_models.urls'))
]
