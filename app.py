import streamlit as st
import random

# Funktion zur Erstellung eines zufälligen Rezepts
def generiere_rezept(zutaten):
    rezept_name = f"Besonderes Rezept mit {', '.join(zutaten)}"
    
    # Zubereitungsschritte
    anweisungen = [
        f"🔹 **Schritt 1:** Bereite die Zutaten vor: {', '.join(zutaten)}.",
        "🔹 **Schritt 2:** Erhitze eine Pfanne mit etwas Öl.",
        f"🔹 **Schritt 3:** Brate {random.choice(zutaten)} goldbraun an.",
        f"🔹 **Schritt 4:** Füge die restlichen Zutaten hinzu und gut umrühren.",
        "🔹 **Schritt 5:** Serviere das Gericht heiß und genieße es! 🍽️"
    ]
    
    # Zufällige Nährwerte
    naehrwerte = {
        "Kalorien": random.randint(200, 600),
        "Eiweiß": random.randint(10, 50),
        "Fett": random.randint(5, 30),
        "Kohlenhydrate": random.randint(10, 70)
    }
    
    return rezept_name, naehrwerte, anweisungen

# Streamlit UI
st.title("🥗 High-Protein Rezept-Generator für Sportler")
st.write("Gib die Zutaten ein, die du im Kühlschrank hast:")

# Eingabe der Zutaten
zutaten_input = st.text_input("🔍 Zutaten eingeben (durch Komma getrennt)")

if st.button("🔎 Rezept generieren"):
    if zutaten_input:
        zutaten_liste = [z.strip().lower() for z in zutaten_input.split(",")]
        
        # Generiere ein zufälliges Rezept basierend auf den eingegebenen Zutaten
        rezept_titel, naehrwerte, anweisungen = generiere_rezept(zutaten_liste)
        
        st.success(f"**{rezept_titel}**")
        st.write(f"🔥 **Nährwerte:** {naehrwerte}")

        st.subheader("📌 **Zubereitung:**")
        for schritt in anweisungen:
            st.write(schritt)
        
    else:
        st.warning("Bitte Zutaten eingeben, um ein Rezept zu generieren.")
