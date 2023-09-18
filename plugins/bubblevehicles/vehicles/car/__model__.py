from typing import cast

from plugins.utils import quote
from ..nbt import as_nbt_string
from ..structs import BoxSize, PlayerHead, Point
from ..unit import Block, Item
from ..vehicle import BaseAttributes, BaseVehicle


class CarAttributes:
    def __init__(
        self,
        base: BaseAttributes,
        *,
        max_speed: int,
        front_wheels: BoxSize,
        rear_wheels: BoxSize,
        seats: list["Car.Seat"],
    ):
        self.base = base
        self.max_speed = max_speed
        self.front_wheels = front_wheels
        self.rear_wheels = rear_wheels
        self.seats = seats


class Car(BaseVehicle):
    class Wheel:
        def __init__(self, side: str, x: float, y: float):
            self.side = side
            self.x = x
            self.z = y

    class Seat:
        def __init__(self, is_driver_seat: bool, pos: Point):
            self.is_driver_seat = is_driver_seat
            self.pos = pos

    @classmethod
    def as_partial_dict(cls):
        return {}

    @classmethod
    def get_wheels(cls):
        return [
            "summon interaction ~{} ~ ~{} {}".format(
                wheel.x,
                wheel.z,
                as_nbt_string(
                    {
                        "Tags": [
                            "+bubblevehicles",
                            "bbfh.wheel",
                            f"--bbfh.{wheel.side}",
                            "--bbfh.new",
                        ],
                        "width": 0.66,
                        "height": 0.66,
                        "Passengers": [
                            Item(
                                "wheel",
                                Point(0.5, 0.5, 1.512),
                                Point(0, 0, 90),
                                Point(1.25),
                                "player_head",
                                {"SkullOwner": PlayerHead.WHEEL.value},
                            ).as_dict(1.0, 1.0, Point(0))
                        ],
                    }
                ),
            )
            for wheel in [
                Car.Wheel(
                    "front",
                    -cls.get_attributes().front_wheels.x + 0.5,
                    cls.get_attributes().front_wheels.y,
                ),
                Car.Wheel(
                    "front",
                    cls.get_attributes().front_wheels.x - 0.5,
                    cls.get_attributes().front_wheels.y,
                ),
                Car.Wheel(
                    "rear",
                    -cls.get_attributes().rear_wheels.x + 0.5,
                    cls.get_attributes().rear_wheels.y,
                ),
                Car.Wheel(
                    "rear",
                    cls.get_attributes().rear_wheels.x - 0.5,
                    cls.get_attributes().rear_wheels.y,
                ),
            ]
        ]

    @classmethod
    def get_seats(cls):
        return [
            "summon interaction ~{} ~{} ~{} {}".format(
                seat.pos.x,
                seat.pos.y,
                seat.pos.z,
                {
                    "Tags": [
                        "+bubblevehicles",
                        "bbfh.seat",
                        "--bbfh.{}".format(
                            "driver" if seat.is_driver_seat else "passenger"
                        ),
                        "--bbfh.new",
                    ],
                    "width": 0.75,
                    "height": 1.5,
                    "response": True,
                    "Passengers": [
                        {
                            "id": "llama",
                            "Tags": [
                                "+bubblevehicles",
                                "bbfh.seat_entity",
                                "--bbfh.{}".format(
                                    "driver" if seat.is_driver_seat else "passenger"
                                ),
                                "--bbfh.new",
                            ],
                            "CustomName": quote(cls.__name__),
                            "NoGravity": True,
                            "Tame": True,
                            "Strength": 5,
                            "ChestedHorse": seat.is_driver_seat,
                            "Silent": True,
                            "Invulnerable": True,
                            "Age": -2147483648,
                            "NoAI": True,
                            "ActiveEffects": [
                                {
                                    "Id": 14,
                                    "Duration": -1,
                                    "ShowParticles": False,
                                }
                            ],
                            "PersistenceRequired": True,
                        }
                    ],
                },
            )
            for seat in cls.get_attributes().seats
        ]

    @classmethod
    def get_attributes(cls) -> CarAttributes:
        return cast(CarAttributes, cls.get_attr("attributes"))

    @classmethod
    def get_attribute_variables(cls):
        attr = cls.get_attributes()
        return [
            f"max_health {attr.base.max_health}",
            f"is_paintable {int(attr.base.is_paintable)}",
            f"max_speed {attr.max_speed}",
        ]


def get_headlight(pos: Point, rot: Point):
    return Item(
        "headlights",
        pos,
        rot,
        Point(0.75),
        "player_head",
        {"SkullOwner": PlayerHead.HEADLIGHTS_OFF.value},
    )


def get_rear_lights(pos: Point, rot: Point):
    return Item(
        "rear_light",
        pos,
        rot,
        Point(0.75),
        "player_head",
        {"SkullOwner": PlayerHead.REAR_LIGHTS_OFF.value},
    )


def get_siren(pos: Point):
    return Block(
        "siren",
        pos,
        None,
        Point(
            1.124,
            0.75,
            0.1,
        ),
        "redstone_lamp",
    )
