advancement revoke @s only bubblevehicles:events/started_riding
tag @s add --bbfh.this_player
execute as @e[type=llama,tag=bbfh.seat_entity,limit=1,sort=nearest] run function bubblevehicles:events/started_riding
tag @s remove --bbfh.this_player
