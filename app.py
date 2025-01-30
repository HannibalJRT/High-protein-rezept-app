
import streamlit as st

# Titolo dell'app
st.title("🥗 High Protein Rezept-Generator für Sportler")

st.write("Gib die Zutaten ein, die du im Kühlschrank hast:")

# Dizionario con ricette ad alto contenuto proteico
rezepte = {
    "Hähnchenbrust mit Gemüse": {
        "zutaten": ["hähnchenbrust", "brokkoli", "öl", "salz", "pfeffer"],
        "nährwerte": {"Kalorien": 400, "Eiweiß": 35, "Fett": 15, "Kohlenhydrate": 5},
        "zubereitungszeit": "30 Minuten",
        "schwierigkeit": "Mittel",
        "kategorie": "Proteinaufbau",
        "anweisungen": [
            "🔹 **Schritt 1:** Die Hähnchenbrust mit Salz und Pfeffer würzen.",
            "🔹 **Schritt 2:** Erhitze etwas Öl in einer Pfanne und brate die Hähnchenbrust goldbraun an.",
            "🔹 **Schritt 3:** Brokkoli in kleine Röschen schneiden und in einem separaten Topf mit Wasser kochen.",
            "🔹 **Schritt 4:** Die Hähnchenbrust im Ofen bei 180°C für 15 Minuten backen.",
            "🔹 **Schritt 5:** Mit dem Brokkoli servieren. Perfekt für den Muskelaufbau! 🏋️‍♂️"
        ]
    },
    "Proteinshake": {
        "zutaten": ["milch", "proteinpulver", "banane", "mandeln"],
        "nährwerte": {"Kalorien": 300, "Eiweiß": 25, "Fett": 10, "Kohlenhydrate": 35},
        "zubereitungszeit": "5 Minuten",
        "schwierigkeit": "Einfach",
        "kategorie": "Proteinaufbau",
        "anweisungen": [
            "🔹 **Schritt 1:** Banane in Stücke schneiden.",
            "🔹 **Schritt 2:** Alle Zutaten in einen Mixer geben.",
            "🔹 **Schritt 3:** Mixe die Zutaten bis sie cremig sind.",
            "🔹 **Schritt 4:** In ein Glas gießen und direkt nach dem Training genießen! 🥤"
        ]
    }
}

# Campo di input per gli ingredienti
zutaten_input = st.text_input("🔍 Zutaten eingeben (getrennt durch Komma)")

if st.button("🔎 Rezept suchen"):
    if zutaten_input:
        zutaten_liste = [z.strip().lower() for z in zutaten_input.split(",")]
        
        bestes_rezept = None
        max_zutaten_treffer = 0
        
        for rezept_name, details in rezepte.items():
            zutaten_match = len(set(zutaten_liste) & set(details["zutaten"]))
            
            if zutaten_match > max_zutaten_treffer:
                max_zutaten_treffer = zutaten_match
                bestes_rezept = rezept_name
        
        if bestes_rezept:
            details = rezepte[bestes_rezept]
            st.success(f"**Das beste Rezept für dich:** {bestes_rezept}")
            st.write(f"⏳ **Zubereitungszeit:** {details['zubereitungszeit']}")
            st.write(f"⭐ **Schwierigkeit:** {details['schwierigkeit']}")
            st.write(f"🔥 **Nährwerte:** {details['nährwerte']}")
            st.write(f"💪 **Kategorie:** {details['kategorie']}")
            
            st.subheader("📌 **Zubereitung:**")
            for schritt in details["anweisungen"]:
                st.write(schritt)
        else:
            st.warning("❌ Kein passendes Rezept gefunden. Versuche andere Zutaten!")
    else:
        st.warning("Bitte Zutaten eingeben, um ein Rezept zu finden.")
