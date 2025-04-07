import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

tips = sns.load_dataset("tips")

st.title("Tips 데이터 대시보드")

option = st.selectbox("시각화 종류 선택", ["Matplotlib", "Seaborn", "Plotly"])

if option == "Matplotlib":
    st.subheader("Matplotlib 바 차트")
    fig, ax = plt.subplots()
    tips.groupby("day")["total_bill"].mean().plot(kind="bar", ax=ax)
    ax.set_title("요일별 평균 총액")
    st.pyplot(fig)

elif option == "Seaborn":
    st.subheader("Seaborn 산점도")
    sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time")
    st.pyplot()

elif option == "Plotly":
    st.subheader("Plotly Box Plot")
    fig = px.box(tips, x="day", y="total_bill", points="all")
    st.plotly_chart(fig)