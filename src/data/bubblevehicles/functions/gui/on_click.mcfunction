function bubblevehicles:registry/determine_group
execute if score @e[type=llama,tag=--bbfh.group,limit=1,sort=nearest] bbfh.is_glovebox_open matches 1 run data modify entity @e[type=armor_stand,tag=--bbfh.group,limit=1] ArmorItems[0].tag.bbfh_items set from entity @e[type=llama,tag=--bbfh.group,limit=1,sort=nearest] Items

execute store success score check bbfh.runtime run clear @s #bubblevehicles:gui_item{bbfh_gui: 1b, bbfh_item:0} 0
execute if score check bbfh.runtime matches 1 run scoreboard players set @e[type=llama,tag=--bbfh.group,limit=1,sort=nearest] bbfh.is_glovebox_open 1

execute store success score check bbfh.runtime run clear @s #bubblevehicles:gui_item{bbfh_gui: 1b, bbfh_item:1} 0
execute if score check bbfh.runtime matches 1 run function bubblevehicles:gui/_on_click/close_glovebox

execute store success score check bbfh.runtime run clear @s #bubblevehicles:gui_item{bbfh_gui: 1b, bbfh_item:2} 0
execute if score check bbfh.runtime matches 1 run scoreboard players set @e[type=armor_stand,tag=--bbfh.group,limit=1,sort=nearest] bbfh.is_locked 1

execute store success score check bbfh.runtime run clear @s #bubblevehicles:gui_item{bbfh_gui: 1b, bbfh_item:3} 0
execute if score check bbfh.runtime matches 1 run scoreboard players set @e[type=armor_stand,tag=--bbfh.group,limit=1,sort=nearest] bbfh.is_locked 0

execute store success score check bbfh.runtime run clear @s #bubblevehicles:gui_item{bbfh_gui: 1b, bbfh_item:4} 0
execute if score check bbfh.runtime matches 1 unless data entity @s SelectedItem.id run tellraw @s {"text":"You must hold a block in your mainhand", "color":"red"}
execute if score check bbfh.runtime matches 1 if data entity @s SelectedItem.id run function bubblevehicles:gui/_on_click/paint

execute store success score check bbfh.runtime run clear @s #bubblevehicles:gui_item{bbfh_gui: 1b, bbfh_item:5} 0
execute if score check bbfh.runtime matches 1 unless data entity @s SelectedItem{id:"minecraft:name_tag"}.tag.display.Name run tellraw @s {"text":"You must hold a renamed ", "color":"red", "extra":[{"translate":"item.minecraft.name_tag"}, " in your mainhand"]}
execute if score check bbfh.runtime matches 1 if data entity @s SelectedItem{id:"minecraft:name_tag"}.tag.display.Name run function bubblevehicles:gui/_on_click/change_nameplate

execute as @e[type=llama,tag=--bbfh.group] run function bubblevehicles:gui/setup
clear @s #bubblevehicles:gui_item{bbfh_gui: 1b}
playsound ui.button.click master @s ~ ~ ~ 1 1 0
