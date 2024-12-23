# dispatch/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BoxViewSet, CreateBoxView, LoadBoxView, CheckLoadedItemsView, AvailableBoxesView, CheckBatteryLevelView

# Create a router and register your viewset
router = DefaultRouter()
router.register(r'boxes', BoxViewSet)  # Register the BoxViewSet with the URL 'boxes'

# Define your URL patterns
urlpatterns = [
    path('api/', include(router.urls)),  # Include the router URLs under the 'api/' prefix
    path('api/create_box/', CreateBoxView.as_view(), name='create_box'),
    path('api/load_box/<str:txref>/', LoadBoxView.as_view(), name='load_box'),
    path('api/loaded_items/<str:txref>/', CheckLoadedItemsView.as_view(), name='check_loaded_items'),
    path('api/available_boxes/', AvailableBoxesView.as_view(), name='available_boxes'),
    path('api/battery_level/<str:txref>/', CheckBatteryLevelView.as_view(), name='check_battery_level'),
]