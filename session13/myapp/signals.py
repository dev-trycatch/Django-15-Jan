from django.dispatch import receiver
from .models import *
from django.db.models.signals import pre_save,post_save

@receiver(pre_save,sender=Blog)
def before_blog_save(sender,instance,**kwargs):
    print(f"Before save to blog  [pre-save] {instance.title}")

@receiver(post_save,sender=Blog)
def after_blog_save(sender,instance,created,**kwargs):
    if created:
        print(f'After save to blog [Post-save] {instance.title}')
    else:
        print(f"Blog Updated [Post-save] {instance.title}")