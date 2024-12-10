from csv import DictReader
from datetime import date, datetime, time
from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from pathlib import Path
from ...models import EnergyUsage


class Command(BaseCommand):
    """
    Import energy usage data to the database,
    from comma-separated values ("CSV") file.
    """
    help = "Import energy usage data."

    def handle(self, *args, **options):

        # peco_electric_usage_interval_data_Service 1_1_2023-01-21_to_2023-12-07.csv
        csv_prefix = "peco_electric_usage_interval_data_Service 1_1_"
        csv_files = sorted(
            list(Path(".").glob(f"{csv_prefix}*.csv")),
            reverse=True
        )
        try:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{len(csv_files)} CSV file(s) found."
                )
            )
            num_created = 0

            for csv_file in csv_files:
                csv_path = Path(csv_file)
                csv_name = csv_path.name.replace(csv_prefix, "")
                csv_stat = csv_path.stat()
                csv_size = csv_stat.st_size

                if csv_size == 241:
                    self.stdout.write(self.style.NOTICE(f"Skipped: {csv_name}"))
                    continue

                with csv_path.open(mode="r", encoding="utf-8-sig") as read_fh:
                    csv_lines = read_fh.readlines()
                    for row in DictReader(csv_lines[6:]):
                        assert row["TYPE"] == "Electric usage", "Invalid type!"

                        # Parse the date and time columns within each CSV row.
                        time_parts = row["START TIME"].split(':')

                        # Map datetime of hour to electricity usage (in kWh).
                        usage = {
                            "hour": timezone.make_aware(
                                value=datetime.combine(
                                    date=date.fromisoformat(row["DATE"]),
                                    time=time(
                                        hour=int(time_parts[0]),
                                        minute=int(time_parts[1])
                                    )
                                )
                            ),
                            "kwh": float(row["USAGE (kWh)"])
                        }

                        # Update or create energy usage object in the database.
                        obj, created = EnergyUsage.objects.update_or_create(
                            **usage,
                            defaults=usage
                        )

                        # Show any newly created energy usage database objects.
                        if created:
                            num_created += 1
                            self.stdout.write(self.style.SUCCESS(
                                "Created:\t"
                                f"{obj.hour.strftime("%A, %B %d, %Y @ %I %p")}"
                                f" ({obj.hour}) [{obj.kwh} kWh]"
                            ))

            # List total count of newly created energy usage database objects.
            if num_created > 0:
                self.stdout.write(self.style.SUCCESS(
                    f"Total:\t\t{num_created}"
                ))
            self.stdout.write(self.style.SUCCESS("Done."))

        except Exception as exc:
            raise CommandError(exc)
