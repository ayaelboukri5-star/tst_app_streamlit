import streamlit as st
 
 
 

# Titre de l'application
st.title("📚 Formulaire Étudiant")

# Informations de l'étudiant
nom = st.text_input("Nom")
prenom = st.text_input("Prénom")
age = st.number_input("Âge", min_value=10, max_value=100, step=1)

# Choix du genre
genre = st.radio(
    "Genre",
    ["Femme", "Homme"]
)

# Choix des matières
matieres = st.multiselect(
    "Choisissez vos matières préférées",
    ["Math", "Physique", "Informatique", "Français", "Anglais"]
)

# Niveau d'étude
niveau = st.selectbox(
    "Niveau d'étude",
    ["1ère année", "2ème année", "3ème année"]
)

# Zone de texte
commentaire = st.text_area("Commentaire")

# Bouton de validation
if st.button("Envoyer"):
    st.success("Formulaire envoyé avec succès !")

    st.write("### Informations saisies :")
    st.write(f"**Nom :** {nom}")
    st.write(f"**Prénom :** {prenom}")
    st
```
     