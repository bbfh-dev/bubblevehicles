from beet import Function

from .log import Log
from ..bubblevehicles.vehicles.structs import NBTByte, NBTDouble, NBTLong, NBTRaw


def as_function(*lines: str) -> Function:
    """
    Combine lines into a function
    """
    return Function(
        "\n".join(
            ["#! ⚠️ This code is generated. See project's source code!", *lines, ""]
        )
    )


def quote(string: str):
    """
    Surrounds provided string with quotation marks
    """
    if '"' in string:
        return "'{}'".format(string)
    return '"{}"'.format(string)


def get_nbt_value(
    nbt: list | tuple | dict | str | int | float | bool | NBTDouble | NBTByte | NBTLong,
):
    if type(nbt) in [list, tuple]:
        return "[" + ", ".join([get_nbt_value(i) for i in nbt]) + "]"

    if type(nbt) is dict:
        return as_nbt_string(nbt)

    if type(nbt) is float:
        return "{}f".format(nbt)

    if type(nbt) is bool:
        return "{}b".format(int(nbt))

    if type(nbt) is str:
        return quote(nbt)

    if type(nbt) is NBTDouble:
        return "{}d".format(nbt.value)

    if type(nbt) is NBTByte:
        return "{}b".format(nbt.value)

    if type(nbt) is NBTLong:
        return "{}L".format(nbt.value)

    if type(nbt) is NBTRaw:
        return nbt.value

    return str(nbt)


def as_nbt_string(nbt: dict) -> str:
    result = []
    for key, value in nbt.items():
        result.append(f"{key}: {get_nbt_value(value)}")
    return "{" + ", ".join(result) + "}"
