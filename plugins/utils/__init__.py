from .log import Log
from beet import Function


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
