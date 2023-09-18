tellraw @a ["", {"text":"→ ", "color":"gray"}, {"text":"BubbleVehicles", "hoverEvent":{"action": "show_text", "contents": "made by bbfh aka BubbleFish"}}, {"text":" datapack was loaded", "color":"gray"}]

scoreboard objectives add bbfh.runtime dummy
scoreboard objectives add bbfh.id dummy
scoreboard objectives add bbfh.owner dummy
scoreboard objectives add bbfh.key_forward dummy
scoreboard objectives add bbfh.key_strafe dummy
scoreboard objectives add bbfh.on_drop minecraft.custom:minecraft.drop

scoreboard objectives add bbfh.is_glovebox_open dummy
scoreboard objectives add bbfh.is_locked dummy

scoreboard objectives add --bbfh.max_health dummy
scoreboard objectives add --bbfh.is_paintable dummy
scoreboard objectives add --bbfh.max_speed dummy

#> INSERT <bbfh.auto>

team add bubblevehicles "BubbleVehicles"
team modify bubblevehicles collisionRule never
