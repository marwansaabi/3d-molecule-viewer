# 🧬 3D Interactive Molecule Viewer & Lipinski Analyzer

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](TU_URL_DE_STREAMLIT_AQUI)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![RDKit](https://img.shields.io/badge/RDKit-Cheminformatics-green.svg)](https://www.rdkit.org/)

A web-based cheminformatics application that transforms SMILES strings into interactive 3D molecular structures and evaluates their drug-likeness in real-time. 

Designed for researchers and data scientists in the Drug Discovery and HealthTech space, this tool provides instant structural visualization and physicochemical property analysis.

## 🚀 Live Demo
**[Click here to open the 3D Viewer](TU_URL_DE_STREAMLIT_AQUI)**

## ✨ Key Features
- **SMILES to 3D Generation:** Automatically calculates 3D coordinates, adds hydrogens, and optimizes molecular geometry using MMFF (Merck Molecular Force Field).
- **Interactive 3D Rendering:** Rotate, zoom, and explore molecular structures directly in the browser using `py3Dmol`.
- **Lipinski's Rule of 5 (Ro5) Analysis:** Real-time calculation and compliance alerts for:
  - Molecular Weight (≤ 500 Da)
  - Lipophilicity / LogP (≤ 5)
  - Hydrogen Bond Donors (≤ 5)
  - Hydrogen Bond Acceptors (≤ 10)

## 🛠️ Tech Stack
- **Frontend/UI:** [Streamlit](https://streamlit.io/)
- **Cheminformatics Engine:** [RDKit](https://www.rdkit.org/)
- **3D Visualization:** `py3Dmol` & `stmol`

## 📥 Local Installation
Want to run this locally on your machine?

```bash
# 1. Clone the repository
git clone [https://github.com/marwansaabi/3d-molecule-viewer.git](https://github.com/marwansaabi/3d-molecule-viewer.git)
cd 3d-molecule-viewer

# 2. Install required dependencies
pip install -r requirements.txt

# 3. Launch the Streamlit app
streamlit run app.py
