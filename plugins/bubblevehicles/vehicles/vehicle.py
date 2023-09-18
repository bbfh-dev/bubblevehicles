from typing import cast

from plugins.utils import quote
from .model import Model
from .structs import BoxSize, NBTByte


class BaseAttributes:
    def __init__(self, *, max_health: int, is_paintable: bool):
        self.max_health = max_health
        self.is_paintable = is_paintable


class BaseVehicle:
    @classmethod
    def get_origin(cls):
        return cls.__bases__[0].__name__

    @classmethod
    def as_dict(cls):
        """
        :return: dictionary used for summoning the vehicle
        """
        return {
            "Tags": ["+bubblevehicles", "bbfh.origin", "--bbfh.new"],
            "CustomName": quote(cls.__name__),
            "NoGravity": True,
            "Silent": True,
            "Invulnerable": True,
            "Invisible": True,
            "Small": True,
            "NoBasePlate": True,
            "PersistenceRequired": True,
            "DisabledSlots": 4144959,
            "ArmorItems": [
                {"id": "chest", "Count": NBTByte(1), "tag": {"bbfh_items": []}},
                {},
                {},
                {},
            ],
            "Passengers": [
                unit.as_dict(
                    cls.get_hitbox().x,
                    cls.get_hitbox().y,
                    cls.get_model().offset,
                )
                for unit in cls.get_model().display_entities
            ],
        }

    @classmethod
    def get_attr(cls, name: str):
        return cls.__dict__.get(name)

    @classmethod
    def get_model(cls) -> Model:
        return cast(Model, cls.get_attr("model"))

    @classmethod
    def get_hitbox(cls) -> BoxSize:
        return cast(BoxSize, cls.get_attr("hitbox"))

    @classmethod
    def get_attribute_variables(cls):
        pass
