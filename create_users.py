from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Creates multiple users'

    def add_arguments(self, parser):
        parser.add_argument('usernames', nargs='+', type=str)

    def handle(self, *args, **options):
        for username in options['usernames']:
            User.objects.create_user(username=username, password='default_password')
            self.stdout.write(self.style.SUCCESS(f"User '{username}' created successfully."))