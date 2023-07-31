import pandas as pd
import plotly.express as px
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

input_camila_file = "averageMileage-camila.csv"
input_eddie_file = "averageMileage-eduardo.csv"

#manual data per week for camila:
#data = [['Monday',20],['Tuesday',12],['Wednesday',33],['Thursday',15]]
#df = pd.DataFrame(data,columns=['Days','Miles'])

#manual data per week for eddie:
#data1 = [['Monday',25],['Tuesday',22],['Wednesday',30],['Thursday',20]]
#df1 = pd.DataFrame(data1,columns=['Days','Miles'])

#instead of manual data, a csv file was used
df1 = pd.read_csv(input_camila_file , usecols=["Week","Average number of miles"])
df2 = pd.read_csv(input_eddie_file , usecols=["Week","Average number of miles"])

#camila info
df3 = pd.read_csv(input_camila_file , usecols=["Days-Week 1","Miles-Week 1"])
df4 = pd.read_csv(input_camila_file , usecols=["Days-Week 2","Miles-Week 2"])
df5 = pd.read_csv(input_camila_file , usecols=["Days-Week 3","Miles-Week 3"])
df6 = pd.read_csv(input_camila_file , usecols=["Days-Week 4","Miles-Week 4"])

#eddie info
df7 = pd.read_csv(input_eddie_file , usecols=["Days-Week 1","Miles-Week 1"])
df8 = pd.read_csv(input_eddie_file , usecols=["Days-Week 2","Miles-Week 2"])
df9 = pd.read_csv(input_eddie_file , usecols=["Days-Week 3","Miles-Week 3"])
df0 = pd.read_csv(input_eddie_file , usecols=["Days-Week 4","Miles-Week 4"])

#both info -> removed bc idk how to do multi select yet
df_combined = df1.merge(df2, on='Week', suffixes=('_Camila', '_Eduardo')).melt(id_vars='Week', var_name='User', value_name='Average number of miles')

app.layout = html.Div(children=[html.H1(children='Mileage', style={'text-align': 'center'}),
    
    #graph1 = camila
    #graph2 = eddie

    html.Div([
        html.Label(['Choose a graph:'],style={'font-weight': 'bold'}),
        
        dcc.Dropdown(

            id='dropdown',

            options=[
                {'label': 'Camila', 'value': 'Camila'},
                {'label': 'Eduardo', 'value': 'Eduardo'},
                {'label': 'Both', 'value': 'Both'},
            ],

            value='Camila',
            style={"width": "50%"}),

    html.Div(dcc.Graph(id='averageGraph')),        
    ]),

    html.Div([
        html.Label(['Choose a week ~ Camila:'],style={'font-weight': 'bold'}),
        dcc.Dropdown(
            id="week-camila-dropdown", 
            
            options=[
                {'label': 'Week 1', 'value': 'Week 1'},
                {'label': 'Week 2', 'value': 'Week 2'},
                {'label': 'Week 3', 'value': 'Week 3'},
                {'label': 'Week 4', 'value': 'Week 4'},
            ],

            value='Week 1',
            style={"width": "50%"}),

    html.Div(dcc.Graph(id='camilaGraph')),        
    ]),
            
    html.Div([
        html.Label(['Choose a week ~ Eduardo:'],style={'font-weight': 'bold'}),
        dcc.Dropdown(
            id="week-eduardo-dropdown", 
            
            options=[
                {'label': 'Week 1', 'value': 'Week 1'},
                {'label': 'Week 2', 'value': 'Week 2'},
                {'label': 'Week 3', 'value': 'Week 3'},
                {'label': 'Week 4', 'value': 'Week 4'},
            ],

            value='Week 1',
            style={"width": "50%"}),

    html.Div(dcc.Graph(id='eduardoGraph')),        
    ]),
])

@app.callback(
    Output('averageGraph', 'figure'),
    [Input(component_id='dropdown', component_property='value')]
)

def select_graph(value): 
    #print(df1)
    #print(df2)
    if value == 'Camila':
        fig1 = px.line(df1, x=df1['Week'], y=df1['Average number of miles'])
        return fig1
    elif value == 'Eduardo':
        fig2 = px.line(df2, x=df2['Week'], y=df2['Average number of miles'])
        return fig2
    elif value == 'Both': # to create a figure with both lines
        fig10 = px.line(df_combined, x='Week', y='Average number of miles', color='User', title='Camila and Eduardo')
        return fig10

@app.callback(
    Output('camilaGraph', 'figure'),
    Input('week-camila-dropdown', 'value')
)
def update_camila_graph(camila_week_value):
    if camila_week_value == "Week 1":
        fig3 = px.bar(df3, x=df3['Days-Week 1'], y=df3['Miles-Week 1'])
        return fig3
    elif camila_week_value == "Week 2":
        fig4 = px.bar(df4, x=df4['Days-Week 2'], y=df4['Miles-Week 2'])
        return fig4
    elif camila_week_value == "Week 3":
        fig5 = px.bar(df5, x=df5['Days-Week 3'], y=df5['Miles-Week 3'])
        return fig5
    elif camila_week_value == "Week 4":
        fig6 = px.bar(df6, x=df6['Days-Week 4'], y=df6['Miles-Week 4'])
        return fig6
    # Return a default figure in case no conditions match
    return {}

@app.callback(
    Output('eduardoGraph', 'figure'),
    Input('week-eduardo-dropdown', 'value')
)

def update_eduardo_graph(eduardo_week_value):
    if eduardo_week_value == "Week 1":
        fig7 = px.bar(df7, x=df7['Days-Week 1'], y=df7['Miles-Week 1'])
        return fig7
    elif eduardo_week_value == "Week 2":
        fig8 = px.bar(df8, x=df8['Days-Week 2'], y=df8['Miles-Week 2'])
        return fig8
    elif eduardo_week_value == "Week 3":
        fig9 = px.bar(df9, x=df9['Days-Week 3'], y=df9['Miles-Week 3'])
        return fig9
    elif eduardo_week_value == "Week 4":
        fig0 = px.bar(df0, x=df0['Days-Week 4'], y=df0['Miles-Week 4'])
        return fig0
    return {}

if __name__ == '__main__':
    app.run_server(debug=True)


