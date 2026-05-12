import streamlit as st

# --- JEDNODUCHÉ HESLO ---
def check_password():
    if "password_correct" not in st.session_state:
        st.session_state["password_correct"] = False
    if not st.session_state["password_correct"]:
        heslo = st.text_input("Zadej heslo", type="password")
        if heslo == "1234": # Tady je tvoje heslo, pak si ho změníme
            st.session_state["password_correct"] = True
            st.rerun()
        return False
    return True

if check_password():
    st.title("🏠 Správa mých bytů")
    menu = ["Přehled", "Nahrát foto/metry", "Opravy a náklady"]
    volba = st.sidebar.selectbox("Menu", menu)

    if volba == "Přehled":
        st.write("Tady bude tvůj seznam bytů a výpočty výnosů.")
    
    if volba == "Nahrát foto/metry":
        st.header("📸 Stav měřidel a dokumenty")
        st.number_input("Elektřina (kWh)")
        st.file_uploader("Vyfoť měřidlo nebo smlouvu")
        if st.button("Uložit"):
            st.success("Uloženo!")
