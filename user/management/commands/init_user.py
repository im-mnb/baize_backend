from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from user.status import UserRole

User = get_user_model()

class Command(BaseCommand):
    def handle(self, *args, **options):
        User.objects.filter(role=UserRole.ADMIN.value)
        user = User(username="admin", email="admin@mail.com", role=UserRole.ADMIN.value)
        user.set_password("BZ123!")
        user.save()