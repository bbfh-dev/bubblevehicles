from copy import copy

from .structs import Axis, Material, NBTByte, Point, get
from ...utils import quote


class Unit:
    def __init__(self, name: str, pos: Point | None, rot: Point | None, scale: Point):
        self.name = name
        self.pos: Point = get(pos, Point(0))
        self.rot: Point = get(rot, Point(0))
        self.scale = scale

    def __str__(self):
        return f"<{self.name} at {'x: {}, z: {}, y: {}'.format(*self.pos.as_vec())}>"

    def __repr__(self):
        return self.__str__()

    def as_dict(self, *args, **kwargs) -> dict:
        pass

    def move(self, new_pos: Point):
        """
        Creates a new copy of the unit
        with a different position
        :return: Modified copy
        """
        buffered = self.pos
        self.pos = new_pos
        new_unit = copy(self)
        self.pos = buffered
        return new_unit

    def get_scaled_pos(self, offset: Point):
        """
        :return: Position scaled and offset accordingly
        """
        return Point(
            self.pos.center_x * self.scale.x + offset.x,
            self.pos.center_z * self.scale.z + offset.z,
            self.pos.center_y * self.scale.y + offset.y,
        )


class DisplayEntity(Unit):
    def __init__(
        self,
        name: str | None,
        pos: Point | None,
        rot: Point | None,
        scale: Point,
        material: Material | str,
        full_bright: bool = False,
    ):
        self.material = material
        self.full_bright = full_bright
        super().__init__(get(name, self.get_name()), pos, rot, scale)

    def get_brightness(self):
        """
        :return: Dictionary used for setting brightness of a display entity
        """
        if self.full_bright:
            return {"brightness": {"sky": 15, "block": 15}}
        return {}

    def as_partial_dict(self):
        """
        Used for inserting class-specific data
        """
        pass

    def get_name(self):
        if type(self.material) is Material:
            return self.material.name.split("__")[0]
        return "generic"

    def get_value(self):
        if type(self.material) is Material:
            return self.material.value
        return self.material

    def as_dict(self, width: float, height: float, offset: Point) -> dict:
        return {
            **self.as_partial_dict(),
            **self.get_brightness(),
            "Tags": [
                "+bubblevehicles",
                "bbfh.unit",
                f"--bbfh.{self.name.lower()}",
                "--bbfh.new",
            ],
            "width": width,
            "height": height,
            "transformation": {
                "left_rotation": self.rot.left_rotation,
                "right_rotation": self.rot.right_rotation,
                "translation": self.get_scaled_pos(offset).as_vec(),
                "scale": self.scale.as_vec(),
            },
        }


class Block(DisplayEntity):
    def __init__(
        self,
        name: str | None,
        pos: Point | None,
        rot: Point | None,
        scale: Point,
        material: Material | str,
        properties: dict = None,
        full_bright: bool = False,
    ):
        self.properties = get(properties, {})
        super().__init__(name, pos, rot, scale, material, full_bright)

    def as_partial_dict(self):
        return {
            "id": "block_display",
            "block_state": {"Name": self.get_value(), "Properties": self.properties},
        }


class Item(DisplayEntity):
    def __init__(
        self,
        name: str | None,
        pos: Point | None,
        rot: Point | None,
        scale: Point,
        material: str,
        tag: dict = None,
    ):
        self.tag = get(tag, {})
        super().__init__(name, pos, rot, scale, material)

    def as_partial_dict(self):
        return {
            "id": "item_display",
            "item": {"id": self.get_value(), "Count": NBTByte(1), "tag": self.tag},
        }


class Text(DisplayEntity):
    def __init__(
        self,
        name: str | None,
        pos: Point | None,
        rot: Point | None,
        scale: Point,
        material: str,
    ):
        super().__init__(name, pos, rot, scale, material)

    def as_partial_dict(self):
        return {
            "id": "text_display",
            "text": quote(self.get_value()),
            "background": 0,
            "shadow": True,
        }


def fill(unit: Unit, point1: Point, point2: Point, distance: float = 1.0):
    """
    'Fills' the area using the provided unit.
    Inclusive in both boundaries.
    :return: Array of units in the specified area
    """
    result = []
    for x in range(abs(round(point2.x - point1.x)) + 1):
        for z in range(abs(round(point2.z - point1.z)) + 1):
            for y in range(abs(round(point2.y - point1.y)) + 1):
                result.append(
                    unit.move(
                        Point(
                            min(point1.x + x * distance, point2.x),
                            min(point1.z + z * distance, point2.z),
                            min(point1.y + y * distance, point2.y),
                        )
                    )
                )
    return result


def mirror(*units: Unit, axis: Axis, offset: Point) -> list[Unit]:
    """
    Mirrors units along an axis.
    :return: both original and mirrored units
    """

    def mirror_attr(attr: Point):
        """
        Used to ensure no code repeatition in the future
        in-case there will be a need for mirroring other attributes (preferably)
        """
        return Point(
            attr.x * -1 + offset.x if axis is Axis.X else attr.x,
            attr.z * -1 + offset.z if axis is Axis.Z else attr.z,
            attr.y * -1 + offset.y if axis is Axis.Y else attr.y,
        )

    return [
        *units,
        *[unit.move(mirror_attr(unit.pos)) for unit in units],
    ]
