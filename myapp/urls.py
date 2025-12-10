from django.contrib import admin
from django.urls import path , include
# from myapp.views import index
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)




urlpatterns = [
    path ('admin/', admin.site.urls),
    path ("todo/" , include("todo.urls")),
    path ("student/" , include("student.urls")),
    path ("account/" , include("account.urls")),
    # path ('finance/' , include("finance.urls")),


    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)