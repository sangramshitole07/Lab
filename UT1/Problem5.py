A={2,4,6}
B={4,5,6}
n=6
p_A=len(A)/n
p_B=len(B)/n
p_Intersection=len(A & B)/n
p_union=len(A | B)/n

print("Probablilty of A ", p_A )
print("Probablilty of B ", p_B)
print("Probalility of Intersection ", p_Intersection)
print("Probalility of Union ", p_union)
print("Verifying Union : ",p_A+p_B-p_Intersection)