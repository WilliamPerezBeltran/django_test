from django.test import TestCase
from emissions_project.usecases.get_emissions import GetEmissions
from emissions_project.infrastructure.models import EmissionModel
from emissions_project.infrastructure.repository_impl import EmissionRepositoryImpl

class GetEmissionsUseCaseProfessionalTests(TestCase):
    def setUp(self):
        self.repo = EmissionRepositoryImpl()
        self.usecase = GetEmissions(self.repo)
        self.emissions_data = [
            {"year": 2020, "emissions": 100.5, "emission_type": "CO2", "country": "Canada", "activity": "Transport"},
            {"year": 2021, "emissions": 120.8, "emission_type": "CH4", "country": "USA", "activity": "Agriculture"},
            {"year": 2022, "emissions": 95.2, "emission_type": "CO2", "country": "Canada", "activity": "Industry"},
            {"year": 2023, "emissions": 200.1, "emission_type": "N2O", "country": "Mexico", "activity": "Energy"},
            {"year": 2021, "emissions": 130.0, "emission_type": "CO2", "country": "USA", "activity": "Transport"},
        ]
        for data in self.emissions_data:
            EmissionModel.objects.create(**data)

    def test_execute_returns_all_emissions_without_filters(self):
        result = self.usecase.execute()
        self.assertEqual(len(result), len(self.emissions_data))
        years = [e.year for e in result]
        self.assertEqual(sorted(years), sorted([d["year"] for d in self.emissions_data]))
        for e in result:
            self.assertIsInstance(e.year, int)
            self.assertIsInstance(e.emissions, float)
            self.assertIsInstance(e.emission_type, str)
            self.assertIsInstance(e.country, str)
            self.assertIsInstance(e.activity, str)

    def test_execute_dynamic_filters(self):
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
                result = self.usecase.execute(filters_dict)
                self.assertEqual(len(result), expected_count)
                for emission in result:
                    for key, value in filters_dict.items():
                        self.assertEqual(getattr(emission, key), value)
                        self.assertIsInstance(getattr(emission, key), type(value))

    def test_execute_combined_filters(self):
        combined_filters = [
            ({"country": "USA", "emission_type": "CO2"}, 1),
            ({"country": "Canada", "activity": "Industry"}, 1),
            ({"country": "Mexico", "activity": "Transport"}, 0),
        ]
        for filters_dict, expected_count in combined_filters:
            with self.subTest(filters=filters_dict):
                result = self.usecase.execute(filters_dict)
                self.assertEqual(len(result), expected_count)
                for emission in result:
                    for key, value in filters_dict.items():
                        self.assertEqual(getattr(emission, key), value)
                        self.assertIsInstance(getattr(emission, key), type(value))

    def test_execute_returns_empty_list_when_no_results(self):
        filters_dict = {"country": "Spain", "activity": "Mining"}
        result = self.usecase.execute(filters_dict)
        self.assertEqual(len(result), 0)

    def test_execute_ordering_by_year(self):
        result = self.usecase.execute()
        years = [e.year for e in result]
        self.assertEqual(years, sorted(years))

    def test_execute_consistency_of_emission_objects(self):
        result = self.usecase.execute()
        for emission in result:
            self.assertTrue(hasattr(emission, "year"))
            self.assertTrue(hasattr(emission, "emissions"))
            self.assertTrue(hasattr(emission, "emission_type"))
            self.assertTrue(hasattr(emission, "country"))
            self.assertTrue(hasattr(emission, "activity"))
