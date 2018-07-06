# from django.db.models.signals import post_save
# from .models import UserProfile

# def create_profile(sender, **kwargs):
#     user = kwargs["instance"]
#     if kwargs["created"]:
#         user_profile = UserProfile(user=user)
#         user_profile.save()
# post_save.connect(create_profile, sender=User)