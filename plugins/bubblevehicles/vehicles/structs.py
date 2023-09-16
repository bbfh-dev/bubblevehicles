from dataclasses import dataclass
from enum import Enum
from typing import cast

from scipy.spatial.transform import Rotation

VEC = tuple[float, float, float]
ROT = tuple[float, float, float, float]


def get(var, otherwise):
    return otherwise if var is None else var


class Point:
    def __init__(self, x: float, z: float = None, y: float = None):
        self._x = x
        self._y: float = get(y, x)
        self._z: float = get(z, x)

    def __str__(self):
        return "<x:{} y:{} z:{}>".format(self._x, self._y, self._z)

    def __repr__(self):
        return self.__str__()

    def as_vec(self) -> VEC:
        return float(self._x), float(self._y), float(self._z)

    def as_rot(self, _x: float = None, _z: float = None, _y: float = None) -> ROT:
        x = get(_x, self._x)
        y = get(_y, self._y)
        z = get(_z, self._z)
        return cast(
            ROT,
            tuple(
                [
                    float(round(i, 3))
                    for i in Rotation.from_rotvec([x, z, y], degrees=True).as_quat(
                        False
                    )
                ]
            ),
        )

    @property
    def left_rotation(self):
        if self.x != 0:
            return self.as_rot(self.x, 0, 0)
        if self.y != 0:
            return self.as_rot(0, self.y, 0)
        if self.z != 0:
            return self.as_rot(0, 0, self.z)
        return self.as_rot()

    @property
    def right_rotation(self):
        if self.left_rotation[0] != 0:
            return self.as_rot(0, self.y, self.z)
        if self.left_rotation[1] != 0:
            return self.as_rot(self.x, 0, self.z)
        if self.left_rotation[2] != 0:
            return self.as_rot(self.x, self.y, 0)
        return Point(0).as_rot()

    @property
    def x(self):
        return self.as_vec()[0]

    @property
    def y(self):
        return self.as_vec()[1]

    @property
    def z(self):
        return self.as_vec()[2]

    @property
    def center_x(self):
        return self.x - 0.5

    @property
    def center_y(self):
        return self.y - 1

    @property
    def center_z(self):
        return self.z - 0.5


@dataclass
class BoxSize:
    x: float
    y: float


@dataclass
class NBTDouble:
    value: float


@dataclass
class NBTByte:
    value: int


@dataclass
class NBTLong:
    value: int


@dataclass
class NBTRaw:
    value: str


class Material(Enum):
    PRIMARY = "yellow_terracotta"
    PRIMARY__PD = "black_concrete"
    SLAB = "dark_oak_slab"
    CARPET = "brown_carpet"
    CARPET__PD = "white_carpet"
    CARPET__PD2 = "black_carpet"
    TRAPDOOR = "dark_oak_trapdoor"
    STAIRS = "dark_oak_stairs"
    STEERING_BASE = "lightning_rod"
    STEERING_WHEEL = "mangrove_trapdoor"


class PlayerHead(Enum):
    WHEEL = NBTRaw(
        '{Id:[I;-1620253083,1948861092,-1515577044,1369749555],Properties:{textures:[{Value:"eyJ0ZXh0dXJlcy'
        "I6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvZGRmZTVhOTYzODY5NDE1MzQw"
        'ZDJjZWMwZjgyZDA4ZGY3M2RjYjE2ODQyODQ4N2I1MTRhYThkNGVjMTlmZTJjIn19fQ=="}]}}'
    )
    HEADLIGHTS_OFF = NBTRaw(
        '{Id:[I;1761756027,-337097798,-1247026872,-1023879146],Properties:{textures:[{Value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvMzk4ZmZiMGYwMTAxZjExYzUxN2Q0OTgxOTAwZmM2YjU0YWM5OGZkZTBkOTBiZGVkMzQ3N2Y0YjZkNTJhZjg4NyJ9fX0="}]}}'
    )
    REAR_LIGHTS_OFF = NBTRaw(
        '{Id:[I;-711908062,-2090844072,-1258282898,-2075414609],Properties:{textures:[{Value:"eyJ'
        "0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvZGU"
        "1YTJkMjBjOGVlNTZjZmM3N2I0NTU2NWNjODdhNzU4Yjg4MTY3NTBkNTM3ZmY2ZDExMTZkZmYyYzA4MTQxIn19fQ="
        '="}]}}'
    )
    SIRENS_OFF = NBTRaw("{}")


class Axis(Enum):
    X = 0
    Z = 1
    Y = 2
