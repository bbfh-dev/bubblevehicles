ride @p[tag=--bbfh.this_player] dismount
execute unless score @s bbfh.is_locked matches 1 as @e[type=llama,tag=--bbfh.group,limit=1,sort=nearest] run function bubblevehicles:events/_clicked_seat/_start_riding/ride
execute if score @s bbfh.is_locked matches 1 run function bubblevehicles:events/_clicked_seat/_start_riding/check_ownership
