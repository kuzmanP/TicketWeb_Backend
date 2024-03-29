from django.urls import path

from .import views

from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view
from .views import UserTicketsView,EventListView

schema_view = swagger_get_schema_view(
    openapi.Info(
        title="TicketWeb API",
        default_version='1.0.0',
        description="API documentation of App",
    ),
    public=True,
)


urlpatterns = [
    path('swagger/schema/', schema_view.with_ui('swagger', cache_timeout=0), name="swagger-schema"),
    path('ticket', UserTicketsView.as_view(), name='all_tickets'),
    path('events', EventListView.as_view(), name='all_events'),
]

