from django.urls import include, path

from .api import api_router
from .views import EnergyChartView


urlpatterns = [
    path("api/", include(api_router.urls), name="api"),
    path("", EnergyChartView.as_view(), name="chart"),
#    path("chart/", EnergyChartView.as_view(), name="chart"),
#    path("table/", EnergyTableView.as_view(), name="table"),

]
