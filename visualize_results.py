# Recreate the five statistical-analysis figures.
# The generated figures are:
# 1 boxplot + observations
# 2 means with 95% confidence intervals
# 3 distribution comparison
# 4 residual diagnostic
# 5 pairwise mean differences
import pandas as pd, numpy as np, matplotlib.pyplot as plt
from statsmodels.formula.api import ols

df=pd.read_csv("data/iris_statistical_analysis.csv")
cats=["setosa","versicolor","virginica"]
groups=[df.loc[df.species==s,"petal_length_cm"] for s in cats]
summary=pd.read_csv("data/group_summary_ci.csv")
model=ols("petal_length_cm ~ C(species)",data=df).fit()

# 1
fig,ax=plt.subplots(figsize=(9,6)); ax.boxplot(groups,tick_labels=cats)
for i,s in enumerate(cats,1):
    y=df.loc[df.species==s,"petal_length_cm"]; ax.scatter(np.random.default_rng(i).normal(i,.045,len(y)),y,alpha=.45,s=18)
ax.set_title("Petal Length by Species"); ax.set_xlabel("Species"); ax.set_ylabel("Petal length (cm)")
fig.tight_layout(); fig.savefig("visualizations/01_boxplot_petal_length.png",bbox_inches="tight"); plt.close(fig)

# 2
fig,ax=plt.subplots(figsize=(9,6)); x=np.arange(3); m=summary["mean"].values; err=np.vstack([m-summary.ci_low.values,summary.ci_high.values-m])
ax.errorbar(x,m,yerr=err,fmt="o",capsize=6,markersize=8); ax.set_xticks(x,cats); ax.set_ylabel("Mean petal length (cm)"); ax.set_xlabel("Species")
ax.set_title("Mean Petal Length with 95% Confidence Intervals"); fig.tight_layout(); fig.savefig("visualizations/02_means_confidence_intervals.png",bbox_inches="tight"); plt.close(fig)

# 3
fig,ax=plt.subplots(figsize=(9,6))
for s in cats: ax.hist(df.loc[df.species==s,"petal_length_cm"],bins=10,alpha=.45,label=s,density=True)
ax.set_title("Petal Length Distributions by Species"); ax.set_xlabel("Petal length (cm)"); ax.set_ylabel("Density"); ax.legend(frameon=False)
fig.tight_layout(); fig.savefig("visualizations/03_distribution_comparison.png",bbox_inches="tight"); plt.close(fig)

# 4
fig,ax=plt.subplots(figsize=(9,6)); ax.scatter(model.fittedvalues,model.resid,alpha=.7); ax.axhline(0,linewidth=1)
ax.set_title("ANOVA Residual Diagnostic"); ax.set_xlabel("Fitted petal length"); ax.set_ylabel("Residual")
fig.tight_layout(); fig.savefig("visualizations/04_residual_diagnostic.png",bbox_inches="tight"); plt.close(fig)

# 5
diffs=[summary.loc[0,"mean"]-summary.loc[1,"mean"],summary.loc[0,"mean"]-summary.loc[2,"mean"],summary.loc[1,"mean"]-summary.loc[2,"mean"]]
fig,ax=plt.subplots(figsize=(9,6)); ax.barh(["setosa vs versicolor","setosa vs virginica","versicolor vs virginica"],diffs); ax.axvline(0,linewidth=1)
ax.set_title("Pairwise Mean Differences in Petal Length"); ax.set_xlabel("Mean difference (cm)")
fig.tight_layout(); fig.savefig("visualizations/05_pairwise_mean_differences.png",bbox_inches="tight"); plt.close(fig)
