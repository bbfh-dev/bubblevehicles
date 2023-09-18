# give --bbfh.group tag to all entities with the same bbfh.id

tag @s add --bbfh.this
tag @e[type=#bubblevehicles:vehicle_entity] remove --bbfh.group
execute as @e[type=#bubblevehicles:vehicle_entity] if score @s bbfh.id = @e[type=#bubblevehicles:vehicle_entity,tag=--bbfh.this,limit=1] bbfh.id run tag @s add --bbfh.group
tag @s remove --bbfh.this
