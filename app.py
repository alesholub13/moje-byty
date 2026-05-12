import streamlit as st

# 1. Nastavení vzhledu aplikace
st.set_page_config(page_title="Správa majetku", page_icon="🏠")

# 2. Funkce pro kontrolu hesla
def check_password():
    if "password_correct" not in st.session_state:
        st.session_state["password_correct"] = False
    
    if not st.session_state["password_correct"]:
        st.title("🔐 Soukromý systém")
        heslo = st.text_input("Zadej přístupový kód", type="password")
        if heslo == "1234":
            st.session_state["password_correct"] = True
            st.rerun()
        elif heslo != "":
            st.error("Špatné heslo, zkus to znova.")
        return False
    return True

# 3. Hlavní obsah aplikace (spustí se jen po hesle)
if check_password():
    st.sidebar.title("🏠 Menu")
    volba = st.sidebar.selectbox("Co jdeme řešit?", 
        ["Přehled bytů", "Předávací protokol", "Auto (Arteon)", "Fotovoltaika"])

    if volba == "Přehled bytů":
        st.header("📊 Moje nemovitosti")
        st.info("Zde uvidíš výnosy a přehled nájemníků.")
        # Sem v budoucnu napojíme tvou Google tabulku

    elif volba == "Předávací protokol":
        st.header("📸 Stavy měřidel")
        byt = st.selectbox("Vyber byt", ["Byt Stará Ves", "Byt 2"])
        col1, col2 = st.columns(2)
        with col1:
            st.number_input("Elektřina (kWh)", step=1)
            st.number_input("Voda (m3)", step=1)
        with col2:
            st.number_input("Plyn (m3)", step=1)
            st.file_uploader("Vyfoť měřidlo", type=['jpg', 'png'])
        
        if st.button("Uložit data"):
            st.success("Uloženo!")

    elif volba == "Auto (Arteon)":
        st.header("🏎 VW Arteon Shooting Brake")
        st.write("Technické údaje a servisní deník.")
        st.text("Motor: 2.0 TDI 110 kW")
        st.date_input("Příští výměna oleje")

    elif volba == "Fotovoltaika":
        st.header("☀️ FVE & SolarXBox")
        st.write("Sledování přebytků do vody.")
        st.metric("Výkon panelů", "10 kWp")
