from datetime import datetime
from django.urls import reverse
import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db
class TestPostApi:
    def test_get_post_response_200_status(self):
        client = APIClient()
        url = reverse("blog:api-v1:post_list")
        response = client.get(url)
        assert response.status_code == 200

        def test_create_post_response_401_status(self):
            url = reverse("blog:api-v1:post_list")
            data = {
                "title": "test",
                "content": "description",
                "status": True,
                "published_date": datetime.now(),
            }
            response = self.client.post(url, data)
            assert response.status_code == 401

        def test_render_views():
            url = reverse("blog:api-v1:post_list")
            response = self.client.get(url)
            assert response.status_code == 200


#         def test_serializer_with_valid_data():
#             input_data = {'key': 'value'}
#             expected_output = '{"key": "value"}'
#             result = serialize(input_data)
#             assert result == expected_output

# def test_serialize_deserialize():
#     input_data = {'key': 'value'}
#     serialized = serialize(input_data)
#     deserialized = deserialize(serialized)
#     assert input_data == deserialized
