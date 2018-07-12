from birds.bird import Bird, Seabird, Fowl

my_bird = Bird('robin', 'chirp')
new_bird = Bird('crow', 'croak')

# print(my_bird.call)
# print(my_bird.kind)

# print(new_bird.call)
# print(new_bird.kind)

# print(my_bird.get_description())

# my_sea_going_bird = Seabird('Gull', 'Skraawwk!', 2)

# print(my_sea_going_bird.call)
# print(my_sea_going_bird.kind)
# print(my_sea_going_bird.diving_depth)

# print(my_sea_going_bird.get_description())

my_fowl = Fowl('hen', 'bockbock', 'landfowl')
other_fowl = Fowl('duck', 'quack', 'waterfowl')

print(my_fowl.call)
print(my_fowl.kind)
print(my_fowl.fowl_type)
print(my_fowl.get_description())
print(other_fowl.get_description())