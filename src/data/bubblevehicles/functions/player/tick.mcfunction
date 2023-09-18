tag @s add --bbfh.this_player

execute if predicate bubblevehicles:is_driving run function bubblevehicles:player/while_driving
execute as @s[tag=--bbfh.riding_a_vehicle] unless predicate bubblevehicles:is_driving run function bubblevehicles:events/stopped_riding

tag @s remove --bbfh.this_player
