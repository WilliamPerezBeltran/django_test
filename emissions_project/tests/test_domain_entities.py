from django.test import SimpleTestCase
from emissions_project.domain.entities import Emission
from emissions_project.domain.repositories import EmissionRepository
from abc import ABC, ABCMeta
from dataclasses import is_dataclass

class EmissionEntityTests(SimpleTestCase):
    def setUp(self):
        self.emission_data = {
            "year": 2024,
            "emissions": 150.75,
            "emission_type": "CO2",
            "country": "Canada",
            "activity": "Transport"
        }
        self.emission = Emission(**self.emission_data)

    def test_is_dataclass(self):
        self.assertTrue(is_dataclass(self.emission))

    def test_field_values_and_types(self):
        for field, value in self.emission_data.items():
            with self.subTest(field=field):
                self.assertEqual(getattr(self.emission, field), value)
                expected_type = type(value)
                self.assertIsInstance(getattr(self.emission, field), expected_type)

    def test_equality_and_inequality(self):
        same_emission = Emission(**self.emission_data)
        self.assertEqual(self.emission, same_emission)

        different_data = self.emission_data.copy()
        different_data["year"] = 2025
        different_emission = Emission(**different_data)
        self.assertNotEqual(self.emission, different_emission)

    def test_str_representation(self):
        text = f"{self.emission.country} - {self.emission.year} ({self.emission.emission_type})"
        for field_value in ["Canada", "2024", "CO2"]:
            with self.subTest(value=field_value):
                self.assertIn(str(field_value), text)


class EmissionRepositoryInterfaceTests(SimpleTestCase):
    def test_is_abstract_class(self):
        self.assertTrue(issubclass(EmissionRepository, ABC))
        self.assertTrue(isinstance(EmissionRepository, ABCMeta))

    def test_has_list_method_and_is_abstract(self):
        self.assertTrue(hasattr(EmissionRepository, "list"))
        method = getattr(EmissionRepository, "list")
        self.assertTrue(hasattr(method, "__isabstractmethod__"))

    def test_cannot_instantiate_abstract_repository(self):
        with self.assertRaises(TypeError):
            EmissionRepository()

    def test_concrete_repository_must_implement_list(self):
        class DummyRepo(EmissionRepository):
            pass

        with self.assertRaises(TypeError):
            DummyRepo()
