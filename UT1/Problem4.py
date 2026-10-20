import random
 
n=10000
rolls=[random.randint(1,6) for i in range(n)]

a={1}
b={6}

A_count=sum(1 for x in rolls if x in a)
B_count=sum(1 for x in rolls if x in b)
Union_count=sum(1 for x in rolls if x in a or x in b)

Prob_A=A_count/n
Prob_B=B_count/n
Union_P=Union_count/n

print("Probablilty of A :",Prob_A)
print("Probablilty of B: ", Prob_B)
print("Probablility of Union :", Union_P)
print("Probability of verifying using a + p : ", Prob_B + Prob_A)
