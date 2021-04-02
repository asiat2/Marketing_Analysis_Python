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
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

############Loading the data set############
path_to_csv =("C:/Users/ashia/OneDrive - Data ScienceTech Institute/Python Lab DSTI/MyPythonProject/marketing_dash.csv")
df_m = pd.read_csv(path_to_csv)

#Default graph###########
#Histogram of Age by Customer_Age
bar1 = px.histogram(df_m,
                    x='Customer_Age',
                    y='Expenditure',
                    nbins=20,
                    labels=dict(Customer_Age='Customer_Age',
                    tip='Tip ($)',
                    Expenditure='Expenditure ($)'), 
                    title="Expenditure by Age",
                     height=400)


#Visualise Country by Income
groupped_country = df_m.groupby(by='Country',as_index=False).sum()
fig =px.bar(groupped_country,
                    x='Country',
                    y='Income',
                    orientation ='v',
                    labels=dict(Country='Country',
                    tip='Tip ($)',
                    Income='Income ($)'),
                    title="Income by Country",
                    height=400)
fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
fig.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})


##Visualise Country by Expenditure
groupped_country = df_m.groupby(by='Country',as_index=False).sum()
fig2 = px.bar(groupped_country,
                    x='Country',
                    y='Expenditure',
                    orientation ='v',
                    labels=dict(Country='Country',
                    tip='Tip ($)',
                    height=400,
                    Expenditure='Expenditure ($)'),
                    title="Expenditure by Country")
fig2.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
fig2.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})

#Expenditure by products
Mtnproduct=pd.DataFrame(df_m[[ 'MntWines', 'MntFruits',
                            'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts',
                            'MntGoldProds']].mean()*100, 
                           columns=['Percent']).reset_index()
Mtnproduct
fig3 = px.bar(Mtnproduct,
                        x='Percent',
                        y='index',
                        labels=dict(index='Different products',
                        percent='Expenditure'),
                        title="Expenditure by different products",
                         height=400)
fig3.update_layout(barmode='stack', yaxis={'categoryorder':'total descending'})

#Calculate success rate (percent accepted)
camp_success = pd.DataFrame(df_m[['AcceptedCmp1', 'AcceptedCmp2', 'AcceptedCmp3', 'AcceptedCmp4', 'AcceptedCmp5', 'Response']].mean()*100, 
                           columns=['Percent']).reset_index()

fig4 = px.bar(camp_success,
                        x='Percent',
                        y='index',
                        labels=dict(index='Campaign',
                        Percent='Accepted (%)'),
                        title="Marketing campaign success rate",
                        height=400)
fig4.update_layout(barmode='stack', yaxis={'categoryorder':'total descending'})

#Expenditure by Number of children in the household
df_m['Noofchildren'] = df_m['Noofchildren'].replace({0:'Zero',1:'One',2:'Two',3:'Three'})
fig5 = px.pie(df_m,names="Noofchildren",
                        hole=.3,
                        values="Expenditure", 
                        labels=dict(Income='Income ($)',
                        tip='Tip ($)',
                        TotalSpent='Expenditure ($)'),
                        title="Expenditure by number of children",
                        height=400)



#create the app
app = dash.Dash("MarketingDashboard", external_stylesheets=[dbc.themes.BOOTSTRAP])

#Generate a layout 
app.layout = html.Div(
        id="main_div",
        children=[
            dbc.Row(
                dbc.Col(
            html.H1(
            id="title",
            children="Marketing Analysis"

                ), width={"size": 10, "offset": 4}
            )
        ),

        dbc.Row(
              [
                dbc.Col(   
                    [
                    html.H3(id ="Edu",
                    children="Eduation"),
                 dcc.Dropdown(
                   id="edu2",
                   options=[
                    {'label': 'Graduation', 'value': 'Graduation'},
                    {'label': 'PhD', 'value': 'PhD '},
                    {'label': 'Master', 'value': 'Master'},
                    {'label': '2n Cycle', 'value': '2n Cycle '},
                    {'label': 'Basic', 'value': 'Basic'},
                ],
                    value=['Graduation','PhD','Master','2n Cycle','Basic'],
                    searchable=False
            )
        
            ],width=3,
          
            ),
               dbc.Col(   
                    [
                      html.H3(
                          id ="marital",
                    children="Marital_Status"),
            dcc.Dropdown(id="mar",
                   options=[
                    {'label': 'Married', 'value': 'Married'},
                    {'label': 'Together', 'value': 'Together'},
                    {'label': 'Single', 'value': 'Single'},
                    {'label': 'Divorced ', 'value': 'Divorced'},
                    {'label': 'Widow', 'value': 'Widow'},
                    {'label': 'Alone', 'value': 'Alone '},
                    {'label': 'YOLO', 'value': 'YOLO'},
                    {'label': 'Absurd', 'value': 'Absurd'}
                ],
                    value=['Married','Together','Single', 'Divorced','Widow','Alone','YOLO','Absurd'],
                    searchable=False
            )
            ],width=3,
            
        )
        ]
        ),
       dbc.Row(
            [
                dbc.Col(dcc.Graph(
                    id="Histogram",
                    figure=bar1,
                ),width=4,
                ),
                 dbc.Col(dcc.Graph(
                    id="bar_country_income",
                    figure=fig,
                ),width=4,
                ),
                dbc.Col(dcc.Graph(
                    id="bar_country_expenditure",
                    figure=fig2,
                ),width=4,  
                ),
            ]
        ),
       
         dbc.Row(
            [
                dbc.Col(dcc.Graph(
                    id="products",
                    figure=fig3,
                ),width=4,
                  
                ),
                dbc.Col(dcc.Graph(
                    id="camp",
                    figure=fig4,
                ),width=4,
                  
                ),
                 dbc.Col(dcc.Graph(
                    id="no_children",
                figure=fig5
                ),width=4,
        
                ),
                
             
            ]
        )
    ]
 )
