
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.metrics import (
    confusion_matrix,
    ConfusionMatrixDisplay,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_curve,
    roc_auc_score
)

# ==========================================
# STEP 1: Actual and predicted labels
# ==========================================

# 1 = Fraud, 0 = Legitimate

y_true = np.array([
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0
])

# Predicted labels from the model
y_pred = np.array([
    1, 1, 1, 1, 0, 0, 0, 0, 0, 0,
    1, 1, 0, 0, 0, 0, 0, 0, 0, 0
])

# Model scores / probabilities for the positive class
y_score = np.array([
    0.95, 0.90, 0.85, 0.80, 0.40,
    0.35, 0.30, 0.25, 0.20, 0.10,
    0.90, 0.70, 0.40, 0.30, 0.25,
    0.20, 0.15, 0.10, 0.05, 0.02
])


# ==========================================
# STEP 2: Calculate confusion matrix
# ==========================================

tn, fp, fn, tp = confusion_matrix(
    y_true, y_pred, labels=[0, 1]
).ravel()

print("Confusion Matrix:")
print(confusion_matrix(y_true, y_pred, labels=[0, 1]))

print("\nTP:", tp)
print("TN:", tn)
print("FP:", fp)
print("FN:", fn)


# ==========================================
# STEP 3: Calculate AI/ML metrics
# ==========================================

total = tp + tn + fp + fn

accuracy = (tp + tn) / total
precision = tp / (tp + fp) if tp + fp else 0
recall = tp / (tp + fn) if tp + fn else 0
specificity = tn / (tn + fp) if tn + fp else 0
fpr = fp / (fp + tn) if fp + tn else 0
fnr = fn / (fn + tp) if fn + tp else 0
fdr = fp / (tp + fp) if tp + fp else 0
forate = fn / (fn + tn) if fn + tn else 0
positive_rate = (tp + fp) / total

f1 = f1_score(y_true, y_pred, zero_division=0)

metrics = pd.DataFrame({
    "Metric": [
        "Accuracy",
        "Precision",
        "Recall / TPR",
        "Specificity / TNR",
        "F1-score",
        "False Positive Rate",
        "False Negative Rate",
        "False Discovery Rate",
        "False Omission Rate",
        "Positive Prediction Rate"
    ],
    "Value": [
        accuracy,
        precision,
        recall,
        specificity,
        f1,
        fpr,
        fnr,
        fdr,
        forate,
        positive_rate
    ]
})

metrics["Percentage"] = metrics["Value"] * 100

print("\nAI/ML Metrics:")
print(metrics.round(4).to_string(index=False))


# ==========================================
# STEP 4: Plot confusion matrix
# ==========================================

cm = confusion_matrix(y_true, y_pred, labels=[0, 1])

display = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["Legitimate (0)", "Fraud (1)"]
)

display.plot()
plt.title("Confusion Matrix")
plt.tight_layout()
plt.show()


# ==========================================
# STEP 5: Plot metric comparison
# ==========================================

plt.figure(figsize=(10, 5))

plt.bar(
    metrics["Metric"],
    metrics["Percentage"]
)

plt.ylabel("Percentage (%)")
plt.title("Comparison of Classification Metrics")
plt.xticks(rotation=45, ha="right")
plt.ylim(0, 100)
plt.tight_layout()
plt.show()


# ==========================================
# STEP 6: Plot ROC curve and calculate AUC
# ==========================================

fpr_curve, tpr_curve, thresholds = roc_curve(
    y_true, y_score
)

auc_value = roc_auc_score(y_true, y_score)

plt.figure(figsize=(7, 5))

plt.plot(
    fpr_curve,
    tpr_curve,
    label=f"ROC Curve (AUC = {auc_value:.3f})"
)

plt.plot(
    [0, 1],
    [0, 1],
    linestyle="--",
    label="Random Classifier"
)

plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("Receiver Operating Characteristic (ROC)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

print("\nROC-AUC:", auc_value)


# ==========================================
# STEP 7: Print ROC threshold table
# ==========================================

roc_table = pd.DataFrame({
    "Threshold": thresholds,
    "FPR": fpr_curve,
    "TPR": tpr_curve
})

print("\nROC Threshold Table:")
print(roc_table.round(4).to_string(index=False))
