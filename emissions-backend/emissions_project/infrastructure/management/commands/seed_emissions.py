from django.core.management.base import BaseCommand
from emissions_project.infrastructure.models import EmissionModel
import random

class Command(BaseCommand):
    help = "Seeds the database with 100 emission records."

    def handle(self, *args, **options):
        activities = ["Air travel", "Waste", "Transport", "Agriculture"]
        countries = ["United Kingdom", "Canada", "USA"]
        emission_types = ["CO2", "N2O", "CH4"]
        years = list(range(1970, 2026))

        self.stdout.write("Deleting old emissions data...")
        EmissionModel.objects.all().delete()

        self.stdout.write("Creating new emission records...")
        emissions = []
        for _ in range(100):
            emissions.append(
                EmissionModel(
                    activity=random.choice(activities),
                    country=random.choice(countries),
                    emission_type=random.choice(emission_types),
                    emissions=round(random.uniform(1.0, 300.0), 2),
                    year=random.choice(years),
                )
            )

        EmissionModel.objects.bulk_create(emissions)
        self.stdout.write(self.style.SUCCESS("Seeds emissions created successfully!"))

