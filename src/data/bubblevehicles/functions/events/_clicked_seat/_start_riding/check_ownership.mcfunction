execute if score @p[tag=--bbfh.this_player] bbfh.id = @s bbfh.owner as @e[type=llama,tag=--bbfh.group,limit=1,sort=nearest] run function bubblevehicles:events/_clicked_seat/_start_riding/ride
execute unless score @p[tag=--bbfh.this_player] bbfh.id = @s bbfh.owner run tellraw @p[tag=--bbfh.this_player] ["", {"text":"Permission denied", "color":"red"}]
