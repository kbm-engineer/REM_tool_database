from drf_yasg import openapi
from rest_framework import permissions
from drf_yasg.views import get_schema_view


SCHEMA_VIEW = get_schema_view(
    openapi.Info(
        title="База данных инструмента РЭМ",
        default_version='v0.1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)