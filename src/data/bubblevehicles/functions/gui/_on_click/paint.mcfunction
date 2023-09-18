scoreboard players set paint_type bbfh.runtime 0

#> INSERT <vehicle paint jobs>

tag @s add --bbfh.this
execute if score paint_type bbfh.runtime matches 1 as @e[type=#bubblevehicles:vehicle_entity, tag=--bbfh.group,tag=--bbfh.primary] run data modify entity @s block_state.Name set from entity @p[tag=--bbfh.this] SelectedItem.id
execute if score paint_type bbfh.runtime matches 2 as @e[type=#bubblevehicles:vehicle_entity, tag=--bbfh.group,tag=--bbfh.stairs] run data modify entity @s block_state.Name set from entity @p[tag=--bbfh.this] SelectedItem.id
execute if score paint_type bbfh.runtime matches 3 as @e[type=#bubblevehicles:vehicle_entity, tag=--bbfh.group,tag=--bbfh.carpet] run data modify entity @s block_state.Name set from entity @p[tag=--bbfh.this] SelectedItem.id
tag @s remove --bbfh.this
