# E-commerce Purchase Intent Prediction Using Logistic Regression

Machine Learning internship project — **Problem #4: E-commerce Purchase Intent**
(from the LearnDepth Academy "Logistic Regression: Applications & Performance" practice set).

**Student:** Mahwish Arooj

## 1. Project Overview

This project builds a binary classification model that predicts whether an
e-commerce website session will end in a purchase, based on six behavioural
features captured during the session:

- `pages_viewed` — number of distinct pages opened
- `session_minutes` — total session duration, in minutes
- `products_viewed` — number of distinct products viewed
- `cart_additions` — number of times an item was added to the cart
- `discount_seen` — number of discount/promotion offers shown
- `previous_orders` — number of past completed orders by the customer

**Target:** `target` — `1` if the session ended in a purchase, `0` otherwise.

**Algorithm:** Logistic Regression (scikit-learn), inside a `StandardScaler` +
`LogisticRegression` `Pipeline`.

**Actual results obtained** (held-out 20% test set, 200 sessions):

| Metric | Value |
|---|---|
| Accuracy | 0.7300 |
| Precision | 0.7396 |
| Recall | 0.7100 |
| F1-Score | 0.7245 |
| ROC-AUC | 0.8005 |

All numbers above were produced by executing the notebook end-to-end on the
real dataset — none are invented.

## 2. Dataset

- File: `data/dataset_04_ecommerce_purchase_intent.csv`
- 1,000 rows, 7 columns (6 features + 1 binary target)
- No missing values, no duplicate rows, perfectly balanced target (500 / 500)
- Because the raw data was already clean, no rows/columns were changed —
  `data/dataset_04_ecommerce_purchase_intent.csv` is the same file used
  throughout the notebook (no separate "cleaned" file was needed).

## 3. Installation Requirements

- Python 3.9+
- Jupyter Notebook / JupyterLab
- Packages: `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`

Install everything with:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
```

## 4. How to Run the Notebook

1. Keep the folder structure below intact (the notebook loads the dataset
   using a relative path `../data/...`).
2. From the `notebook/` folder, launch Jupyter:

   ```bash
   cd notebook
   jupyter notebook Ecommerce_Purchase_Intent_Logistic_Regression.ipynb
   ```

3. Run all cells from top to bottom (`Kernel → Restart & Run All`). Every
   cell has been verified to run without errors, and generated figures are
   also saved into the `figures/` folder as the notebook executes.

## 5. Libraries Required

| Library | Purpose |
|---|---|
| pandas | Data loading and manipulation |
| numpy | Numerical operations |
| matplotlib | Base plotting |
| seaborn | Statistical visualisations |
| scikit-learn | Train/test split, scaling, Logistic Regression, metrics |

## 6. Project Structure

```
Ecommerce_Purchase_Intent_Logistic_Regression/
│
├── notebook/
│   └── Ecommerce_Purchase_Intent_Logistic_Regression.ipynb
│
├── report/
│   └── Ecommerce_Purchase_Intent_Logistic_Regression_Report.docx
│
├── data/
│   └── dataset_04_ecommerce_purchase_intent.csv
│
├── figures/
│   ├── 01_target_distribution.png
│   ├── 02_feature_distributions.png
│   ├── 03_feature_boxplots.png
│   ├── 04_session_minutes_vs_target.png
│   ├── 05_pages_viewed_vs_target.png
│   ├── 06_products_viewed_vs_target.png
│   ├── 07_cart_additions_vs_target.png
│   ├── 08_previous_orders_vs_target.png
│   ├── 09_discount_seen_vs_target.png
│   ├── 10_correlation_heatmap.png
│   ├── 11_pairplot.png
│   ├── 12_confusion_matrix.png
│   ├── 13_roc_curve.png
│   └── 14_coefficients.png
│
└── README.md
```

## 7. Notes for the Internship Presentation / Viva

- The Word report (`report/Ecommerce_Purchase_Intent_Logistic_Regression_Report.docx`)
  mirrors the notebook exactly — same dataset, same metrics, same figures —
  so you can present from either document.
- Section 12 of the report (and Section 15 of the notebook) walks through the
  model's coefficients feature-by-feature: which behaviours increase vs.
  decrease predicted purchase probability, phrased as **associations found
  in the data**, not proven causes.
- Section 14/15 of the report ("Limitations" / "Future Scope") lists honest,
  realistic next steps (Random Forest, Gradient Boosting, cross-validation,
  hyperparameter tuning, more features) if you're asked "what would you do
  next?" in a viva.
