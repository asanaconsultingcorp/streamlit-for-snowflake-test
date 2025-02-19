import streamlit as st

st.title("Hierarchical Data Viewer")

st.header("this is a header")
st.subheader("subheader")
st.caption("caption")
st.write("this is write")
st.text("field text")
st.code("v = variable()\nv_another_call()", "python")
st.markdown("**bold**")
st.markdown("*italic*")

st.divider()


st.latex("...")
st.error("this is error")
st.info("this is info")
st.warning("this is warning")
st.success("this is success")
st.toast("this is toast")

st.balloons()
st.snow()

