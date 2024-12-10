from django.views.generic import TemplateView, ListView

from .models import EnergyUsage


class EnergyUsageBaseView(TemplateView):
    """Base energy usage view."""
    http_method_names = ("get",)
    model = EnergyUsage
    title = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["TITLE"] = self.title
        return context


class EnergyIndexView(ListView, EnergyUsageBaseView):
    """Energy usage index view."""
    context_object_name = "items"
    model = EnergyUsage
    queryset = model.objects.all()
    template_name = "index.html"
    title = "Index"


class EnergyTableView(EnergyUsageBaseView):
    """Energy usage table view."""
    template_name = "table.html"
    title = "Table"


class EnergyChartView(EnergyUsageBaseView):
    """Energy usage chart view."""
    template_name = "chart.html"
    title = "Chart"
