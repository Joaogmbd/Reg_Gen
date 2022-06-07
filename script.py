x = 5001
y = 1
name = "person"

while (y < x):
    number = str(randint(0, 90000000)).zfill(8)
    print("register('" + str(name) + str(y)+ "', " + str(number) + ").")
    y += 1
