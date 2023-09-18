advancement revoke @s only bubblevehicles:events/clicked_seat
tag @s add --bbfh.this_player
execute anchored eyes positioned ^ ^ ^1.5 as @e[type=interaction,tag=bbfh.seat,limit=1,sort=nearest] run function bubblevehicles:events/clicked_seat
tag @s remove --bbfh.this_player
