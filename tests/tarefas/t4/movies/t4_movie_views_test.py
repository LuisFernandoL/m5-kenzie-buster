from rest_framework.test import APITestCase
from rest_framework.views import status
from movies.models import Movie
from rest_framework_simplejwt.tokens import RefreshToken
from tests.factories import (
    create_employee_with_token,
    create_movie_with_employee,
    create_non_employee_with_token,
    create_multiple_movies_with_employee,
)


class MovieViewsT4Test(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.BASE_URL = "/api/movies/"
        # UnitTest Longer Logs
        cls.maxDiff = None

    def test_movies_listing_pagination(self):
        employee, _ = create_employee_with_token()
        movies_count = 10
        create_multiple_movies_with_employee(employee, movies_count)

        response = self.client.get(self.BASE_URL)
        resulted_data = response.json()
        expected_pagination_keys = {"count", "next", "previous"}
        msg = "Verifique se a paginação está sendo feita corretamente"
        with self.subTest():
            for expected_key in expected_pagination_keys:
                self.assertIn(expected_key, resulted_data.keys(), msg)

        results_len = len(resulted_data["results"])
        expected_len = 2

        msg = "Verifique se a paginação está retornando apenas dois items de cada vez"
        self.assertEqual(expected_len, results_len)

