from django.contrib import admin
from django.urls import path
from django.urls import include
from django.http import JsonResponse


def api_root(request):
    return JsonResponse({
        "brand": "Gambit Fragrances API",
        "endpoints": {
            "products": "/api/products/",
            "register": "/api/users/register/",
            "login": "/api/users/login/",
        }
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('products.urls')),
    path('api/users/', include('users.urls')),
]
