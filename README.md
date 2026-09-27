# Week 3 – Statistical Analysis and Hypothesis Testing

## Research question
Do the mean petal lengths differ among setosa, versicolor, and virginica?

## Hypotheses
H0: The population mean petal length is equal across the three species.
H1: At least one species has a different population mean petal length.

## Tests
- Shapiro-Wilk normality checks
- Levene's test for homogeneity of variance
- One-way ANOVA
- Eta-squared effect size
- Tukey HSD post-hoc comparisons
- 95% confidence intervals
- Residual diagnostic visualization

## Run
```bash
pip install -r requirements.txt
python src/run_pipeline.py
```

Main submission: `docs/Week3_Statistical_Analysis_Hypothesis_Testing_Report.docx`
