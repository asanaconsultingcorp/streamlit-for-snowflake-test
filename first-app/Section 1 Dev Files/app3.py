import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import urllib.request
import json

st.title("Hierarchical Data Viewer")

df = pd.read_csv("data/employees.csv", header=0).convert_dtypes()
#st.dataframe(df)

labels=df[df.columns[0]]
parents=df[df.columns[1]]

data = go.Treemap(
    ids=labels,
    labels=labels,
    parents=parents,
    root_color="lightgray"
)
fig = go.Figure(data)
st.plotly_chart(fig, use_container_width=True)

data = go.Icicle(
    ids=labels,
    labels=labels,
    parents=parents,
    root_color="lightgray"
)
fig = go.Figure(data)
st.plotly_chart(fig, use_container_width=True)

data = go.Sunburst(
    ids=labels,
    labels=labels,
    parents=parents,
    insidetextorientation='horizontal'
)
fig = go.Figure(data)
st.plotly_chart(fig, use_container_width=True)

data = go.Sankey(
    node=dict(label=labels),
    link=dict(
        source=[list(labels).index(x) for x in labels],
        target=[-1 if pd.isna(x) else list(labels).index(x) for x in labels],
        label=labels,
        value=list(range(1, len(labels))))
    )
fig = go.Figure(data)
st.plotly_chart(fig)


url = 'https://raw.githubusercontent.com/plotly/plotly.js/master/test/image/mocks/sankey_energy.json'
response = urllib.request.urlopen(url)
data = json.loads(response.read())

fig = go.Figure(data=[go.Sankey(
    valueformat = ".0f",
    valuesuffix = "TWh",
    node = dict(
      pad = 15,
      thickness = 15,
      line = dict(color = "black", width = 0.5),
      label =  data['data'][0]['node']['label'],
      color =  data['data'][0]['node']['color']
    ),
    link = dict(
      source =  data['data'][0]['link']['source'],
      target =  data['data'][0]['link']['target'],
      value =  data['data'][0]['link']['value'],
      label =  data['data'][0]['link']['label']
  ))])

fig.update_layout(
    hovermode = 'x',
    title=dict(text="Energy forecast for 2050<br>Source: Department of Energy & Climate Change, Tom Counsell via <a href='https://bost.ocks.org/mike/sankey/'>Mike Bostock</a>"),
    font=dict(size = 10, color = 'white'),
    plot_bgcolor='black',
    paper_bgcolor='black'
)
st.plotly_chart(fig)