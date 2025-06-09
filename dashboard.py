import pandas as pd
import dash 
from dash import Dash,dcc,html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go

app = Dash(__name__)
external_stylesheets = ["https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css"]
app = Dash(__name__, external_stylesheets=external_stylesheets,)

################### DATASET ####################################
df=pd.read_csv("DataHabitAcadamicPerm .csv")

#################### CHARTS #####################################
def tab1_layout():
    return html.Div([dcc.Graph(id='graph1')])

def tab2_layout():
    return html.Div([dcc.Graph(id='graph2')])

def tab3_layout():
    return html.Div([dcc.Graph(id='graph3')])

##################### APP LAYOUT ####################################
app.layout = html.Div([
        html.H1("Student Habit & Academic Dasboard", style={'textAlign':'Center'}),
        dcc.Tabs(id='tabs',value='tab1',
                children=[
                dcc.Tab(label='Study vs Exam Score',value='tab1'),
                dcc.Tab(label='Social Media vs Mental Health',value='tab2'),
                dcc.Tab(label='Sleep vs Attendance',value='tab3')
        ]),
             html.Div(id='tab-content')
        ])

##################### CALLBACKS ####################################
@app.callback(
    Output('tab-content', 'children'),
    Input('tabs', 'value')
)
def render_content(tab):
    if tab=='tab1':
        return tab1_layout()
    elif tab=='tab2':
        return tab2_layout()
    elif tab=='tab3':
        return tab3_layout()

@app.callback(
    Output('graph1', 'figure'),
    Input('tabs', 'value')
)
def update_graph1(tab):
    if tab=='tab1':
        return px.scatter(df, x='study_hours_per_day', y='exam_score',
                color='gender', trendline='ols',
                color_discrete_sequence=['#FF6361', '#58508D'],        
                title='Study Hours vs Exam Score')

@app.callback(
    Output('graph2', 'figure'),
    Input('tabs', 'value')
)
def update_graph2(tab):
   if tab=='tab2':
        return px.scatter(df, x='social_media_hours', y='mental_health_rating',
                     color='part_time_job', trendline='ols',color_discrete_sequence=['#2ca02c', '#d62728'],
                     title='Social Media vs Mental Health')
       
@app.callback(
    Output('graph3', 'figure'),
    Input('tabs', 'value')
)
def update_graph3(tab):
    if tab=='tab3':
        return px.scatter(df, x='sleep_hours', y='attendance_percentage',
                     color='diet_quality', trendline='ols',color_discrete_sequence=['#17becf', '#bcbd22', '#ff7f0e'],
                     title='Sleep Hours vs Attendance')
   
if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)