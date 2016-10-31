from django.conf.urls import url
from snippets.views import SnippetList, SnippetDetail
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^snippets/$', SnippetList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)