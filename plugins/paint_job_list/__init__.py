from beet import Context

from plugins.utils import Log, find_and_replace_in_function

COLORS = [
    "white",
    "orange",
    "magenta",
    "light_blue",
    "yellow",
    "lime",
    "pink",
    "gray",
    "light_gray",
    "cyan",
    "purple",
    "blue",
    "brown",
    "green",
    "red",
    "black",
]

WOODS = [
    "oak",
    "spruce",
    "birch",
    "acacia",
    "jungle",
    "dark_oak",
    "crimson",
    "warped",
    "mangrove",
    "bamboo",
    "cherry",
]

STAIRS_AND_SLABS = [
    "oak",
    "spruce",
    "birch",
    "jungle",
    "acacia",
    "dark_oak",
    "crimson",
    "warped",
    "mangrove",
    "bamboo",
    "cherry",
    "bamboo_mosaic",
    "cobblestone",
    "sandstone",
    "nether_brick",
    "stone_brick",
    "brick",
    "purpur",
    "quartz",
    "red_sandstone",
    "prismarine_brick",
    "prismarine",
    "dark_prismarine",
    "polished_granite",
    "smooth_red_sandstone",
    "mossy_stone_brick",
    "polished_diorite",
    "mossy_cobblestone",
    "end_stone_brick",
    "stone",
    "smooth_sandstone",
    "smooth_quartz",
    "granite",
    "andesite",
    "red_nether_brick",
    "polished_andesite",
    "diorite",
    "blackstone",
    "polished_blackstone_brick",
    "polished_blackstone",
    "cobbled_deepslate",
    "polished_deepslate",
    "deepslate_tile",
    "deepslate_brick",
    "oxidized_cut_copper",
    "weathered_cut_copper",
    "exposed_cut_copper",
    "cut_copper",
    "waxed_weathered_cut_copper",
    "waxed_exposed_cut_copper",
    "waxed_cut_copper",
    "waxed_oxidized_cut_copper",
    "mud_brick",
]


def get_materials(palette: list[str], name: str):
    return [f"{material}_{name}" for material in palette]


def print_category(index: int, *materials):
    return [
        (
            'execute if data entity @s SelectedItem{id:"minecraft:'
            + material
            + '"} run '
            "scoreboard players set paint_type bbfh.runtime " + str(index)
        )
        for material in materials
    ] + [""]


def run_pipeline(ctx: Context):
    """
    Inserts all paint jobs that are available
    """
    find_and_replace_in_function(
        ctx.data.functions["bubblevehicles:gui/_on_click/paint"],
        "vehicle paint jobs",
        *print_category(
            1,
            *get_materials(COLORS, "concrete"),
            *get_materials(COLORS, "glazed_terracotta"),
            *get_materials(COLORS, "terracotta"),
            *get_materials(COLORS, "wool"),
            *get_materials(WOODS, "wood"),
            *get_materials(WOODS, "planks"),
        ),
        *print_category(
            2,
            *get_materials(STAIRS_AND_SLABS, "stairs"),
            *get_materials(STAIRS_AND_SLABS, "slab"),
        ),
        *print_category(
            3,
            *get_materials([*COLORS, "mossb"], "carpet"),
        ),
    )
    Log("PaintJobList").info("Initialized", "")
