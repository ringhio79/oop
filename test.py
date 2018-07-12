from auto.auto import Door, Wheel, Engine

my_door = Door('automatic')
my_wheel = Wheel('3', "pirelli")
my_engine = Engine('lpg')

print(my_door.close())
print(my_door.open())

print(my_wheel.stop())

print(my_engine.start())
