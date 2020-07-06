from django.urls import path

# Views
from .views import hello as hello_views

urlpatterns = [
    path(
        route='',
        view=hello_views.hello,
        name='hello'),
]
