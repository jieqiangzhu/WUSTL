# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 14:14:53 2017

@author: Jieqiang.Zhu

How to get substructural search and give out format result
"""

import pandas as pd
import numpy as np
from rdkit import Chem


# drug list
# the drugs should be stored in a sheet named "drugs"
drugs = pd.read_excel("354 drugs with RMs formation information.xls","drugs")

# alert list
# the alerts should be stored in a sheet named "alerts"
alerts = pd.read_excel("354 drugs with RMs formation information.xls","alerts")

# create a dataframe to store the final search results
# index = drugs, columns = alerts
result = pd.DataFrame(np.random.randn(len(drugs.index),len(alerts.index)),
                      index = list(drugs.Name),
                      columns=list(alerts.Name))

# doing comparision
for i,drug in enumerate(drugs.InChI):
    m = Chem.MolFromInchi(drug)
    for j,alert in enumerate(alerts.SMARTS):
        n = Chem.MolFromSmarts(alert)
        result.iloc[i,j] = int(m.HasSubstructMatch(n))

# write the result to exist xlsx
# I cannot keep the exist sheet in original workbook
writer = pd.ExcelWriter("354 drugs with RMs formation information.xlsx",engine='xlsxwriter')
result.to_excel(writer,sheet_name="result")
alerts.to_excel(writer,sheet_name="alerts")
drugs.to_excel(writer,sheet_name="drugs")
writer.save()
