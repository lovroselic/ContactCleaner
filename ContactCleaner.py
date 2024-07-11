# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 11:44:09 2024

@author: lovro
"""

import pandas as pd

CNT = pd.read_csv("contacts.csv", low_memory=False)
CNT = CNT.dropna(subset=['E-mail 1 - Value'])
CNT = CNT[~CNT['E-mail 1 - Value'].str.contains(r'\.pl$', regex=True)]
CNT = CNT[~CNT['E-mail 1 - Value'].str.contains(r'\.org$', regex=True)]
CNT = CNT[~CNT['E-mail 1 - Value'].str.contains(r'\.hu$', regex=True)]
CNT = CNT[~CNT['E-mail 1 - Value'].str.contains(r'\.nl$', regex=True)]
CNT = CNT[~CNT['E-mail 1 - Value'].str.contains(r'\.fm$', regex=True)]
CNT = CNT[~CNT['E-mail 1 - Value'].str.contains(r'\.eu$', regex=True)]
CNT = CNT[~CNT['E-mail 1 - Value'].str.contains(r'\.net$', regex=True)]
CNT = CNT[~CNT['E-mail 1 - Value'].str.contains(r'\.arnes.si$', regex=True)]
CNT = CNT[~CNT['E-mail 1 - Value'].str.contains(r'\.info$', regex=True)]
CNT = CNT[~CNT['E-mail 1 - Value'].str.contains(r'^dir.', regex=True)]
CNT = CNT[~CNT['E-mail 1 - Value'].str.contains(r'^info.', regex=True)]
CNT = CNT[~CNT['E-mail 1 - Value'].str.contains(r'^admin.', regex=True)]
CNT = CNT[~CNT['E-mail 1 - Value'].str.contains(r'^obs.', regex=True)]
CNT = CNT[~CNT['E-mail 1 - Value'].str.contains(r'^sp.', regex=True)]
CNT = CNT[~CNT['E-mail 1 - Value'].str.contains(r'^suli.', regex=True)]
CNT = CNT[~CNT['E-mail 1 - Value'].str.contains(r'^sz.', regex=True)]
CNT = CNT[~CNT['E-mail 1 - Value'].str.contains(r'^sekretar.', regex=True)]
CNT = CNT[~CNT['E-mail 1 - Value'].str.contains(r'.skola.', regex=True)]
CNT = CNT[~CNT['E-mail 1 - Value'].str.contains(r'.szkol.', regex=True)]
CNT = CNT[~CNT['E-mail 1 - Value'].str.contains(r'.@os.', regex=True)]


TEST = CNT['E-mail 1 - Value']

CNT.to_csv('output.csv', index=False)
