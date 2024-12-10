from rest_framework.routers import DefaultRouter
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import EnergyUsage


class EnergyUsageSerializer(ModelSerializer):
    """Django-Rest-Framework (DRF) serializer for energy usage API endpoint."""
    class Meta:
        model = EnergyUsage
        fields = "__all__"


class APIEnerguUsageViewSet(ReadOnlyModelViewSet):
    """Energy usage in gallons per day."""
    fields = "__all__"
    filterset_fields = ("date",)
    model = EnergyUsage
    queryset = model.objects
    serializer_class = EnergyUsageSerializer


api_router = DefaultRouter()
api_router.register(prefix=r"usage", viewset=APIEnerguUsageViewSet)
