from csv import DictReader
from datetime import date
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from ...models import EnergyUsage


class Command(BaseCommand):
    """
    Import energy usage data to the database,
    from comma-separated values ("CSV") file.
    """
    help = "Import energy usage data."

    def handle(self, *args, **options):

        num_created = 0
        try:
            # Open comma-separated values ("CSV") file of energy usage data.
            with open(file=settings.IMPORT_FILENAME, mode="r") as csv_fh:

                # Iterate each row of the CSV file.
                for csv_row in DictReader(csv_fh):

                    # Ensure the row is measuring gallons (not CCFs, etc.)
                    assert csv_row[" Units"] == " Gallons", "Invalid unit."

                    # Parse the date column within each CSV row.
                    date_parts = csv_row[" Time Interval"].strip().split('/')
                    date_iso = \
                        f"{date_parts[2]}-{date_parts[0]}-{date_parts[1]}"

                    # Create dictionary mapping hour to energy usage in gallons.
                    usage = {
                        "date": date.fromisoformat(date_iso),
                        "gallons": float(csv_row[" Consumption"].strip())
                    }

                    # Update or create the energy usage object in the database.
                    obj, created = EnergyUsage.objects.update_or_create(
                        **usage,
                        defaults=usage
                    )

                    # Show any newly created energy usage database objects.
                    if created:
                        num_created += 1
                        self.stdout.write(self.style.SUCCESS(
                            f"Created:\t{obj.date.strftime("%A, %B %d, %Y")}"
                            f" ({obj.date}) [{obj.gallons} gallons]"
                        ))

            # List total count of newly created energy usage database objects.
            if num_created > 0:
                self.stdout.write(self.style.SUCCESS(
                    f"Total:\t\t{num_created}"
                ))
            self.stdout.write(self.style.SUCCESS("Done."))

        except Exception as exc:
            raise CommandError(exc)
