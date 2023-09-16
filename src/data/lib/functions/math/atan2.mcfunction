#! Remez Algorithm
# a := min (|x|, |y|) / max (|x|, |y|)
# s := a * a
# r := ((-0.0464964749 * s + 0.15931422) * s - 0.327622764) * s * a + a
# if |y| > |x| then r := 1.57079637 - r
# if x < 0 then r := 3.14159274 - r
# if y < 0 then r := -r

# a
scoreboard players operation #a bbfh.runtime = ^lib.a bbfh.runtime
scoreboard players operation #b bbfh.runtime = ^lib.b bbfh.runtime
execute if score #a bbfh.runtime matches ..-1 run scoreboard players operation #a bbfh.runtime *= -1 bbfh.auto
execute if score #b bbfh.runtime matches ..-1 run scoreboard players operation #b bbfh.runtime *= -1 bbfh.auto
scoreboard players operation #c bbfh.runtime = #a bbfh.runtime
scoreboard players operation #c bbfh.runtime < #b bbfh.runtime
scoreboard players operation #d bbfh.runtime = #a bbfh.runtime
scoreboard players operation #d bbfh.runtime > #b bbfh.runtime
scoreboard players operation #c bbfh.runtime *= 1000 bbfh.auto
scoreboard players operation #c bbfh.runtime /= #d bbfh.runtime

# s
scoreboard players operation #d bbfh.runtime = #c bbfh.runtime
scoreboard players operation #d bbfh.runtime *= #d bbfh.runtime
scoreboard players operation #d bbfh.runtime /= 1000 bbfh.auto

# r
scoreboard players operation lib.out bbfh.runtime = #d bbfh.runtime
scoreboard players operation lib.out bbfh.runtime *= -46496 bbfh.auto
scoreboard players operation lib.out bbfh.runtime /= 100000 bbfh.auto
scoreboard players add lib.out bbfh.runtime 1593
scoreboard players operation lib.out bbfh.runtime *= #d bbfh.runtime
scoreboard players operation lib.out bbfh.runtime /= 1000 bbfh.auto
scoreboard players remove lib.out bbfh.runtime 3276
scoreboard players operation lib.out bbfh.runtime *= #d bbfh.runtime
scoreboard players operation lib.out bbfh.runtime /= 1000 bbfh.auto
scoreboard players operation lib.out bbfh.runtime *= #c bbfh.runtime
scoreboard players operation lib.out bbfh.runtime /= 10000 bbfh.auto
scoreboard players operation lib.out bbfh.runtime += #c bbfh.runtime
execute if score #b bbfh.runtime > #a bbfh.runtime run scoreboard players remove lib.out bbfh.runtime 1570
execute if score #b bbfh.runtime > #a bbfh.runtime run scoreboard players operation lib.out bbfh.runtime *= -1 bbfh.auto
execute if score ^lib.a bbfh.runtime matches ..-1 run scoreboard players remove lib.out bbfh.runtime 3141
execute if score ^lib.a bbfh.runtime matches ..-1 run scoreboard players operation lib.out bbfh.runtime *= -1 bbfh.auto
execute if score ^lib.b bbfh.runtime matches ..-1 run scoreboard players operation lib.out bbfh.runtime *= -1 bbfh.auto

# rad2deg()
scoreboard players operation lib.out bbfh.runtime *= 57295 bbfh.auto
scoreboard players operation lib.out bbfh.runtime /= 1000000 bbfh.auto
