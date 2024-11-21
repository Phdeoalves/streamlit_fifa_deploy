import streamlit as st

st.set_page_config(
    page_title="Players",
    layout="wide"
)

df_data = st.session_state["data"]

clubes = df_data["Club"].value_counts().index #Cria a lista de nomes únicos dos clubes do df e a nomeia como clubes
club = st.sidebar.selectbox("Clube", clubes) #Cria o selectbox no sidebar com a lista clubes e a nomeia como Clube

df_players = df_data[(df_data["Club"] == club)] #Filtra o df dos jogadores do Club = a do selectbox
players = df_players["Name"].value_counts().index #Faz o mesmo que clubes, mas com os nomes dos jogadores
player = st.sidebar.selectbox("Jogador", players)

df_player = df_players[(df_players["Name"] == player)]

st.image(df_player["Photo"].iloc[0])
st.title(df_player["Name"].iloc[0])

st.markdown(f"**Clube:** {df_player['Club'].iloc[0]}")
st.markdown(f"**Posição:** {df_player['Position'].iloc[0]}")

col1, col2, col3, col4 = st.columns(4)
col1.markdown(f"**Idade:** {df_player['Age'].iloc[0]}")
col2.markdown(f"**Altura:** {df_player['Height(cm.)'].iloc[0]/100}")
col3.markdown(f"**Peso:** {df_player['Weight(lbs.)'].iloc[0]*0.453:.2f}")
st.divider()

st.subheader(f"Overall {df_player['Overall'].iloc[0]}")
st.progress(int(df_player["Overall"].iloc[0]))

col1, col2, col3, col4 = st.columns(4)
col1.metric(label="Valor de Mercado", value=f"£ {df_player['Value(£)'].iloc[0]:,}")
col2.metric(label="Remuneração Semanal", value=f"£ {df_player['Wage(£)'].iloc[0]:,}")
col3.metric(label="Cláusula de Rescição", value=f"£ {df_player['Release Clause(£)'].iloc[0]:,}")

