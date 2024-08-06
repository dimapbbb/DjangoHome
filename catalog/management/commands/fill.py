import json

from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):

    @staticmethod
    def json_read_data():
        with open("catalog/fixtures/catalog_data.json", 'r', encoding="utf-8") as file:
            return json.load(file)

    def handle(self, *args, **options):
        Category.objects.all().delete()

        category_for_create = []

        for category in self.json_read_data():
            category_for_create.append(Category(**category["fields"]))

        Category.objects.bulk_create(category_for_create)
