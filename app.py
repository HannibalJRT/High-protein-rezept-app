import streamlit as st
import random

# Funzione per generare una ricetta casuale
def generare_ricetta(ingredienti):
    titolo_ricetta = f"Ricetta speciale con {', '.join(ingredienti)}"
    
    # Passaggi generici per la preparazione
    passaggi = [
        f"🔹 **Passaggio 1:** Prepara gli ingredienti: {', '.join(ingredienti)}.",
        "🔹 **Passaggio 2:** Riscalda una padella con un filo d'olio.",
        f"🔹 **Passaggio 3:** Cuoci {random.choice(ingredienti)} fino a doratura.",
        f"🔹 **Passaggio 4:** Aggiungi gli altri ingredienti e mescola bene.",
        "🔹 **Passaggio 5:** Servi caldo e buon appetito! 🍽️"
    ]
    
    # Valori nutrizionali casuali
    nutrizione = {
        "Kalorien": random.randint(200, 600),
        "Eiweiß": random.randint(10, 50),
        "Fett": random.randint(5, 30),
        "Kohlenhydrate": random.randint(10, 70)
    }
    
    return titolo_ricetta, nutrizione, passaggi

# UI di Streamlit
st.title("🥗 High Protein Rezept-Generator für Sportler")
st.write("Gib die Zutaten ein, die du im Kühlschrank hast:")

# Input per gli ingredienti
zutaten_input = st.text_input("🔍 Zutaten eingeben (getrennt durch Komma)")

if st.button("🔎 Rezept generieren"):
    if zutaten_input:
        zutaten_liste = [z.strip().lower() for z in zutaten_input.split(",")]
        
        # Genera una ricetta casuale con gli ingredienti forniti
        titel, naehrwerte, anweisungen = generare_ricetta(zutaten_liste)
        
        st.success(f"**{titel}**")
        st.write(f"🔥 **Nährwerte:** {naehrwerte}")

        st.subheader("📌 **Zubereitung:**")
        for schritt in anweisungen:
            st.write(schritt)
    else:
        st.warning("Bitte Zutaten eingeben, um ein Rezept zu generieren.")

