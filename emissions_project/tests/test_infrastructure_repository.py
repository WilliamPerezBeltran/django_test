from django.test import TestCase
from emissions_project.infrastructure.repository_impl import EmissionRepositoryImpl
from emissions_project.infrastructure.models import EmissionModel


class EmissionRepositoryImplTests(TestCase):
    def setUp(self):
        self.repo = EmissionRepositoryImpl()
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

    def test_list_all_emissions(self):
        result = self.repo.list()
        self.assertEqual(len(result), len(self.emissions_data))
        years = [e.year for e in result]
        self.assertEqual(
            sorted(years), sorted([d["year"] for d in self.emissions_data])
        )

    def test_list_with_dynamic_filters(self):
        dynamic_filters = [
            ({"country": "Canada"}, 2),
            ({"country": "USA"}, 2),
            ({"activity": "Transport"}, 2),
            ({"emission_type": "CO2"}, 3),
            ({"emission_type": "N2O"}, 1),
            ({"country": "Spain"}, 0),
        ]
        for filters_dict, expected_count in dynamic_filters:
            with self.subTest(filters=filters_dict):
                result = self.repo.list(filters_dict)
                self.assertEqual(len(result), expected_count)
                for emission in result:
                    for key, value in filters_dict.items():
                        self.assertEqual(getattr(emission, key), value)

    def test_combined_filters(self):
        combined_filters = [
            ({"country": "USA", "emission_type": "CO2"}, 1),
            ({"country": "Canada", "activity": "Industry"}, 1),
            ({"country": "Mexico", "activity": "Transport"}, 0),
        ]
        for filters_dict, expected_count in combined_filters:
            with self.subTest(filters=filters_dict):
                result = self.repo.list(filters_dict)
                self.assertEqual(len(result), expected_count)
                for emission in result:
                    for key, value in filters_dict.items():
                        self.assertEqual(getattr(emission, key), value)

    def test_result_types(self):
        result = self.repo.list()
        for emission in result:
            self.assertIsInstance(emission.year, int)
            self.assertIsInstance(emission.emissions, float)
            self.assertIsInstance(emission.emission_type, str)
            self.assertIsInstance(emission.country, str)
            self.assertIsInstance(emission.activity, str)
