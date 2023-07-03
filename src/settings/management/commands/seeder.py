from django.core.management.base import BaseCommand
from settings.models import SystemSettings


class Command(BaseCommand):
    help = 'Seed SystemSettings data'

    def handle(self, *args, **options):
        # SystemSettings.objects.all().delete()

        settings = [
            {
                'key': 'setting1',
                'value': 'value1',
                'description': 'Описание настройки 1',
            },
            {
                'key': 'setting2',
                'value': 'value2',
                'description': 'Описание настройки 2',
            },
        ]

        for setting_data in settings:
            try:
                SystemSettings.objects.create(**setting_data)
            except:
                pass

        self.stdout.write(self.style.SUCCESS('SystemSettings data seeded successfully.'))
