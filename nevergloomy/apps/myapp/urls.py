from django.conf.urls import patterns, url, include
from apps.myapp import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'events', views.EventViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login urls for the browseable API

urlpatterns = patterns('',
	url(r'^', include(router.urls)),
)
