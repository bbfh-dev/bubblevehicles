from beet import Context

from plugins.utils import Log, as_function
from .vehicles.car import Car, Rofi
from .vehicles.car.pineda import Pineda
from .vehicles.nbt import as_nbt_string
from .vehicles.vehicle import BaseVehicle

REGISTRY = [Rofi, Pineda]


class Pipeline:
    def __init__(self, ctx: Context, vehicle: type[Car]):
        self.ctx = ctx
        self.vehicle = vehicle

    def insert_summon(self):
        self.ctx.data.functions[
            f"summon:bubblevehicles/{self.vehicle.get_origin()}/{self.vehicle.__name__}".lower()
        ] = as_function(
            "summon armor_stand ~ ~ ~ {}".format(as_nbt_string(self.vehicle.as_dict())),
            *self.vehicle.get_wheels(),
            *self.vehicle.get_seats(),
            *[
                "scoreboard players set @e[type=armor_stand,tag=bbfh.origin,tag=--bbfh.new] --bbfh.{}".format(
                    i
                )
                for i in self.vehicle.get_attribute_variables()
            ],
            "team join bubblevehicles @e[tag=--bbfh.new]",
            "function bubblevehicles:registry/set_entry",
        )
        return self


def run_pipeline(ctx: Context):
    for vehicle in REGISTRY:
        Log("BubbleVehicles").info(
            "Added", f"{vehicle.get_origin()}/{vehicle.__name__}"
        )
        (Pipeline(ctx, vehicle).insert_summon())
