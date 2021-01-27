import pandas as pd

outf = open("hw4_result.txt","w")
df = pd.read_csv("BIOGRID-MV-Physical-4.2.193.tab2.txt", sep = "\t").astype('str')
#print(df.iloc[:,7:9])
#print(df.iloc[:,-9:-7])
df = df[(df["Organism Interactor A"]=="9606") & (df["Organism Interactor B"]=="9606")]

prtn_srs = (df["Official Symbol Interactor A"].drop_duplicates())
#print(prtn_srs)
fml_lst = []

def in_fml(gene, fml_lst):
		for fml in fml_lst:
			if gene in fml:
				return fml_lst.index(fml) + 1
		return False

for gene in prtn_srs:
	for prtnr in df["Official Symbol Interactor B"][df["Official Symbol Interactor A"]==gene]:
		if not gene == prtnr:
			if not (in_fml(gene, fml_lst) or in_fml(prtnr,fml_lst)):
				fml_lst.append([gene,prtnr])
			elif in_fml(gene, fml_lst) and not in_fml(prtnr,fml_lst):
				fml_lst[in_fml(gene,fml_lst)-1].append(prtnr)
			elif in_fml(prtnr,fml_lst) and not in_fml(gene,fml_lst):
				fml_lst[in_fml(prtnr,fml_lst)-1].append(gene)

for fml in fml_lst:
	print(fml, file=outf)