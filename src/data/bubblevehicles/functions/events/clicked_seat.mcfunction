# from minecraft:bubblevehicles/events/clicked_seat

function bubblevehicles:registry/determine_group

scoreboard players set this.check bbfh.runtime 0
tag @e[type=llama,tag=--bbfh.group,limit=1,sort=nearest] add --bbfh.filtered
execute as @a if predicate bubblevehicles:is_riding_group_entity run scoreboard players set this.check bbfh.runtime 1

execute if score this.check bbfh.runtime matches 0 at @s as @e[type=armor_stand,tag=--bbfh.group,limit=1] run function bubblevehicles:events/_clicked_seat/start_riding
tag @e[type=llama] remove --bbfh.filtered
