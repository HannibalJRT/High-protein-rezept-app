import streamlit as st
import random

# Funktion zur Erstellung eines intelligenten Rezepts mit Schwierigkeitsgrad, Kochzeit und Tipps
def generiere_rezept(zutaten):
    rezept_name = f"Besonderes Rezept mit {', '.join(zutaten)}"
    
    # Berechnung der Zubereitungszeit
    vorbereitungszeit = random.randint(5, 15)  # Minuten für das Schneiden und Vorbereiten
    kochzeit = random.randint(10, 30)  # Minuten für das Kochen
    gesamtzeit = vorbereitungszeit + kochzeit  # Gesamtzeit

    # Berechnung der Schwierigkeit
    if gesamtzeit < 15:
        schwierigkeitsgrad = "Einfach"
    elif 15 <= gesamtzeit <= 30:
        schwierigkeitsgrad = "Mittel"
    else:
        schwierigkeitsgrad = "Schwierig"

    # Detaillierte Zubereitungsschritte
    anweisungen = [
        f"🔹 **Schritt 1:** Sammle alle Zutaten: {', '.join(zutaten)}. Wasche und schneide das Gemüse nach Bedarf. *(Dauer: {vorbereitungszeit} Minuten)*",
        f"🔹 **Schritt 2:** Erhitze eine Pfanne mit etwas Öl. *(Dauer: 2 Minuten)*",
        f"🔹 **Schritt 3:** Falls du Fleisch oder Fisch hast, würze es mit Salz, Pfeffer und Gewürzen.",
        f"🔹 **Schritt 4:** Brate das Protein ({', '.join([z for z in zutaten if z in ['huhn', 'fisch', 'fleisch']])}) für 5-7 Minuten pro Seite an.",
        f"🔹 **Schritt 5:** Falls du Reis oder Nudeln hast, koche sie für {random.randint(8, 15)} Minuten.",
        f"🔹 **Schritt 6:** Füge das Gemüse hinzu und brate es für weitere 3-5 Minuten.",
        f"🔹 **Schritt 7:** Mische alles zusammen und serviere es. *(Gesamtzeit: {gesamtzeit} Minuten)*",
        "🔹 **Schritt 8:** Guten Appetit! 🍽️"
    ]

    return rezept_name, schwierigkeitsgrad, anweisungen, vorbereitungszeit, kochzeit, gesamtzeit

# Funktion für Koch-Tipps
def generiere_tipps():
    tipps = [
        "🌿 Füge frische Kräuter hinzu für mehr Geschmack!",
        "🧄 Ein bisschen Knoblauch kann dein Gericht noch aromatischer machen.",
        "🔥 Ein Spritzer Zitrone oder Essig hebt den Geschmack hervor!",
        "🌶️ Magst du es scharf? Füge etwas Chili oder Paprika hinzu.",
        "🥑 Ein paar Nüsse oder Avocado machen dein Essen noch besser!"
    ]
    return random.choice(tipps)

# Funktion für Ersatz-Zutaten
def ersatz_zutat(zutat):
    ersatz = {
        "milch": "Mandelmilch oder Sojamilch",
        "butter": "Olivenöl oder Kokosöl",
        "zucker": "Honig oder Ahornsirup",
        "reis": "Quinoa oder Couscous",
        "fleisch": "Tofu oder Pilze",
        "nudeln": "Zucchini-Nudeln oder Vollkornnudeln"
    }
    return ersatz.get(zutat, None)

# Streamlit UI
st.title("🥗 High-Protein Rezept-Generator für Sportler")
st.write("Gib die Zutaten ein, die du im Kühlschrank hast:")

# Eingabe der Zutaten
zutaten_input = st.text_input("🔍 Zutaten eingeben (durch Komma getrennt)")

if st.button("🔎 Rezept generieren"):
    if zutaten_input:
        zutaten_liste = [z.strip().lower() for z in zutaten_input.split(",")]
        rezept_titel, schwierigkeitsgrad, anweisungen, vorbereitungszeit, kochzeit, gesamtzeit = generiere_rezept(zutaten_liste)

        st.success(f"**{rezept_titel}**")
        
        # Zubereitungszeiten anzeigen
        st.subheader("⏳ **Zubereitungszeit:**")
        st.write(f"🔪 **Vorbereitungszeit:** {vorbereitungszeit} Minuten")
        st.write(f"🔥 **Kochzeit:** {kochzeit} Minuten")
        st.write(f"⏱️ **Gesamtzeit:** {gesamtzeit} Minuten")

        # Schwierigkeitsgrad anzeigen
        st.subheader("⭐ **Schwierigkeitsgrad:**")
        st.write(f"🧑‍🍳 **{schwierigkeitsgrad}**")

        # Zubereitungsschritte anzeigen
        st.subheader("📌 **Zubereitung:**")
        for schritt in anweisungen:
            st.write(schritt)

        # Koch-Tipp anzeigen
        st.subheader("💡 **Koch-Tipp:**")
        st.write(generiere_tipps())

        # Ersatzmöglichkeiten anzeigen
        ersatzvorschläge = [f"🔄 Kein {z}? Versuche {ersatz_zutat(z)}!" for z in zutaten_liste if ersatz_zutat(z)]
        if ersatzvorschläge:
            st.subheader("🔄 **Ersatzmöglichkeiten:**")
            for vorschlag in ersatzvorschläge:
                st.write(vorschlag)
        
    else:
        st.warning("Bitte Zutaten eingeben, um ein Rezept zu generieren.")

