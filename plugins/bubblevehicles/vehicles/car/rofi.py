from .__model__ import Car, CarAttributes, get_headlight, get_rear_lights
from ..model import Model
from ..structs import Axis, BoxSize, Material, Point
from ..unit import Block, Text, fill, mirror
from ..vehicle import BaseAttributes


class Rofi(Car):
    hitbox = BoxSize(x=3.0, y=1.0)
    attributes = CarAttributes(
        BaseAttributes(health=100, is_paintable=True),
        max_speed=100,
        front_wheels=BoxSize(x=1.4, y=2),
        rear_wheels=BoxSize(x=1.4, y=-1.25),
        seats=[
            Car.Seat(True, Point(0.8 - 3 / 16, 0.25, -0.5)),
            Car.Seat(False, Point(-0.8 + 3 / 16, 0.25, -0.5)),
        ],
    )
    model = Model(
        units=[
            # Boot:
            *fill(
                Block(None, None, None, Point(0.75), Material.PRIMARY),
                Point(-1, -2.5, 0.5),
                Point(1, -1.5, 0.5),
            ),
            *fill(
                Block(None, None, Point(-30, 0, 0), Point(0.75), Material.PRIMARY),
                Point(-0.999, -1.075, 0.5),
                Point(0.999, -1.075, 0.5),
            ),
            # Hood:
            *fill(
                Block(None, None, None, Point(0.75), Material.PRIMARY),
                Point(-1, 1.5, 0.5),
                Point(1, 3.5, 0.5),
            ),
            # Door:
            *mirror(
                *fill(
                    Block(None, None, Point(0, 90, 0), Point(0.75), Material.TRAPDOOR),
                    Point(-1 + 3 / 16, -0.5, 0.5),
                    Point(-1 + 3 / 16, 0.5, 0.5),
                ),
                axis=Axis.X,
                offset=Point(1 + 3 / 16, 0, 0),
            ),
            # Floor:
            *fill(
                Block(None, None, None, Point(0.75), Material.CARPET),
                Point(-1, -2.5, 0.5 - 1 / 16),
                Point(1, 3.5, 0.5 - 1 / 16),
            ),
            # Windshield:
            Block(
                None,
                Point(0.719, 1.67, 1.325),
                Point(-20, 0, 30),
                Point(0.75),
                "glass_pane",
                {
                    "east": "true",
                    "west": "true",
                },
            ),
            Block(
                None,
                Point(0, 1.6, 1.3),
                Point(-20, 0, 0),
                Point(0.75),
                "glass_pane",
                {
                    "east": "true",
                    "west": "true",
                },
            ),
            Block(
                None,
                Point(-0.584, 1.203, 1.15),
                Point(-20, 0, -30),
                Point(0.75),
                "glass_pane",
                {
                    "east": "true",
                    "west": "true",
                },
            ),
            # Grille:
            *mirror(
                Block(
                    None,
                    Point(0.5, 6.15, 0.25),
                    Point(10, 0, 0),
                    Point(0.5),
                    "dark_oak_fence",
                    {
                        "east": "true",
                        "west": "true",
                    },
                ),
                axis=Axis.X,
                offset=Point(0),
            ),
            # Seats:
            *mirror(
                Block(
                    None,
                    Point(1 - 3 / 16, -0.5, 0.5),
                    Point(0),
                    Point(0.75),
                    Material.STAIRS,
                ),
                axis=Axis.X,
                offset=Point(0),
            ),
            # Glovebox:
            Block(
                None,
                Point(-1 + 3 / 16, 1.6, 0.5),
                Point(-10, 0, 0),
                Point(0.75, 0.66, 0.5),
                "loom",
            ),
            # Handbrake:
            Block(
                None,
                Point(0, -0.25, 1.5),
                Point(90, 0, 0),
                Point(0.75),
                "lever",
            ),
            # Steering wheel:
            Block(
                None,
                Point(1 + 3 / 16, 2.3, 0.82),
                Point(-70, 0, 0),
                Point(0.5),
                "lightning_rod",
            ),
            Block(
                None,
                Point(1 + 3 / 16, 1.55, 1.09),
                Point(-70, 0, 0),
                Point(0.5),
                "mangrove_trapdoor",
            ),
            # License plate
            Block(
                None,
                Point(0, -3.479, 0.4),
                Point(10, 0, 0),
                Point(0.75),
                "birch_wall_sign",
                {
                    "facing": "north",
                },
            ),
            # Common parts:
            *mirror(
                get_headlight(Point(1.8, 4.3, 1.4), Point(0, 0, 180)),
                axis=Axis.X,
                offset=Point(1, 0, 0),
            ),
            *mirror(
                get_rear_lights(Point(1.4, -2.325, 1.375), Point(-15, 0, 0)),
                axis=Axis.X,
                offset=Point(1, 0, 0),
            ),
            # License plate:
            Text(None, Point(0.5, -2.56, 0.51), Point(10, 0, 180), Point(0.75), "ROFI"),
        ],
        offset=Point(0),
    )
