data modify storage bubblevehicles Runtime.Motion set from entity @s Motion
execute store result score lib.x bbfh.runtime run data get storage bubblevehicles Runtime.Motion[0] 1000.0
execute store result score lib.z bbfh.runtime run data get storage bubblevehicles Runtime.Motion[2] 1000.0

scoreboard players set @s bbfh.key_forward 0
scoreboard players set @s bbfh.key_strafe 0

scoreboard players set lib.dir bbfh.runtime 0
execute if score lib.z bbfh.runtime matches 0 if score lib.x bbfh.runtime matches 0 run scoreboard players set lib.dir bbfh.runtime -999
execute unless score lib.dir bbfh.runtime matches -999 run function lib:keystrokes/_detect/calculate
