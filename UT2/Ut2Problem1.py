
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# ==========================================
# STEP 1: Identify the random variable
# ==========================================

p = 0.30
q = 1 - p

# X = 1: Customer clicks
# X = 0: Customer does not click
# X is a discrete random variable
# X follows Bernoulli distribution

print("Distribution: Bernoulli")
print("P(X=0):", q)
print("P(X=1):", p)


# ==========================================
# STEP 2 & 3: Theoretical PMF and simulation
# ==========================================

sample_size = 20

samples = np.random.binomial(
    n=1,
    p=p,
    size=sample_size
)

print("\nGenerated observations:")
print(samples)
print("Number of observations:", len(samples))


# ==========================================
# STEP 4: Count clicks and non-clicks
# ==========================================

number_of_clicks = np.sum(samples == 1)
number_of_non_clicks = np.sum(samples == 0)

print("\nNumber of clicks:", number_of_clicks)
print("Number of non-clicks:", number_of_non_clicks)
print("Total customers:", number_of_clicks + number_of_non_clicks)


# ==========================================
# STEP 5: Calculate empirical PMF
# ==========================================

Probability_0 = np.mean(samples == 0)
Probability_1 = np.mean(samples == 1)

print("\nEmpirical PMF")
print("P(X=0):", Probability_0)
print("P(X=1):", Probability_1)


# ==========================================
# STEP 6 & 7: Compare and plot PMFs
# ==========================================

x = [0, 1]

theoretical_pmf = [q, p]
empirical_pmf = [Probability_0, Probability_1]

width = 0.35

plt.figure(figsize=(7, 5))

plt.bar(
    np.array(x) - width / 2,
    theoretical_pmf,
    width,
    label="Theoretical PMF"
)

plt.bar(
    np.array(x) + width / 2,
    empirical_pmf,
    width,
    label="Empirical PMF"
)

plt.xlabel("Outcome X")
plt.ylabel("Probability")
plt.title("Theoretical vs Empirical PMF")
plt.xticks(x)
plt.ylim(0, 1)
plt.legend()
plt.tight_layout()
plt.show()


# ==========================================
# STEP 8-11: Expectation and variance
# ==========================================

theoretical_expectation = p
theoretical_variance = p * q

empirical_expectation = np.mean(samples)
empirical_variance = np.var(samples)

print("\nExpectation and Variance")
print("Theoretical expectation:", theoretical_expectation)
print("Empirical expectation:", empirical_expectation)
print("Theoretical variance:", theoretical_variance)
print("Empirical variance:", empirical_variance)


# ==========================================
# STEP 12: Final result table
# ==========================================

measures = [
    "P(X=0)",
    "P(X=1)",
    "Expectation",
    "Variance"
]

theoretical_values = [
    q,
    p,
    theoretical_expectation,
    theoretical_variance
]

empirical_values = [
    Probability_0,
    Probability_1,
    empirical_expectation,
    empirical_variance
]

result_table = pd.DataFrame({
    "Measure": measures,
    "Theoretical Value": theoretical_values,
    "Empirical Value": empirical_values
})

result_table["Absolute Difference"] = abs(
    result_table["Theoretical Value"]
    - result_table["Empirical Value"]
)

print("\nFinal Result Table")
print(result_table.round(4).to_string(index=False))


# ==========================================
# STEP 13: Effect of sample size
# ==========================================

sample_sizes = [10, 100, 1000, 10000]
results = []

for n in sample_sizes:

    sample = np.random.binomial(
        n=1,
        p=p,
        size=n
    )

    prob_0 = np.mean(sample == 0)
    prob_1 = np.mean(sample == 1)

    empirical_mean = np.mean(sample)
    empirical_var = np.var(sample)

    results.append({
        "Sample Size": n,
        "Empirical P(X=0)": prob_0,
        "Empirical P(X=1)": prob_1,
        "Empirical Mean": empirical_mean,
        "Empirical Variance": empirical_var
    })

df = pd.DataFrame(results)

print("\nEffect of Sample Size")
print(df.round(4).to_string(index=False))

print("\nTheoretical reference values:")
print("P(X=0):", q)
print("P(X=1):", p)
print("Expectation:", p)
print("Variance:", p * q)
