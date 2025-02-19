import json, uuid
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from io import StringIO
import modules.graphs as graphs
import modules.formats as formats
import modules.charts as charts
import modules.animated as animated
import modules.utils as utils

st.set_page_config(layout="wide")
st.title("Hierarchical Data Viewer")
st.caption("Display your hierarchical data with charts and graphs.")

