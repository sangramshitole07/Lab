import random

n=6000
rolls=[random.randint(1,6) for i in range(n)]

print("Die Rolling Results")
for outcome in range(1,7):
    count=rolls.count(outcome)
    probabilty=count/n
    print(f"Outcome {outcome} : count={count},Probability = {probabilty:.4f}")