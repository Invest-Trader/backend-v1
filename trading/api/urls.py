
from django.contrib import admin
from django.urls import path,re_path,include
from rest_framework_simplejwt import views as jwt_views
from api import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
path('', views.HelloView.as_view(), name='hello'),
path('token/', jwt_views.TokenObtainPairView.as_view()),
path('token/refresh/', jwt_views.TokenRefreshView.as_view()),
path('create_user/', views.register_user),
path('delete_user/', views.delete_user),
path('upload_documents/', views.upload_documents),
path('change_password/', views.ChangePasswordView.as_view()),
path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
