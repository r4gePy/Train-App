from route import Route
from train import Train
from station import Station

train = Train("123", "123", 10)
m = Route()
m.create_route("stv", "moscow")
m.add_point("rostov")
m.add_point("voronezh")
r = m.print_station()
train.get_route(r)
print(train.return_next_position())
print(train.return_position())
print(train.return_previous())