from django.contrib import admin
from django.urls import path
from user_management.views import *
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register', register),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/employeeinfo', EmployeeView.as_view(), name="employeeinfo")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
