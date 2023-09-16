# Source: https://github.com/CloudWolfYT/WASD-Detection

# Debouncing rotation
scoreboard players operation lib.rot_y bbfh.runtime = @s bbfh.runtime
execute store result score @s bbfh.runtime run data get entity @s Rotation[0] 1.0

# lib.dir = atan2(Motion[0], Motion[2]) + Rotation[0]
scoreboard players operation ^lib.a bbfh.runtime = lib.z bbfh.runtime
scoreboard players operation ^lib.b bbfh.runtime = lib.x bbfh.runtime
function lib:math/atan2
scoreboard players operation lib.dir bbfh.runtime = lib.out bbfh.runtime
scoreboard players operation lib.dir bbfh.runtime += lib.rot_y bbfh.runtime

# Map angle to the range 0..360
scoreboard players operation lib.dir bbfh.runtime %= 360 bbfh.auto

# Determine pressed key based on the dir angle range
execute if score lib.dir bbfh.runtime matches 23..157 run scoreboard players set @s bbfh.key_strafe -1
execute if score lib.dir bbfh.runtime matches 112..248 run scoreboard players set @s bbfh.key_forward -1
execute if score lib.dir bbfh.runtime matches 203..337 run scoreboard players set @s bbfh.key_strafe 1
execute if score lib.dir bbfh.runtime matches 293..360 run scoreboard players set @s bbfh.key_forward 1
execute if score lib.dir bbfh.runtime matches 0..67 run scoreboard players set @s bbfh.key_forward 1
