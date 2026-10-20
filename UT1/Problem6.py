import random

n=10000
coin_tosses=[random.choice(["Heads","Tails"]) for i in range(n)]
die_roll=[random.randint(1,6) for i in range(n)]
A={"Heads"}
B={2,4,6}

p_A=sum(1 for x in coin_tosses if x in A)/n
p_B=sum(1 for x in die_roll if x in B)/n

P_intersection=sum(1 for x in range(n)
                   if coin_tosses[x] in A and die_roll[x] in B
                   )/n
result=p_B*p_A
print("Probablity of Intersection : " ,P_intersection)
print("probablility of P(A) x P(B) ", result)

