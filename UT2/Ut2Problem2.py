
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# STEP 1: Define the Binomial distribution
# ==========================================

n = 50                  # Transactions per hour
p = 0.04                # Probability of being flagged
q = 1 - p
number_of_hours = 20000

# X = Number of flagged transactions in one hour
# X follows Binomial(n=50, p=0.04)

print("Distribution: Binomial")
print("Number of transactions per hour:", n)
print("Probability of flagging:", p)
print("Probability of not being flagged:", q)


# ==========================================
# STEP 2: Simulate 20,000 independent hours
# ==========================================

X = np.random.binomial(
    n=n,
    p=p,
    size=number_of_hours
)

print("\nFlagged transactions in the first 20 hours:")
print(X[:20])


# ==========================================
# STEP 3: Basic summary statistics
# ==========================================

print("\nTotal simulated hours:", len(X))
print("Average flagged transactions per hour:", np.mean(X))
print("Minimum flagged transactions in an hour:", np.min(X))
print("Maximum flagged transactions in an hour:", np.max(X))


# ==========================================
# STEP 4: Theoretical expectation and variance
# ==========================================

theoretical_mean = n * p
theoretical_variance = n * p * q

print("\nTheoretical expectation:", theoretical_mean)
print("Theoretical variance:", theoretical_variance)
print("Empirical expectation:", np.mean(X))
print("Empirical variance:", np.var(X))


# ==========================================
# STEP 5: Investigation team capacity
# ==========================================

capacity = 4

hours_within_capacity = np.sum(X <= capacity)
hours_exceeding_capacity = np.sum(X > capacity)

probability_within_capacity = np.mean(X <= capacity)
probability_exceeding_capacity = np.mean(X > capacity)

print("\nInvestigation Team Capacity Analysis")
print("Maximum capacity per hour:", capacity)
print("Hours within capacity:", hours_within_capacity)
print("Hours exceeding capacity:", hours_exceeding_capacity)
print("Probability within capacity:", probability_within_capacity)
print("Probability exceeding capacity:", probability_exceeding_capacity)


# ==========================================
# STEP 6: Frequency distribution
# ==========================================

values, counts = np.unique(X, return_counts=True)

frequency_table = pd.DataFrame({
    "Flagged Transactions": values,
    "Number of Hours": counts,
    "Empirical Probability": counts / number_of_hours
})

print("\nFrequency Distribution")
print(frequency_table.to_string(index=False))


# ==========================================
# STEP 7: Plot the simulated results
# ==========================================

plt.figure(figsize=(9, 5))

plt.hist(
    X,
    bins=np.arange(-0.5, X.max() + 1.5, 1),
    edgecolor="black",
    density=True
)

plt.xlabel("Number of Flagged Transactions")
plt.ylabel("Empirical Probability")
plt.title("Binomial Distribution: Fraud Detection Simulation")
plt.xticks(range(0, X.max() + 1))
plt.tight_layout()
plt.show()
