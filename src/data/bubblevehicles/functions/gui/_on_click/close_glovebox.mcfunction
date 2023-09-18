scoreboard players set @e[type=llama,tag=--bbfh.group,limit=1,sort=nearest] bbfh.is_glovebox_open 0
data modify entity @e[type=armor_stand,tag=--bbfh.group,limit=1] ArmorItems[0].tag.bbfh_items set from entity @e[type=llama,tag=--bbfh.group,limit=1,sort=nearest] Items
