from typing import cast

from .structs import Point
from .unit import DisplayEntity, Unit


class Model:
    def __init__(self, *, units: list[Unit], offset: Point):
        self.units = units
        self.offset = offset

    @property
    def display_entities(self) -> list[DisplayEntity]:
        return [
            cast(DisplayEntity, unit)
            for unit in self.units
            if issubclass(type(unit), DisplayEntity)
        ]
