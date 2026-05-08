import streamlit as st
from rdkit import Chem
from rdkit.Chem import Descriptors, AllChem
import py3Dmol
from stmol import showmol

# Configuración de la página
st.set_page_config(page_title="3D Drug Explorer", page_icon="🧬", layout="wide")

st.title("🧬 Visualizador 3D de Fármacos y Regla de Lipinski")
st.markdown("""
Escribe el código **SMILES** de cualquier molécula. La aplicación calculará sus propiedades 
fisicoquímicas en tiempo real y renderizará su estructura tridimensional interactiva.
""")

# Input del usuario (Por defecto: Aspirina)
smiles_input = st.text_input("Introduce el SMILES de la molécula:", "CC(=O)OC1=CC=CC=C1C(=O)O")

try:
    # 1. Crear el objeto molécula desde el SMILES
    mol = Chem.MolFromSmiles(smiles_input)
    
    if mol:
        st.subheader("📊 Análisis de la Regla de Lipinski (Ro5)")
        st.markdown("Para ser un fármaco oral viable, debe cumplir idealmente estas métricas:")
        
        # Calcular propiedades
        mw = Descriptors.MolWt(mol)
        logp = Descriptors.MolLogP(mol)
        hbd = Descriptors.NumHDonors(mol)
        hba = Descriptors.NumHAcceptors(mol)
        
        # Mostrar métricas con colores si cumplen/no cumplen la regla
        col1, col2, col3, col4 = st.columns(4)
        
        col1.metric("Peso Molecular (≤ 500 Da)", f"{mw:.2f}", 
                    delta="Cumple" if mw <= 500 else "Alerta", delta_color="normal" if mw <= 500 else "inverse")
        
        col2.metric("Lipofilicidad (LogP ≤ 5)", f"{logp:.2f}", 
                    delta="Cumple" if logp <= 5 else "Alerta", delta_color="normal" if logp <= 5 else "inverse")
        
        col3.metric("Donadores H (≤ 5)", hbd, 
                    delta="Cumple" if hbd <= 5 else "Alerta", delta_color="normal" if hbd <= 5 else "inverse")
        
        col4.metric("Aceptores H (≤ 10)", hba, 
                    delta="Cumple" if hba <= 10 else "Alerta", delta_color="normal" if hba <= 10 else "inverse")

        st.divider()

        # 2. Renderizado 3D
        st.subheader("🧊 Estructura 3D Interactiva")
        st.info("💡 Puedes rotar la molécula con el ratón y hacer zoom con la rueda.")
        
        # Preparar la molécula para 3D (Añadir hidrógenos y calcular coordenadas)
        mol_3d = Chem.AddHs(mol)
        AllChem.EmbedMolecule(mol_3d, randomSeed=42)
        AllChem.MMFFOptimizeMolecule(mol_3d) # Optimización de geometría (Relajar la molécula)
        
        # Convertir a bloque MOL para el visor
        mol_block = Chem.MolToMolBlock(mol_3d)
        
        # Configurar py3Dmol
        view = py3Dmol.view(width=800, height=500)
        view.addModel(mol_block, "sdf")
        # Estilo visual: Palos (bonds) y Esferas pequeñas (átomos)
        view.setStyle({'stick': {'radius': 0.15}, 'sphere': {'radius': 0.4}})
        view.zoomTo()
        
        # Renderizar en Streamlit
        showmol(view, height=500, width=800)

    else:
        st.error("⚠️ El código SMILES introducido no es válido. Prueba con otro.")

except Exception as e:
    st.error(f"Hubo un error al procesar la molécula: {e}")

st.sidebar.title("Ejemplos interesantes:")
st.sidebar.code("CC(=O)OC1=CC=CC=C1C(=O)O\n# Aspirina", language="python")
st.sidebar.code("CN1C=NC2=C1C(=O)N(C(=O)N2C)C\n# Cafeína", language="python")
st.sidebar.code("CC12CCC3C(C1CCC2O)CCC4=CC(=O)CCC34C\n# Testosterona", language="python")