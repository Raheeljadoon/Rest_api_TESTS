from django.conf.urls import url

from . import views

urlpatterns = [
    url('api/v1/puppies/(?P<pk>[0-9]+)', views.get_delete_update_puppy, name='get_delete_update_puppy' ),
    url('api/v1/puppies/', views.get_post_puppy,name='get_post_puppy')
]
