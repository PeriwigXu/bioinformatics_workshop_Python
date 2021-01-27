import pandas as pd

outf = open("hw3_result.txt","w")
def question1():
	print("-"*10+"question1"+"-"*10, file=outf)
	i = 0
	with open("yeast_genes.pep") as inf:
		for line in inf:
			if line[0]==">":
				i+=1
	print("Sequences number:" ,i, file=outf)
	
question1()


def question2():
	print("-"*10+"question2"+"-"*10,file=outf)
	global df
	df = pd.read_csv("yeast.blastp", sep="\t",
					 names=["qseqid","sseqid", "pident", "length", "mismatch", "gapopen", "qstart", "qend", "sstart", "send", "evalue","bitscore"])
	global cnt_srs
	cnt_srs = (df["qseqid"].value_counts())
	print(cnt_srs, file=outf)
	
question2()
	
def question3(): #must run after question2() 'cause df and cnt_srs are necessary
	print("-"*10+"question3"+"-"*10, file=outf)
	fml_lst = []
	def in_fml(gene, fml_lst):
		for fml in fml_lst:
			if gene in fml:
				return fml_lst.index(fml) + 1
		return False
	for gene in cnt_srs.index:
		for prtnr in df["sseqid"][df["qseqid"]==gene]:
			if not gene == prtnr:
				if not (in_fml(gene, fml_lst) or in_fml(prtnr,fml_lst)):
					fml_lst.append([gene,prtnr])
				elif in_fml(gene, fml_lst) and not in_fml(prtnr,fml_lst):
					fml_lst[in_fml(gene,fml_lst)-1].append(prtnr)
				elif in_fml(prtnr,fml_lst) and not in_fml(gene,fml_lst):
					fml_lst[in_fml(prtnr,fml_lst)-1].append(gene)
	for fml in fml_lst:
		print(fml, file=outf)
		 
question3()
	
	
