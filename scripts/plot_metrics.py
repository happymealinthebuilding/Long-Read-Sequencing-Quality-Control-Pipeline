import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys

input_file = sys.argv[1]
out_dir = sys.argv[2]

df = pd.read_csv(input_file)

# Save summary statistics
summary = df.describe()
summary.to_csv(f"{out_dir}/summary_statistics.csv")

# GC Content
plt.figure()
sns.histplot(df["gc_content"], bins=50)
plt.axvline(df["gc_content"].mean(), linestyle="--")
plt.title("GC Content Distribution")
plt.xlabel("GC %")
plt.savefig(f"{out_dir}/gc_distribution.png")

# Read Length
plt.figure()
sns.histplot(df["read_length"], bins=50)
plt.axvline(df["read_length"].mean(), linestyle="--")
plt.title("Read Length Distribution")
plt.xlabel("Length")
plt.savefig(f"{out_dir}/length_distribution.png")

# Quality
plt.figure()
sns.histplot(df["mean_quality"], bins=50)
plt.axvline(df["mean_quality"].mean(), linestyle="--")
plt.title("Mean Read Quality Distribution")
plt.xlabel("Quality Score")
plt.savefig(f"{out_dir}/quality_distribution.png")

print(summary)