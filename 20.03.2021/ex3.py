# shared references
A = ["AAA", "AAB", "ABC"]
B = A
C = A
print(A)
print(B)
print(C)
C[2] = "CCC"
print(C)
print(A)
print(B)

print(("\ncopy:"))
D = ["DDD", "DDE", "DEF"]
E = D[:]
E[2] = "EEE"
print(E)
print(D)