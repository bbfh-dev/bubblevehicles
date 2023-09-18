ride @p[tag=--bbfh.this_player] mount @s
function bubblevehicles:registry/determine_group
execute if entity @s[tag=--bbfh.driver] run function bubblevehicles:gui/setup
