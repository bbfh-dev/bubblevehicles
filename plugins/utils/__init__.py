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


def find_and_replace_in_function(fn: Function, target: str, *replacements: str):
    fn.set_content(
        fn.get_content().replace(
            f"#> INSERT <{target}>",
            "\n".join(replacements)
        )
    )
