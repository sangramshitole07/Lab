import random 

n_trails=[10,100,1000,10000]

for n in n_trails:
    tosses=[random.choice(["Head","Tails"]) for i in range(n)]
    heads=tosses.count("Head")
    tails=tosses.count("Tails")
    print(f"Trails:{n} ")
    print("heads :",heads)
    print("tails",tails)
    print("P(Head)",heads/n)
    print("p(Tail): ",tails/n)
    