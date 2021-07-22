import csv
from django.core.management import BaseCommand
from django.utils import timezone

from TechSup.models import City, Product


class Command(BaseCommand):
    help = "Loads products and cities from CSV file."

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str)

    def handle(self, *args, **options):
        start_time = timezone.now()
        file_path = options["file_path"]
        with open(file_path, "r") as csv_file:
            data = csv.reader(csv_file, delimiter=",")
            Cities = {city.country: city for city in Product.objects.all()}
            products = []
            for row in data:
                country = row[4]
                City = Cities.get(country)
                if not city:
                    City = City.objects.create(name=row[3], population=row[4])
                    Cities[city.country] = City
                city = City(
                    name=row[0],
                    country=row[1],
                    population=row[2],
                    City=City
                )
                products.append(city)
                if len(products) > 5000:
                    Product.objects.bulk_create(products)
                    products = []
            if products:
                Product.objects.bulk_create(products)
        end_time = timezone.now()
        self.stdout.write(
            self.style.SUCCESS(
                f"Loading CSV took: {(end_time-start_time).total_seconds()} seconds."
            )
        )