from auto.auto import Door, Wheel, Engine, Body

my_door = Door('automatic')
my_wheel = Wheel('3', "pirelli")
my_engine = Engine('lpg', 2000)
my_body = Body('fibre', True, False)

print(my_door.close())
print(my_door.open())

print(my_wheel.stop())

print(my_engine.start())

print(my_body.composition)
print(my_body.close_roof())