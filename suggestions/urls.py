from django.conf.urls import url
from .views import get_suggestions, suggestion_detail, create_or_edit_suggestion, upvotes

urlpatterns = [
    url(r'^suggestions', get_suggestions, name='get_suggestions'),
    url(r'^suggestions', suggestion_detail, name='suggestion_detail'),
    url(r'^new_suggestions', create_or_edit_suggestion, name='new_suggestion'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_suggestion, name='edit_suggestion'),
    url(r'^(?P<pk>\d+)/$', upvotes, name='upvotes'),
]