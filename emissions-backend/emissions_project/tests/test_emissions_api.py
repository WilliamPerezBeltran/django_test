from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from emissions_project.infrastructure.models import EmissionModel


class EmissionsAPITests(APITestCase):
    def setUp(self):
        self.emissions_data = [
            {
                "year": 2020,
                "emissions": 100.5,
                "emission_type": "CO2",
                "country": "Canada",
                "activity": "Transport",
            },
            {
                "year": 2021,
                "emissions": 120.8,
                "emission_type": "CH4",
                "country": "USA",
                "activity": "Agriculture",
            },
            {
                "year": 2022,
                "emissions": 95.2,
                "emission_type": "CO2",
                "country": "Canada",
                "activity": "Industry",
            },
            {
                "year": 2023,
                "emissions": 200.1,
                "emission_type": "N2O",
                "country": "Mexico",
                "activity": "Energy",
            },
            {
                "year": 2021,
                "emissions": 130.0,
                "emission_type": "CO2",
                "country": "USA",
                "activity": "Transport",
            },
        ]
        for data in self.emissions_data:
            EmissionModel.objects.create(**data)
        self.url = reverse("emission-list")

    def test_list_all_emissions(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), len(self.emissions_data))

    def test_dynamic_single_filters(self):
        filters = [
            ("country", "Canada", 2),
            ("country", "USA", 2),
            ("activity", "Transport", 2),
            ("emission_type", "CO2", 3),
            ("emission_type", "N2O", 1),
            ("country", "Spain", 0),
        ]
        for field, value, expected_count in filters:
            with self.subTest(field=field, value=value):
                response = self.client.get(self.url, {field: value})
                self.assertEqual(response.status_code, status.HTTP_200_OK)
                self.assertEqual(len(response.data), expected_count)
                for record in response.data:
                    self.assertEqual(record[field], value)

    def test_combined_filters(self):
        combined_filters = [
            ({"country": "USA", "emission_type": "CO2"}, 1),
            ({"country": "Canada", "activity": "Industry"}, 1),
            ({"country": "Mexico", "activity": "Transport"}, 0),
        ]
        for filters_dict, expected_count in combined_filters:
            with self.subTest(filters=filters_dict):
                response = self.client.get(self.url, filters_dict)
                self.assertEqual(response.status_code, status.HTTP_200_OK)
                self.assertEqual(len(response.data), expected_count)
                for record in response.data:
                    for key, value in filters_dict.items():
                        self.assertEqual(record[key], value)

    def test_ordering_by_year(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [record["year"] for record in response.data]
        self.assertEqual(years, sorted(years))

    def test_response_structure_and_types(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_fields = {
            "id",
            "year",
            "emissions",
            "emission_type",
            "country",
            "activity",
        }
        for record in response.data:
            self.assertTrue(expected_fields.issubset(record.keys()))
            self.assertIsInstance(record["id"], int)
            self.assertIsInstance(record["year"], int)
            self.assertIsInstance(record["emissions"], float)
            self.assertIsInstance(record["emission_type"], str)
            self.assertIsInstance(record["country"], str)
            self.assertIsInstance(record["activity"], str)

    def test_empty_results(self):
        response = self.client.get(self.url, {"country": "Spain", "activity": "Mining"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)
