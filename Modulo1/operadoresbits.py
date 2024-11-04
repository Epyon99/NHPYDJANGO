a = 5
b = 3

print (a & b)
# 000000101
# 000000011
# 000000001 --resultado

print (a | b)
# 000000101
# 000000011
# 000000111

print (a ^ b) # True o False | True,o True o True, o False o False | False
# 000000101
# 000000011
# 000000110

print (~a)
# 000000101
# 111111010 > -0b010

# 6 
# 000000110
# 111111001 + 1 # Complemento a 1 (+1)
# 111111010 < -6 # Completo a 2