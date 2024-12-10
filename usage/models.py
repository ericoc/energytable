from django.db import models


class EnergyUsage(models.Model):
    """Energy usage table."""

    hour = models.DateTimeField(
        primary_key=True,
        help_text="Start of an hour of energy usage.",
        verbose_name="Hour"
    )
    kwh = models.DecimalField(
        max_digits=7,
        decimal_places=4,
        help_text="Amount of energy used, in kilowatt-hours (kWh) in an hour.",
        verbose_name="Kilowatt-Hours (kWh)",
    )

    class Meta:
        managed = True
        db_table = "usage"
        ordering = ("hour",)
        verbose_name = verbose_name_plural = "Energy Usage"
