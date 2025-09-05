from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def health_check(request):
    return JsonResponse({'status': 'healthy', 'message': 'Django app is running'})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include('chatapp.urls')),
    path('health/', health_check, name='health_check'),
    path('', health_check, name='root_health_check'),
]
