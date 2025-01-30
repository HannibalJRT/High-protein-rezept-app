import streamlit as st
import random

# Funktion zur Erstellung eines intelligenten Rezepts mit detaillierten Schritten und Kochzeiten
def generiere_rezept(zutaten):
    rezept_name = f"Besonderes Rezept mit {', '.join(zutaten)}"
    
    # Basierend auf den Zutaten berechnen wir eine realistische Zubereitungszeit
    vorbereitungszeit = random.randint(5, 15)  # Minuten für das Schneiden und Vorbereiten der Zutaten
    kochzeit = random.randint(10, 30)  # Minuten für das Kochen
    gesamtzeit = vorbereitungszeit + kochzeit  # Gesamtzeit der Zubereitung
    
    # Detaillierte Zubereitungsschritte mit Kochzeiten
    anweisungen = [
        f"🔹 **Schritt 1:** Sammle alle Zutaten: {', '.join(zutaten)}. Wasche und schneide das Gemüse nach Bedarf. *(Dauer: {vorbereitungszeit} Minuten)*",
        f"🔹 **Schritt 2:** Erhitze eine Pfanne mit einem Esslöffel Olivenöl auf mittlerer Hitze. *(Dauer: 2 Minuten)*",
        f"🔹 **Schritt 3:** Falls du Fleisch oder Fisch hast ({', '.join([z for z in zutaten if z in ['huhn', 'fisch', 'fleisch']])}), würze es mit Salz, Pfeffer und Gewürzen nach Geschmack.",
        f"🔹 **Schritt 4:** Brate das Protein ({', '.join([z for z in zutaten if z in ['huhn', 'fisch', 'fleisch']])}) für 5-7 Minuten pro Seite an, bis es goldbraun ist.",
        f"🔹 **Schritt 5:** Falls du Reis, Nudeln oder Quinoa hast ({', '.join([z for z in zutaten if z in ['reis', 'nudeln', 'quinoa']])}), koche sie gemäß den Anweisungen auf der Verpackung. *(Dauer: {random.randint(8, 15)} Minuten)*",
        f"🔹 **Schritt 6:** Füge das Gemüse ({', '.join([z for z in zutaten if z in ['brokkoli', 'paprika', 'karotten', 'zwiebeln', 'spinat']])}) in die Pfanne und brate es für weitere 3-5 Minuten an.",
        f"🔹 **Schritt 7:** Vermische alle Zutaten gut und serviere es heiß mit einer Prise Kräuter oder Nüsse für zusätzlichen Geschmack. 🌿🥜 *(Gesamtzeit: {gesamtzeit} Minuten)*",
        "🔹 **Schritt 8:** Guten Appetit! 🍽️"
    ]

    # Zufällige Nährwerte für eine realistische Berechnung
    naehrwerte = {
        "Kalorien": random.randint(300, 700),
        "Eiweiß": random.randint(20, 60),  # Gramm
        "Fett": random.randint(5, 25),  # Gramm
        "Kohlenhydrate": random.randint(30, 100),  # Gramm
        "Ballaststoffe": random.randint(5, 20),  # Gramm
        "Zucker": random.randint(2, 15),  # Gramm
        "Salz": round(random.uniform(0.5, 3), 1)  # Gramm
    }
    
    return rezept_name, naehrwerte, anweisungen, vorbereitungszeit, kochzeit, gesamtzeit

# Streamlit UI
st.title("🥗 High-Protein Rezept-Generator für Sportler")
st.write("Gib die Zutaten ein, die du im Kühlschrank hast:")

# Eingabe der Zutaten
zutaten_input = st.text_input("🔍 Zutaten eingeben (durch Komma getrennt)")

if st.button("🔎 Rezept generieren"):
    if zutaten_input:
        zutaten_liste = [z.strip().lower() for z in zutaten_input.split(",")]
        
        # Generiere ein zufälliges Rezept basierend auf den eingegebenen Zutaten
        rezept_titel, naehrwerte, anweisungen, vorbereitungszeit, kochzeit, gesamtzeit = generiere_rezept(zutaten_liste)
        
        st.success(f"**{rezept_titel}**")
        
        st.subheader("⏳ **Zubereitungszeit:**")
        st.write(f"🔪 **Vorbereitungszeit:** {vorbereitungszeit} Minuten")
        st.write(f"🔥 **Kochzeit:** {kochzeit} Minuten")
        st.write(f"⏱️ **Gesamtzeit:** {gesamtzeit} Minuten")

        st.subheader("🔥 **Nährwerte pro Portion:**")
        st.write(f"🍽️ **Kalorien:** {naehrwerte['Kalorien']} kcal")
        st.write(f"💪 **Eiweiß:** {naehrwerte['Eiweiß']} g")
        st.write(f"🛢️ **Fett:** {naehrwerte['Fett']} g")
        st.write(f"🍞 **Kohlenhydrate:** {naehrwerte['Kohlenhydrate']} g")
        st.write(f"🌱 **Ballaststoffe:** {naehrwerte['Ballaststoffe']} g")
        st.write(f"🍬 **Zucker:** {naehrwerte['Zucker']} g")
        st.write(f"🧂 **Salz:** {naehrwerte['Salz']} g")

        st.subheader("📌 **Zubereitung:**")
        for schritt in anweisungen:
            st.write(schritt)
        
    else:
        st.warning("Bitte Zutaten eingeben, um ein Rezept zu generieren.")
