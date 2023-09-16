from .__model__ import Car, CarAttributes, get_headlight, get_rear_lights, get_siren
from ..model import Model
from ..structs import Axis, BoxSize, Material, Point
from ..unit import Block, fill, mirror
from ..vehicle import BaseAttributes


class Pineda(Car):
    hitbox = BoxSize(x=4, y=1.0)
    attributes = CarAttributes(
        BaseAttributes(health=105, is_paintable=False),
        max_speed=100,
        front_wheels=BoxSize(x=1.4, y=1.25),
        rear_wheels=BoxSize(x=1.4, y=-1.5),
        seats=[
            Car.Seat(True, Point(0.8 - 1.5 / 16, 0.375, -0.5)),
            Car.Seat(False, Point(-0.8 + 1.5 / 16, 0.375, -0.5)),
            Car.Seat(False, Point(0.8 - 1.5 / 16, -0.75, -0.5)),
            Car.Seat(False, Point(0, -0.75, -0.5)),
            Car.Seat(False, Point(-0.8 + 1.5 / 16, -0.75, -0.5)),
        ],
    )
    model = Model(
        units=[
            # Hood:
            *fill(
                Block(None, None, None, Point(0.75), Material.PRIMARY__PD),
                Point(-1, 1.5, 0.5),
                Point(1, 2.5, 0.5),
            ),
            # Boot:
            *fill(
                Block(None, None, None, Point(0.75), Material.PRIMARY__PD),
                Point(-1, -2.5, 0.5),
                Point(1, -2.5, 0.5),
            ),
            # Windshield:
            *fill(
                Block(
                    None,
                    None,
                    Point(-20, 0, 0),
                    Point(0.75),
                    "glass_pane",
                    {
                        "east": "true",
                        "west": "true",
                    },
                ),
                Point(-0.999, 1.35, 1.35),
                Point(0.999, 1.35, 1.35),
            ),
            # Door:
            *mirror(
                *fill(
                    Block(
                        None, None, Point(0, 90, 0), Point(0.75), Material.CARPET__PD
                    ),
                    Point(-1 + 1 / 16, -1.5, 0.5),
                    Point(-1 + 1 / 16, 0.5, 0.5),
                ),
                axis=Axis.X,
                offset=Point(1 + 1 / 16, 0, 0),
            ),
            # Side:
            *mirror(
                *fill(
                    Block(
                        None, None, Point(0, 90, 0), Point(0.75), Material.CARPET__PD
                    ),
                    Point(-1.001 + 1 / 16, -0.5, 1.5),
                    Point(-1.001 + 1 / 16, 0, 1.5),
                ),
                axis=Axis.X,
                offset=Point(1 + 1 / 16, 0, 0),
            ),
            # Floor:
            *fill(
                Block(None, None, None, Point(0.75), Material.CARPET__PD2),
                Point(-1, -2.5, 0.5 - 1 / 16),
                Point(1, 2.5, 0.5 - 1 / 16),
            ),
            # Ceiling:
            *fill(
                Block(None, None, None, Point(0.75), Material.CARPET__PD),
                Point(-1, -1.498, 2.5 - 1 / 16),
                Point(1, 0.5, 2.5 - 1 / 16),
            ),
            # Iron Bars:
            *fill(
                Block(
                    None,
                    None,
                    None,
                    Point(0.75),
                    "iron_bars",
                    {
                        "east": "true",
                        "west": "true",
                    },
                ),
                Point(-1, -0.5 + 1 / 16, 1.499),
                Point(1, -0.5 + 1 / 16, 1.499),
            ),
            *fill(
                Block(
                    None,
                    None,
                    None,
                    Point(0.75),
                    "black_stained_glass_pane",
                    {
                        "east": "true",
                        "west": "true",
                    },
                ),
                Point(-0.999, -1.999 + 1 / 16, 1.499),
                Point(0.999, -1.999 + 1 / 16, 1.499),
            ),
            Block(
                None,
                Point(0, -0.5 + 1 / 16, 0.499),
                None,
                Point(0.75),
                "iron_bars",
                {
                    "east": "true",
                    "west": "true",
                },
            ),
            *mirror(
                Block(
                    None,
                    Point(1.5 - 1 / 16, -1.5, 1.499),
                    None,
                    Point(0.75),
                    "iron_bars",
                    {
                        "north": "true",
                        "south": "true",
                    },
                ),
                axis=Axis.X,
                offset=Point(0),
            ),
            # Steering wheel:
            Block(
                None,
                Point(1 + 6 / 16, 2.3, 0.82),
                Point(-70, 0, 0),
                Point(0.5),
                "lightning_rod",
            ),
            Block(
                None,
                Point(1 + 6 / 16, 1.55, 1.09),
                Point(-70, 0, 0),
                Point(0.5),
                "mangrove_trapdoor",
            ),
            # Grille:
            *mirror(
                Block(
                    None,
                    Point(0.5, 4.55, 0.25),
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
                    Point(1 - 1 / 16, 0, 0.5),
                    Point(0),
                    Point(0.75),
                    Material.STAIRS,
                ),
                axis=Axis.X,
                offset=Point(0),
            ),
            *fill(
                Block(
                    None,
                    None,
                    Point(0),
                    Point(0.75),
                    Material.STAIRS,
                ),
                Point(-0.999, -1.5, 0.5),
                Point(0.999, -1.5, 0.5),
            ),
            # Common parts:
            *mirror(
                get_headlight(Point(1.6, 3.3, 1.4), Point(0, 0, 180)),
                axis=Axis.X,
                offset=Point(1, 0, 0),
            ),
            *mirror(
                get_rear_lights(Point(1.4, -2.325, 1.375), Point(-15, 0, 0)),
                axis=Axis.X,
                offset=Point(1, 0, 0),
            ),
            *mirror(
                get_siren(Point(0.5, -0.5, 12.2)),
                axis=Axis.X,
                offset=Point(0),
            ),
        ],
        offset=Point(0),
    )
