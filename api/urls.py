from django.urls import path
from .views import plan_trip, plan_style

urlpatterns = [
    path("plan-trip/", plan_trip, name="plan-trip"),
    path("plan-style/", plan_style, name="plan-style")
]