import pandas as pd
import re
df = pd.read_table("mouse_microarray.txt",encoding="utf-8").head()
gene_name = df[df.iloc[:,[33,34]].mean(axis = 1)>100].iloc[:,[1]]
for r in re.findall(r"\['([^\[\]]*\d\d\d\d[^\[\]]*)'\]",str(gene_name.values.tolist())):
	print(r)
