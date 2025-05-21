from django.core import serializers
from django.core.management.base import BaseCommand

from users.models import Inventory


class Command(BaseCommand):
    help = 'Export product residues to a JSON file'

    def handle(self, *args, **options):
        # Экспорт данных из модели остатков товара
        data = serializers.serialize('json', Inventory.objects.all())
        with open('product_residues.json', 'w') as f:
            f.write(data)
        self.stdout.write(self.style.SUCCESS('Successfully exported product residues'))