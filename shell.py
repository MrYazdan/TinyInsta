import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from apps.user.models import User  # noqa:E402
from apps.post.models import Post  # noqa:E402

# User.objects.create_user(
#     username="fardin",
#     email="fardin.zand.orginal@gmail.com",
#     password="12345678",
#     first_name="fardin",
#     last_name="zand",
# )

yazdan = User.objects.get(username="yazdan")
fardin = User.objects.get(username="fardin")

post = Post.objects.get(id=12)

# fardin.follow(yazdan)
# yazdan.follow(fardin)

# print(fardin.followers)
# print(yazdan.followers)

# mixer.cycle(5).blend(Post, author=yazdan, tags=None)

# print(*Post.objects.all(), sep="\n")
# print(Post.objects.filter(~models.Q(is_active=True)).query, sep="\n")
# print("=" * 20)
# print(Post.objects.exclude(is_active=True).query, sep="\n")
# Like.objects.create(user=yazdan, post=Post.objects.get(id=12))
# Like.objects.create(user=fardin, post=Post.objects.get(id=12))
# Comment.objects.create(post=post, user=fardin, content="Salam be maktabia !")
# Comment.objects.create(post=post, user=fardin, content="Ey baba mage commentaro mikhoonid ?")
# Comment.objects.create(post=post, user=yazdan, content="🙃")
# Comment.objects.create(post=post, user=yazdan, content="👾", reply_id=1)
# Comment.objects.get(post=post, user=fardin, content="🤨", reply_id=5)
# Comment.objects.get(post=post, user=fardin, content="🤨", reply_id=5)
# Comment.objects.create(post=post, user=fardin, content="🤨", reply_id=5)
# Comment.objects.create(post=post, user=yazdan, content="😍", reply_id=7)

# yazdan.set_password("1")
# yazdan.save()

# from rest_framework.authtoken.models import Token
# token = Token.objects.create(user=yazdan)
# print(token.key)

# print(Post.objects.filter(author=yazdan).query)
# print(Post.objects.select_related('author').filter(author=yazdan).query)
# print(Post.objects.annotate(likes_count=Count('likes')).get(id=12))
