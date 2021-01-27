import pandas as pd
import re
df = pd.read_csv("mouse_microarray.txt",sep="\t")

ave_df = pd.DataFrame(df.iloc[:,3])

print("Calculating average...", end="") #actually sum instead of average, but this way should be faster.
for i in range(3,len(df.columns),2):
	ave_df[df.columns[i]] = df.iloc[:,i:i+2].apply(lambda x: x.sum(), axis=1)  
print("Completed.")

print("Picking eye-specific genes...", end="")
ave_df = ave_df >= 200
gene_lst = [ave_df.loc[a].name for a in range(len(ave_df)) if ave_df.loc[a]["eye"] and sum(list(ave_df.loc[a]))==1]
print("Completed.")
print("-"*10+"question 1"+"-"*10)
print("Number of eye-specific genes:",len(gene_lst))

print("-"*10+"question 2"+"-"*10)
unk_gn_lst = [df["name"][gene] for gene in gene_lst if re.search(r"\d\d\d\d",df["name"][gene])]
print("Number of unknown genes:", len(unk_gn_lst))