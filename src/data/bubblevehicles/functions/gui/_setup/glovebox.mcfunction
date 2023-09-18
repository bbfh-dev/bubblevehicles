# Restore glovebox
setblock 0 -64 0 yellow_shulker_box
data remove entity @e[type=armor_stand,tag=--bbfh.group,limit=1] ArmorItems[0].tag.bbfh_items[{tag:{bbfh_gui: 1b}}]
data modify block 0 -64 0 Items set from entity @e[type=armor_stand,tag=--bbfh.group,limit=1] ArmorItems[0].tag.bbfh_items

item replace entity @s horse.0 from block 0 -64 0 container.2
item replace entity @s horse.1 from block 0 -64 0 container.3
item replace entity @s horse.2 from block 0 -64 0 container.4
item replace entity @s horse.3 with black_stained_glass_pane{bbfh_item: -1, bbfh_gui: 1b, HideFlags:255, display:{Name:'""'}}
item replace entity @s horse.4 with black_stained_glass_pane{bbfh_item: -1, bbfh_gui: 1b, HideFlags:255, display:{Name:'""'}}
item replace entity @s horse.5 from block 0 -64 0 container.7
item replace entity @s horse.6 from block 0 -64 0 container.8
item replace entity @s horse.7 from block 0 -64 0 container.9
item replace entity @s horse.8 with black_stained_glass_pane{bbfh_item: -1, bbfh_gui: 1b, HideFlags:255, display:{Name:'""'}}
item replace entity @s horse.9 with black_stained_glass_pane{bbfh_item: -1, bbfh_gui: 1b, HideFlags:255, display:{Name:'""'}}
item replace entity @s horse.10 from block 0 -64 0 container.12
item replace entity @s horse.11 from block 0 -64 0 container.13
item replace entity @s horse.12 from block 0 -64 0 container.14
item replace entity @s horse.13 with black_stained_glass_pane{bbfh_item: -1, bbfh_gui: 1b, HideFlags:255, display:{Name:'""'}}
item replace entity @s horse.14 with ender_chest{bbfh_item: 1, bbfh_gui: 1b, HideFlags:255, display:{Name:'{"text":"Close Glovebox", "color":"yellow", "italic":false}'}}
