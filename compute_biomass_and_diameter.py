#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 15:15:44 2022

@author: edu
"""
###biomass 

import pandas as pd
import math
import numpy as np

sheet_url = "https://docs.google.com/spreadsheets/d/1LNcL_CcOi-dEYi-9GD9IP-7CqMW5jGxYjCD3dc-ha4c/edit#gid=814679296"
url_1 = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
dados = pd.read_csv(url_1)

def calc_perfilhos_diam(table, circ=None):
    area = math.pi/4*((pd.DataFrame([i.split('+') for i in table[table[circ].str.contains('\+')==True][circ]]).apply(pd.to_numeric)/math.pi)**2)
    diam = np.sqrt((4*area.sum(axis=1))/math.pi) 

    local=table.loc[dados[circ].str.contains('\+')==True,circ].index.to_list()
    table[circ]=pd.to_numeric(table[circ],errors = 'coerce')
    table.loc[local,circ] = diam.to_list()
    return table
     
def compute_biomass(table=None,d=None,h=None,col_name=None):
    #compute biomass for one column
    table[col_name]=0.0292*(table[d]*table[h])**1.6371
    return table
teste=calc_perfilhos_diam(dados,circ="d1")
teste=calc_perfilhos_diam(teste,circ="d2")
teste=calc_perfilhos_diam(teste,circ="d3")
teste=calc_perfilhos_diam(teste,circ="d4")

compute_biomass(teste,'d1','h1','biomass1')
compute_biomass(teste,'d2','h2','biomass2')
compute_biomass(teste,'d3','h3','biomass3')
compute_biomass(teste,'d4','h4','biomass4')

# dados[dados["d1"].str.contains('\+')==True]["d1"]



