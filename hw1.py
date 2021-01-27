print("-"*10+"Quesion 1"+"-"*10)
import numpy as np
import pandas as pd
import re

df = pd.read_csv("chicken_SNPs.txt", sep = "\t")
poplst = ["pop"+str(i+1) for i in range(10)]
htrdic = {}

def prntloci(dic):
	n_loci = np.array([len(htrdic[x]) for x in htrdic])
	print("pop:", poplst[np.argmax(n_loci)])
	print("loci number:", n_loci[np.argmax(n_loci)])
		
for pop in poplst:
	htrdic[pop] = [i for i in df[pop] if int(i.split(":")[0])*int(i.split(":")[1]) > 0]
prntloci(htrdic)

print("-"*10+"Quesion 2"+"-"*10)
for pop in poplst:
	htrdic[pop] = [i for i in df[pop] if int(i.split(":")[0])==0 and int(i.split(":")[1]) > 0]
prntloci(htrdic)