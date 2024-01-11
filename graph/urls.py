# myapp/urls.py
from django.urls import path
from . import views
app_name = 'graph'

urlpatterns = [
    path('graph/', views.graph_view, name='graph_view'),
    path("contact/", views.contact, name="ContactUs"),
    path("heart/", views.heart, name="heart"),
    path("blood/", views.blood, name="blood"),
    path("temp/", views.temp, name="temp"),
    path("pulse/", views.pulse, name="pulse"),
]


