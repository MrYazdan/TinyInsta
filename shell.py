import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

# from mixer.backend.django import mixer

from apps.user.models import User  # noqa:E402

# User.objects.create_user(
#     username="fardin",
#     email="fardin.zand.orginal@gmail.com",
#     password="12345678",
#     first_name="fardin",
#     last_name="zand",
# )

yazdan = User.objects.get(username="yazdan")
fardin = User.objects.get(username="fardin")

fardin.follow(yazdan)
yazdan.follow(fardin)

# print(fardin.followers)
# print(yazdan.followers)
