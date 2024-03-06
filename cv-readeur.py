from pdfminer.high_level import extract_text
import re

chemin_fichier = 'PDF/test2.pdf'


texte_cv = extract_text(chemin_fichier)

def extraire_informations(texte_cv):

    nom_match = re.search(r"^(.+)\nExpériences", texte_cv)
    nom = nom_match.group(1) if nom_match else None

    experiences_texte_match = re.search(r"Expériences(.+?)Formations", texte_cv, re.DOTALL)
    experiences_texte = experiences_texte_match.group(1) if experiences_texte_match else ""
    experiences = re.findall(r"(.+?)\s(\d{4} - \d{4})\n(.+?)\n(.+)", experiences_texte)

    formations_texte_match = re.search(r"Formations(.+?)Compétences", texte_cv, re.DOTALL)
    formations_texte = formations_texte_match.group(1) if formations_texte_match else ""
    formations = re.findall(r"(.+?)\s(\d{4} - \d{4})\n(.+)", formations_texte)

    competences_match = re.search(r"Compétences\n(.+?)Langues", texte_cv, re.DOTALL)
    competences = competences_match.group(1).split() if competences_match else []

    langues_match = re.search(r"Langues\n(.+?)Loisirs", texte_cv, re.DOTALL)
    langues = langues_match.group(1).split() if langues_match else []

    loisirs_match = re.search(r"Loisirs\n(.+?)Compétence", texte_cv, re.DOTALL)
    loisirs = loisirs_match.group(1).split() if loisirs_match else []

    telephone_match = re.search(r"(\d{3}-\d{3}-\d{4})", texte_cv)
    telephone = telephone_match.group(1) if telephone_match else None
    email_match = re.search(r"(\S+@\S+)", texte_cv)
    email = email_match.group(1) if email_match else None
    adresse_match = re.search(r"(\d+ .+ St., .+ City)", texte_cv)
    adresse = adresse_match.group(1) if adresse_match else None

    cv = {
        "Nom": nom,
        "Expériences": [
            {
                "Entreprise": exp[0],
                "Période": exp[1],
                "Poste": exp[2],
                "Missions": exp[3].split()
            } for exp in experiences
        ],
        "Formations": [
            {
                "Établissement": form[0],
                "Période": form[1],
                "Diplômes": form[2].split()
            } for form in formations
        ],
        "Compétences": competences,
        "Langues": langues,
        "Loisirs": loisirs,
        "Contact": {
            "Téléphone": telephone,
            "Email": email,
            "Adresse": adresse
        }
    }

    return cv

cv = extraire_informations(texte_cv)
print(cv)