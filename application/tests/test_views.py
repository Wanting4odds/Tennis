from rest_framework import status
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase


class TestResultsApiView(APITestCase):

    def test_get_results_success(self):
        response = self.client.get('/result/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_add_result_success(self):
        data = {
            "atp": 1,
            "location": "London",
            "tournament": "testing",
            "date": "2011-01-02T00:00:00Z",
            "series": "test",
            "tier": "test",
            "court": "test",
            "surface": "test",
            "round": "test",
            "best_of": 2,
            "winner": "test",
            "loser": "test",
            "wrank": 3,
            "lrank": 4,
            "wPts": 2,
            "lpts": 3,
            "w1": 8,
            "l1": 7,
            "w2": 4,
            "l2": 3,
            "w3": 2,
            "l3": 3,
            "w4": 3,
            "l4": 1,
            "w5": 4,
            "l5": 8,
            "wsets": 3,
            "lsets": 3,
            "comment": "test",
            "b365w": 4.4,
            "b365l": 2.9,
            "exw": 2.9,
            "exl": 2.9,
            "lbw": 2.9,
            "lbl": 2.9,
            "psw": 2.9,
            "psl": 2.9,
            "sjw": 2.9,
            "sjl": 2.9,
            "maxw": 2.9,
            "maxl": 2.9,
            "avgw": 2.9,
            "avgl": 2.9
        }
        response = self.client.post('/result/', data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TestResultDetailView(APITestCase):
    def test_get_by_id_success(self):
        response = self.client.get('/result/', kwargs={'pk': 367})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_success(self):
        response = self.client.delete('/result/', kwargs={'pk': 366})
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
