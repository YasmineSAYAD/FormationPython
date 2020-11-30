import datetime
from datetime import date


d1=datetime.datetime(2019, 4, 15, 9, 36, 42)
print(d1)
d2=datetime.datetime(2019, 4, 19, 9, 36, 42)
print(d2)
if d1<d2:
    print("d1 est plus ancienne que d2")
else:
    print("d1 est plus récente que d2")


d3=datetime.date(2019, 4, 15)
print(type(d3))
print(d3.year)

d4=datetime.time( 9, 36, 42)
print(d4)

#recuperer la date actuelle
dt=date.today()
print(dt)

