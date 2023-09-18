import os

from beet import Context, Function
from colorama import Fore

from plugins.utils import Log, find_and_replace_in_function


def run_pipeline(ctx: Context):
    """
    Finds all usages of "<int> bbfh.auto"
    and initializes used variables
    with the same value as their name
    as a workaround for scoreboard math
    """
    values = set()
    for path, fn in ctx.data.functions.items():
        for line in fn.get_content().split(os.linesep):
            substr = line.find(" bbfh.auto")
            if substr == -1:
                continue
            values.add(line[:substr].split(" ")[-1])
    find_and_replace_in_function(
        ctx.data.functions["bubblevehicles:load"],
        "bbfh.auto",
        "scoreboard objectives add bbfh.auto dummy",
        *[
            f"scoreboard players set {value} bbfh.auto {value}"
            for value in values
        ]
    )
    Log("AutoVars").info("Initialized", f"{len(values)} constants")
