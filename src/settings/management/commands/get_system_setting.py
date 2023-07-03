from django.core.management.base import BaseCommand
from settings.models import SystemSettings


class Command(BaseCommand):
    help = 'Get value of a system setting by key'

    def add_arguments(self, parser):
        parser.add_argument('key', type=str, help='Key of the system setting')

    def handle(self, *args, **options):
        key = options['key']
        try:
            setting = SystemSettings.objects.get(key=key)
            self.stdout.write(f'Value of {key}: {setting.value}')
        except SystemSettings.DoesNotExist:
            self.stdout.write(f'System setting with key "{key}" does not exist.')