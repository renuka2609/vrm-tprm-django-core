from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("", lambda request: JsonResponse({"status": "Core Backend API running"})),
    path("admin/", admin.site.urls),
    path('api/', include('vendors.urls')),
    path("api/", include("templates.urls")),

    # AUTH
    path("api/auth/", include("accounts.urls")),

    # SWAGGER
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema")),
]
