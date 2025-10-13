from dataclasses import dataclass

@dataclass
class Emission:
    year: int
    emissions: float
    emission_type: str
    country: str
    activity: str
