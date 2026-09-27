import pandas as pd, numpy as np
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd

df=pd.read_csv("data/iris_statistical_analysis.csv")
cats=["setosa","versicolor","virginica"]
groups=[df.loc[df.species==s,"petal_length_cm"] for s in cats]

# Assumption checks
for s,g in df.groupby("species"):
    print("Shapiro",s,stats.shapiro(g.petal_length_cm))
print("Levene:",stats.levene(*groups,center="median"))

# One-way ANOVA
model=ols("petal_length_cm ~ C(species)",data=df).fit()
print(sm.stats.anova_lm(model,typ=2))

# Effect size
tab=sm.stats.anova_lm(model,typ=2)
eta=tab.loc["C(species)","sum_sq"]/tab["sum_sq"].sum()
print("Eta squared:",eta)

# Post-hoc Tukey HSD
print(pairwise_tukeyhsd(df.petal_length_cm,df.species))

# 95% confidence intervals
for s,g in df.groupby("species"):
    ci=stats.t.interval(.95,len(g)-1,loc=g.petal_length_cm.mean(),scale=stats.sem(g.petal_length_cm))
    print(s,"mean=",g.petal_length_cm.mean(),"95% CI=",ci)
