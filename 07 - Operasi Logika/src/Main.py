"""
Operasi Logika pada python
operasi yang menghasilkan nilai boolean
Operator logika
1. and  ( & )
2. or   ( | )
3. xor  ( ^ )
4. not  ( ~ )
"""


print("")

print("========= AND =========")

# AND
a = False
b = False
c = a and b
print(a, "AND", b, '=', c)

# AND
a = False
b = True
c = a and b
print(a, "AND", b, ' =', c)

# AND
a = True
b = False
c = a & b
print(a, " AND", b, '=', c)

# AND
a = True
b = True
c = a & b
print(a, " AND", b, ' =', c)

print("")

print("========= OR =========")

# OR
a = False
b = False
c = a or b
print(a, "OR", b, '=', c)

# OR
a = False
b = True
c = a | b
print(a, "OR", b, ' =', c)

# OR
a = True
b = False
c = a | b
print(a, " OR", b, '=', c)

# OR
a = True
b = True
c = a or b
print(a, " OR", b, ' =', c)

print("")

print("========= XOR =========")

# XOR
a = False
b = False
c = a ^ b
print(a, "XOR", b, '=', c)

# XOR
a = False
b = True
c = a ^ b
print(a, "XOR", b, ' =', c)

# XOR
a = True
b = False
c = a ^ b
print(a, " XOR", b, '=', c)

# XOR
a = True
b = True
c = a ^ b
print(a, " XOR", b, ' =', c)

print("")


print("========= NOT =========")
# NOT 
a = True
b = False
c = not a
d = not b
print(a)
print("------NOT")
print(c)

print("")

print(b)
print("------NOT")
print(d)