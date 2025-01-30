import streamlit as st
import random

# Funktion zur Erstellung eines Rezepts basierend nur auf den eingegebenen Zutaten
def generiere_basis_rezept(zutaten):
    rezept_name = f"Original Rezept mit {', '.join(zutaten)}"
    
    vorbereitungszeit = random.randint(5, 15)
    kochzeit = random.randint(10, 30)
    gesamtzeit = vorbereitungszeit + kochzeit

    anweisungen = [
        f"🔹 **Schritt 1:** Bereite die Zutaten vor: {', '.join(zutaten)}. *(Dauer: {vorbereitungszeit} Minuten)*",
        "🔹 **Schritt 2:** Erhitze eine Pfanne mit Öl. *(Dauer: 2 Minuten)*",
        "🔹 **Schritt 3:** Falls Fleisch oder Gemüse vorhanden ist, brate es goldbraun an.",
        "🔹 **Schritt 4:** Falls du Nudeln oder Reis hast, koche sie gemäß den Anweisungen.",
        "🔹 **Schritt 5:** Vermische alle Zutaten und serviere es warm.",
        f"🔹 **Schritt 6:** Gesamtzeit: {gesamtzeit} Minuten. Guten Appetit! 🍽️"
    ]

    return rezept_name, anweisungen, vorbereitungszeit, kochzeit, gesamtzeit

# Funktion zur Erstellung eines verbesserten Rezepts mit Ersatz und Tipps
def generiere_verbessertes_rezept(zutaten):
    rezept_name = f"Verbessertes Rezept mit {', '.join(zutaten)}"

    vorbereitungszeit = random.randint(5, 15)
    kochzeit = random.randint(10, 30)
    gesamtzeit = vorbereitungszeit + kochzeit

    schwierigkeitsgrad = "Einfach" if gesamtzeit < 15 else "Mittel" if gesamtzeit <= 30 else "Schwierig"

    anweisungen = [
        f"🔹 **Schritt 1:** Bereite die Zutaten vor: {', '.join(zutaten)}. *(Dauer: {vorbereitungszeit} Minuten)*",
        "🔹 **Schritt 2:** Erhitze eine Pfanne mit Öl und brate das Protein an.",
        "🔹 **Schritt 3:** Falls Gemüse vorhanden ist, schneide es fein und gib es in die Pfanne.",
        "🔹 **Schritt 4:** Koche Beilagen wie Reis oder Nudeln, falls sie vorhanden sind.",
        "🔹 **Schritt 5:** Vermische alles und verfeinere das Gericht mit Kräutern oder Gewürzen.",
        f"🔹 **Schritt 6:** Gesamtzeit: {gesamtzeit} Minuten. Guten Appetit! 🍽️"
    ]

    return rezept_name, schwierigkeitsgrad, anweisungen, vorbereitungszeit, kochzeit, gesamtzeit

# Funktion für Tipps
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

        # Generiere Basis-Rezept (ohne Änderungen)
        basis_rezept_titel, basis_anweisungen, basis_vorbereitungszeit, basis_kochzeit, basis_gesamtzeit = generiere_basis_rezept(zutaten_liste)

        # Generiere verbessertes Rezept
        verbessert_rezept_titel, schwierigkeitsgrad, verbessert_anweisungen, verbessert_vorbereitungszeit, verbessert_kochzeit, verbessert_gesamtzeit = generiere_verbessertes_rezept(zutaten_liste)

        # Zeige Original-Rezept
        st.subheader("🍽️ **Original Rezept** (nur mit deinen Zutaten)")
        st.success(f"**{basis_rezept_titel}**")
        st.write(f"⏳ **Zubereitungszeit:** {basis_gesamtzeit} Minuten")
        st.subheader("📌 **Zubereitung:**")
        for schritt in basis_anweisungen:
            st.write(schritt)

        # Zeige Verbesserte Version
        st.subheader("✨ **Verbesserte Rezept-Version**")
        st.success(f"**{verbessert_rezept_titel}**")
        st.write(f"⭐ **Schwierigkeitsgrad:** {schwierigkeitsgrad}")
        st.write(f"⏳ **Zubereitungszeit:** {verbessert_gesamtzeit} Minuten")
        st.subheader("📌 **Zubereitung:**")
        for schritt in verbessert_anweisungen:
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
