x = 10005000
y = 10000000
name = "person"

while (y < x):
    phone = str(y).zfill(8)
    print("register( '" + str(name) + str(y)+ "', " + str(phone) + ").")
    y += 1
