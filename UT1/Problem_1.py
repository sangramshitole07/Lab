import random

n=100

tosses=[random.choice(["Heads","Tails"]) for i in range(n)]

Heads=tosses.count("Heads")
Tails=tosses.count("Tails")

p_heads=Heads/n
p_tails=Tails/n

print("No. of Heads: ", Heads)
print("No. of Tails: ", Tails)
print("Probablilty of Heads : ",p_heads)
print("Probablilty of Tails :", p_tails)