import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import text2emotion as te
st.markdown('<style>body{background-color: Blue;}</style>',unsafe_allow_html=True)
st.title("Emotion Prediction")
txt = st.text_input('Enter Your Text')

if txt!='':
    dat=te.get_emotion(txt)
    st.write(dat)

    fig=go.Figure(data=[go.Pie(labels=list(dat.keys()),values=list(dat.values()))])

    st.plotly_chart(fig)