@app.callback(
  
        [
          Output("Histogram","figure"),
          Output("bar_country_income","figure"),
          Output("bar_country_expenditure","figure"),
           Output("no_children","figure"),
          Output("products","figure"),
          Output("camp","figure"),
         
        ],
          [
         Input("mar","value"),
         Input("edu2","value")
        ]
        
)
def update_graphs(Marital,Education):
    temp_df =df_m[(df_m.Education.apply(lambda x :x in Education) ) | (df_m.Marital_Status.apply(lambda x :x in Marital) ) ]

    #Histogram of Age by Customer_Age
    bar1 = px.histogram(temp_df,
                        x='Customer_Age',
                        y='Expenditure',
                        nbins=20,
                        labels=dict(Customer_Age='Customer_Age',
                        tip='Tip ($)',
                        Expenditure='Expenditure ($)'),
                        title="Expenditure by Age",
                        height=400)


    #Visualise Country by Income
    groupped_country = temp_df.groupby(by='Country',as_index=False).sum()
    fig =px.bar(groupped_country,
                        x='Country',
                        y='Income',
                        orientation ='v',
                        labels=dict(Country='Country',
                        tip='Tip ($)',
                        Income='Income ($)'),
                        title="Income by Country",
                        height=400)
    fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
    fig.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})


    ##Visualise Country by Expenditure
    groupped_country = temp_df.groupby(by='Country',as_index=False).sum()
    fig2 = px.bar(groupped_country,
                        x='Country',
                        y='Expenditure',
                        orientation ='v',
                        labels=dict(Country='Country',tip='Tip ($)',
                        Expenditure='Expenditure ($)'), 
                        title="Expenditure by Country",
                        height=400)
    fig2.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
    fig2.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})

    #Expenditure by products
    Mtnproduct=pd.DataFrame(temp_df[[ 'MntWines', 'MntFruits',
                                'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts',
                                'MntGoldProds']].mean()*100, 
                            columns=['Percent']).reset_index()
    Mtnproduct
    fig3 = px.bar(Mtnproduct,
                        x='Percent',
                        y='index',
                        labels=dict(index='Different products',
                        percent='Expenditure'),
                        title="Expenditure by different products",
                        height=400)
    fig3.update_layout(barmode='stack', yaxis={'categoryorder':'total descending'})

    #Calculate success rate (percent accepted)
    camp_success = pd.DataFrame(temp_df[['AcceptedCmp1', 'AcceptedCmp2', 'AcceptedCmp3', 'AcceptedCmp4', 'AcceptedCmp5', 'Response']].mean()*100, 
                            columns=['Percent']).reset_index()

    fig4 = px.bar(camp_success,
                        x='Percent',
                        y='index',
                        labels=dict(index='Campaign',
                        Percent='Accepted (%)'),
                        title="Marketing campaign success rate",
                        height=400)
    fig4.update_layout(barmode='stack', yaxis={'categoryorder':'total descending'})

    #Expenditure by Number of children in the household
    df_m['Noofchildren'] = df_m['Noofchildren'].replace({0:'Zero',1:'One',2:'Two',3:'Three'})
    fig5 = px.pie(temp_df,names="Noofchildren",
                        hole=.3,
                        values="Expenditure", 
                        labels=dict(Income='Income ($)',
                        tip='Tip ($)',
                        TotalSpent='Expenditure ($)'),
                        title="Expenditure by number of children",
                        height=400)
    return[bar1,fig,fig2,fig3,fig4,fig5]

if __name__=="__main__":
     app.run_server(debug=False)