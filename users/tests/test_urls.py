from django.test import SimpleTestCase
from django.urls import reverse, resolve
from users.api.views import *


class TestUrls(SimpleTestCase):
    def test_list_url_is_resolved(self):
        url = reverse('users:user-list')  # base name
        print(resolve(url))
        self.assertEquals(resolve(url).func, UserViewSet.as_view(actions={'get': 'list'}))

