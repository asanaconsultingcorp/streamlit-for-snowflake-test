
import json
import pandas as pd
import streamlit as st

indent = '  '

def getJson(df):
    """
    { "name": "KING",
      "children": [{
         "name": "BLAKE",
         "children": [
            { "name": "ALLEN" },
            { "name": "JAMES" },
            ...
        ]}]
    }
    """

    # collect all nodes
    nodes = {}
    for _, row in df.iterrows():
        name = row.iloc[2]
        nodes[name] = { "name": name }

    # move children under parents, and detect root
    root = None
    return root

df = pd.read_csv("data/employees.csv", header=0).convert_dtypes()

root = getJson(df)

