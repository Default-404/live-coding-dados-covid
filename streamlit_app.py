import pandas as pd
import plotly.express as px
import streamlit as st

#READ DATASET
df = pd.read_csv("https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv")

#CHANGE COLUMNS NAMES
df = df.rename(columns = {"date": "Data", "newCases": "Novos casos", "newDeaths": "Novos óbitos", "totalCases_per_100k_inhabitants": "Casos por 100 mil habitantes", "deaths_per_100k_inhabitants": "Óbitos por 100 mil habitantes"})

#SET STATE SELECTION
listStates = list(df["state"].unique())
listStates.sort()
listStates.remove("TOTAL")
listStates.insert(0, "TOTAL")
state = st.sidebar.selectbox("Qual estado?", listStates)
df = df[df["state"] == state]

#SET COLUMN SELECTION
listColumns = ["Novos casos", "Novos óbitos", "Casos por 100 mil habitantes", "Óbitos por 100 mil habitantes"]
column = st.sidebar.selectbox("Qual tipo de informação?", listColumns)

#BUILD GRAPH
fig = px.line(df, x = "Data", y = column, title = column + " - " + state)
fig.update_layout(xaxis_title = "DATA", yaxis_title = column.upper(), title = {"x": 0.5})

#SET PAGE STRUCTURE
st.title("DADOS COVID - BRASIL")
st.write("Nessa aplicação, o usuário tem a opção de escolher o estado e o tipo de informação mostrada no gráfico. Utilize o menu lateral para selecioná-los.")

st.plotly_chart(fig, use_container_width = True)

st.caption("Os dados foram obtidos a partir do site: https://github.com/wcota/covid19br.")