data modify entity @e[type=text_display,tag=--bbfh.group,limit=1] text set from entity @s SelectedItem.tag.display.Name
playsound entity.player.levelup master @s ~ ~ ~ 1 1 0
tellraw @s {"text":"Changed the nameplate to \"", "extra":[{"nbt":"SelectedItem.tag.display.Name", "entity":"@s", "interpret":true}, "\""], "color":"green"}
