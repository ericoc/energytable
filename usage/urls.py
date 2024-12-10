from django.urls import include, path

from .api import api_router
from .views import EnergyIndexView, EnergyChartView, EnergyTableView


urlpatterns = [
    path("api/", include(api_router.urls), name="api"),
    path("", EnergyIndexView.as_view(), name="index"),
    path("chart/", EnergyChartView.as_view(), name="chart"),
    path("table/", EnergyTableView.as_view(), name="table"),

]
