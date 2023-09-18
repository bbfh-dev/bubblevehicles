function bubblevehicles:registry/determine_group

execute unless score @s bbfh.is_glovebox_open matches 1 run function bubblevehicles:gui/_setup/menu
execute if score @s bbfh.is_glovebox_open matches 1 run function bubblevehicles:gui/_setup/glovebox
