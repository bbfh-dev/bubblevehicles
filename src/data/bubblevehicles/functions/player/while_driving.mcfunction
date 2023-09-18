execute store success score gui.has_item bbfh.runtime run clear @s #bubblevehicles:gui_item{bbfh_gui: 1b} 0
execute if score gui.has_item bbfh.runtime matches 1 run function bubblevehicles:gui/on_click

execute if score @s bbfh.on_drop matches 1.. run function bubblevehicles:player/event/on_drop
