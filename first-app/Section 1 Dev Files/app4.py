import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import urllib.request
import json

def makeTreemap(labels, parents):
    data = go.Treemap(
        ids=labels,
        labels=labels,
        parents=parents,
        root_color="lightgray"
    )
    fig = go.Figure(data)
    return fig

def makeIcicle(labels, parents):        
    data = go.Icicle(
        ids=labels,
        labels=labels,
        parents=parents,
        root_color="lightgray"
    )
    fig = go.Figure(data)
    return fig

def makeSunburst(labels, parents):
    data = go.Sunburst(
        ids=labels,
        labels=labels,
        parents=parents,
        insidetextorientation='horizontal'
    )
    fig = go.Figure(data)
    return fig


def makeSankey(labels, parents):
    data = go.Sankey(
        node=dict(label=labels),
        link=dict(
            source=[list(labels).index(x) for x in labels],
            target=[-1 if pd.isna(x) else list(labels).index(x) for x in parents],
            label=labels,
            value=list(range(1, len(labels))))
        )
    fig = go.Figure(data)
    return fig

st.title("Hierarchical Data Viewer")

df = pd.read_csv("data/employees.csv", header=0).convert_dtypes()
#st.dataframe(df)

labels, parents=df[df.columns[0]], df[df.columns[1]]


#ORIGINAL METHOD FOR LAYOUT
#with st.expander("Treemap"):
#    fig = makeTreemap(labels, parents)
#    st.plotly_chart(fig, user_container_width=True)

#with st.expander("Icicle"):
#    fig = makeIcicle(labels, parents)
#    st.plotly_chart(fig, user_container_width=True)
    
#with st.expander("Sunburst"):
#    fig = makeSunburst(labels, parents)
#    st.plotly_chart(fig, user_container_width=True)

#with st.expander("Sankey"):
#    fig = makeSankey(labels, parents)
#    st.plotly_chart(fig, user_container_width=True)

#ALTERNATE SYNTAX 1
#exp1 = st.expander("Treemap"):
#fig = makeTreemap(labels, parents)
#exp1.plotly_chart(fig, user_container_width=True)

#exp2 = st.expander("Icicle")
#fig = makeIcicle(labels, parents)
#exp2.plotly_chart(fig, user_container_width=True)
    
#exp3 = st.expander("Sunburst"):
#fig = makeSunburst(labels, parents)
#exp3.plotly_chart(fig, user_container_width=True)

#exp4 = st.expander("Sankey"):
#fig = makeSankey(labels, parents)
#exp4.plotly_chart(fig, user_container_width=True)


#ALTERNATE SYNTAX 2 (Tab control)
tabs = st.tabs(["Treemap","Icicle","Sunburst","Sankey"])
#t1, t2, t3, t4 = st.tabs(["Treemap","Icicle","Sunburst","Sankey"])

with tabs[0]:
    fig = makeTreemap(labels, parents)
    st.plotly_chart(fig, user_container_width=True)

fig = makeIcicle(labels, parents)
tabs[1].plotly_chart(fig, user_container_width=True)

with tabs[2]:
    fig = makeSunburst(labels, parents)
    st.plotly_chart(fig, user_container_width=True)

fig = makeSankey(labels, parents)
tabs[3].plotly_chart(fig, user_container_width=True)


#cols = st.columns(3)
#cols[0].write("Column 1")
#cols[1].write("Column 2")
#cols[2].write("Column 3")

st.sidebar.selectbox("Select Box", ["S", "M"])