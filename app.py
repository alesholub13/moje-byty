import streamlit as st
import pandas as pd

# Nastavení stránky
st.set_page_config(page_title="Správa nemovitostí", layout="wide")

# Jednoduché heslo
def check_password():
    if "password_correct" not in st.session_state:
        st.session_state.password_correct = False
    
    if not st.session_state.password_correct:
        st.title("🔐 Vstup do systému")
        password = st.text_input("Zadejte přístupový kód", type="password")
        if st.button("Přihlásit se"):
            if password == "1234":
                st.session_state.password_correct = True
                st.rerun()
            else:
                st.error("❌ Špatné heslo")
        return False
    return True

if check_password():
    st.sidebar.title("🏠 Menu nemovitostí")
    choice = st.sidebar.radio("Kam chcete jít?", ["Moje Byty", "Předávací protokol", "Kontakty & Správa"])

    if choice == "Moje Byty":
        st.title("📂 Přehled nemovitostí")
        
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Byt 57m² (Cihla)")
            st.info("Aktuální stav: V rekonstrukci")
            st.write("- Hotová nivelačka\n- Rozpracovaná elektřina\n- Plánování kuchyně")
        
        with col2:
            st.subheader("Náklady na rekonstrukci")
            st.number_input("Materiál (Kč)", value=0)
            st.number_input("Práce (Kč)", value=0)

    elif choice == "Předávací protokol":
        st.title("📝 Předávací protokol měřidel")
        st.write("Zapište aktuální stavy při předání nebo kontrole bytu.")
        
        with st.form("protokol"):
            datum = st.date_input("Datum odečtu")
            elektřina = st.text_input("Elektřina (stav v kWh)")
            voda = st.text_input("Voda (stav v m³)")
            plyn = st.text_input("Plyn (stav v m³)")
            st.form_submit_button("Uložit stavy")

    elif choice == "Kontakty & Správa":
        st.title("📞 Důležité kontakty")
        st.write("- **Havarijní služba:** 123 456 789")
        st.write("- **Elektrikář:** Jan Novák (777 888 999)")
        st.write("- **Správce objektu:** Pan Svoboda")
