speed = eval(input("enter speed: "))
if speed <90:
    print("no ticket! ")
elif speed >=90 and speed<110:
    print("ticket small! ")
else:
    print("ticket big! ")