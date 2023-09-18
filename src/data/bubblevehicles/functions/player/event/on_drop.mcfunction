execute store result score dropped_gui_item bbfh.runtime run kill @e[type=item,nbt={Item:{tag:{bbfh_gui:1b}}}]
execute if score dropped_gui_item bbfh.runtime matches 1 run function bubblevehicles:gui/setup_as_player
