execute store result score length bbfh.runtime run data get entity @s SelectedItem.tag.display.Name
scoreboard players remove length bbfh.runtime 11
execute unless score length bbfh.runtime matches ..6 run tellraw @s {"text":"The length must be below 7 characters in length", "color":"red"}
execute if score length bbfh.runtime matches ..6 run function bubblevehicles:gui/_on_click/_change_nameplate/run
