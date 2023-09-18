execute unless score @e[type=armor_stand,tag=--bbfh.group,limit=1] bbfh.is_locked matches 1 run item replace entity @s horse.0 with bell{bbfh_item: 2, bbfh_gui: 1b, HideFlags:255, display:{Name:'{"text":"Lock", "color":"yellow", "italic":false}', Lore:['{"text":"Locked vehicles cannot be accessed", "color":"gray", "italic":false}', '{"text":"by any player other than the owner", "color":"gray", "italic":false}']}}
execute if score @e[type=armor_stand,tag=--bbfh.group,limit=1] bbfh.is_locked matches 1 run item replace entity @s horse.0 with bell{bbfh_item: 3, bbfh_gui: 1b, HideFlags:255, display:{Name:'{"text":"Unlock", "color":"yellow", "italic":false}', Lore:['{"text":"Unlocked vehicles can be accessed", "color":"gray", "italic":false}', '{"text":"by anyone", "color":"gray", "italic":false}']}}
item replace entity @s horse.1 with brush{bbfh_item: 4, bbfh_gui: 1b, HideFlags:255, display:{Name:'{"text":"Paint", "color":"yellow", "italic":false}', Lore:['{"text":"Hold a block in your mainhand", "color":"gray", "italic":false}', '{"text":"in order to apply that block to vehicle", "color":"gray", "italic":false}', '""', '{"text":"Available paint categories:", "color":"gold", "italic":false}', '{"text":"• Solid blocks — primary paint job", "color":"gray", "italic":false}', '{"text":"• Stairs/Half-blocks — secondary paint job", "color":"gray", "italic":false}', '{"text":"• Carpets — compliment paint job", "color":"gray", "italic":false}']}}
item replace entity @s horse.2 with name_tag{bbfh_item: 5, bbfh_gui: 1b, HideFlags:255, display:{Name:'{"text":"Change Nameplate", "color":"yellow", "italic":false}', Lore:['{"text":"Hold a ", "color":"gray", "italic":false, "extra":[{"translate":"item.minecraft.name_tag"}, " in your mainhand"]}', '{"text":"to set the nameplate of vehicle", "color":"gray", "italic":false}', '""', '{"text":"Must be less than 7 characters", "color":"red", "italic":false}']}}
item replace entity @s horse.3 with black_stained_glass_pane{bbfh_item: -1, bbfh_gui: 1b, HideFlags:255, display:{Name:'""'}}
item replace entity @s horse.4 with black_stained_glass_pane{bbfh_item: -1, bbfh_gui: 1b, HideFlags:255, display:{Name:'""'}}
item replace entity @s horse.5 with air
item replace entity @s horse.6 with air
item replace entity @s horse.7 with air
item replace entity @s horse.8 with black_stained_glass_pane{bbfh_item: -1, bbfh_gui: 1b, HideFlags:255, display:{Name:'""'}}
item replace entity @s horse.9 with black_stained_glass_pane{bbfh_item: -1, bbfh_gui: 1b, HideFlags:255, display:{Name:'""'}}
item replace entity @s horse.10 with air
item replace entity @s horse.11 with air
item replace entity @s horse.12 with air
item replace entity @s horse.13 with black_stained_glass_pane{bbfh_item: -1, bbfh_gui: 1b, HideFlags:255, display:{Name:'""'}}
item replace entity @s horse.14 with chest{bbfh_item: 0, bbfh_gui: 1b, HideFlags:255, display:{Name:'{"text":"Open Glovebox", "color":"yellow", "italic":false}'}}
execute store result score glovebox_size bbfh.runtime run data get entity @e[type=armor_stand,tag=--bbfh.group,limit=1] ArmorItems[0].tag.bbfh_items
scoreboard players remove glovebox_size bbfh.runtime 6
scoreboard players operation glovebox_size bbfh.runtime > 0 bbfh.auto
item modify entity @s horse.14 bubblevehicles:gui/set_glovebox_size
