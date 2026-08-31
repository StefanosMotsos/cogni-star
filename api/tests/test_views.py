from rest_framework import status
from rest_framework.test import APITestCase

class PersonViewSetTest(APITestCase):

    def test_list_requires_authentication(self):

        url = "/api/people/"

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)