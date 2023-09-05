from django.urls import path
from . import views

urlpatterns = [
    path('',views.AIView,name="AI page"),
    path('therapist/',views.TherapistListView.as_view(),name="therapist")
]