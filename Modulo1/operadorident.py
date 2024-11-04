x = 15
y = x

print (x is y)

x = 20
y = 15
print (x is not y)

x = 20
y = x
y += 1
print (y)