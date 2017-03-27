# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 09:07:11 2017

@author: Jieqiang.Zhu

find drugs in DILIrank possess four alerts
"""

import pandas as pd
from rdkit import Chem

# import alerts list
Furans = "c1ccc[oX2]1"
Phenols = "[OH]c1ccccc1"
Nitroaromatics = "a[$([NX3](=[OX1])=[OX1]),$([NX3+](=[OX1])[O-])]"
Thiophenes = "c1ccc[sX2]1"

# import drugs in DILIrank
drugs = pd.read_excel("DILIrank Drugs with SMILES.xlsx").SMILES

# Doing substructure search
Furan_result = []
Phenols_result =[]
Nitroaromatics_result =[]
Thiophenes_result =[]

for drug in drugs:
    m = Chem.MolFromSmiles(drug)
    Furan_result.append(m.HasSubstructMatch(Chem.MolFromSmarts(Furans)))
    Phenols_result.append(m.HasSubstructMatch(Chem.MolFromSmarts(Phenols)))
    Nitroaromatics_result.append(m.HasSubstructMatch(Chem.MolFromSmarts(Nitroaromatics)))
    Thiophenes_result.append(m.HasSubstructMatch(Chem.MolFromSmarts(Thiophenes)))

combine_result = pd.DataFrame({"Furans":Furan_result,
                               "Phenols":Phenols_result,
                               "Nitroaromatics":Nitroaromatics_result,
                               "Thiophenes":Thiophenes_result})

# write result to csv
combine_result.to_csv("Drugs with 4 alerts.csv")
