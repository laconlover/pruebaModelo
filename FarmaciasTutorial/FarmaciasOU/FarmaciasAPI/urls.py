from django.urls import path

from FarmaciasAPI.views import FarmaciaListView, FarmaciaDetailView

urlpatterns = [
    path('farmacia/', FarmaciaListView.as_view(), name="lista_farmacias"),
    path('farmacia/<int:pk>/', FarmaciaDetailView.as_view(), name="farmacia_individual"),
]