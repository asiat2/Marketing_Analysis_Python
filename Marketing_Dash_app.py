# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 14:02:50 2021

@author: ashia
"""
#########Loading the required library###############
import numpy as np
import plotly.graph_objects as go # creates plots
import pandas as pd # standard for data processing
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.offline as pyo
import plotly.express as px

############Loading the data set############
path_to_csv =("C:/Users/ashia/OneDrive - Data ScienceTech Institute/Python Lab DSTI/marketing.csv")
df_m = pd.read_csv(path_to_csv)