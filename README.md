# Vehicles

```py
from plugins.vehicles.car import Car, Vehicle
from plugins.vehicles.units import Size

class Rofi(Car):
    size = Size(width=3.0, height=1.0)
    attributes = Car.Attributes(
        health=100,
        max_speed=100,
        wheel_base=4.0,
    )
    model = Vehicle.Model(
        elements=[
            Block()
        ],
        offset=(0, 0, 0),
        scale=0.75,
    )
```
