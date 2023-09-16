import os

from beet import Context, Function
from colorama import Fore


def run(ctx: Context):
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
    fn: Function = ctx.data.functions["bubblevehicles:load"]
    fn.set_content(
        fn.get_content().replace(
            "#> INSERT <bbfh.auto>",
            "scoreboard objectives add bbfh.auto dummy\n"
            + "\n".join(
                [
                    f"scoreboard players set {value} bbfh.auto {value}"
                    for value in values
                ]
            ),
        )
    )
    print(
        f"{Fore.LIGHTBLACK_EX}PLUGIN/{Fore.RESET}AutoVars "
        f"{Fore.LIGHTBLACK_EX}:: "
        f"Initialized {len(values)} used constants{Fore.RESET}"
    )
