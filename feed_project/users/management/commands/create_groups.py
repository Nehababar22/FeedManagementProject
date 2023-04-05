from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group

GROUPS = ['Admin', 'Manager']

class Command(BaseCommand):
    """ management command for creating groups """

    help = 'Create Groups'

    def handle(self, *args, **options):
        for group_name in GROUPS:
            # get or create group
            group = Group.objects.get_or_create(name=group_name)
            