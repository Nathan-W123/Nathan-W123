<div align="center">

<img width="100%" alt="Nathan Ward: computational chemistry and molecular spectroscopy" src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customGradientList=0,0,0,0|25,0,212,255,0.5|50,0,255,200,0.5|75,157,123,255,0.5|100,0,0,0,1&height=260&section=header&text=Nathan%20Ward&fontAlignY=34&fontSize=70&fontColor=ffffff&stroke=00d4ff&strokeWidth=1.2&animation=fadeIn&desc=COMPUTATIONAL%20CHEMISTRY%20%E2%80%A2%20ROTATIONAL%20SPECTROSCOPY%20%E2%80%A2%20SCIENTIFIC%20SOFTWARE&descAlignY=58&descSize=14&descColor=00ffc8" />

<samp>
  <a href="https://nateward.me/#/">site</a> ·
  <a href="https://github.com/Nathan-W123/Quantize">quantize</a> ·
  <a href="https://github.com/Nathan-W123/HF-SCF-Engine">hf-scf-engine</a> ·
  <a href="https://github.com/Nathan-W123?tab=repositories">repos</a> ·
  <a href="mailto:ncward@ucdavis.edu">email</a> ·
  <a href="https://github.com/Nathan-W123/Nathan-W123/issues">ask me anything</a>
</samp>

<br><br>

<img alt="Focus: rotational spectroscopy" src="https://img.shields.io/badge/FOCUS-Rotational_Spectroscopy-000000?style=for-the-badge&logoColor=00d4ff" />
<img alt="Field: quantum chemistry" src="https://img.shields.io/badge/FIELD-Quantum_Chemistry-000000?style=for-the-badge&logoColor=00ffc8" />
<img alt="Builds: scientific software" src="https://img.shields.io/badge/BUILDS-Scientific_Software-000000?style=for-the-badge&logo=python&logoColor=9d7bff" />

</div>

I do quantum research at **UC Davis** and write scientific software in my spare time.

I work at the boundary of **experiment and theory**. Spectroscopists measure rotational constants; quantum chemists compute potential energy surfaces. My work is getting the two to agree on what a molecule actually looks like — which means working down to the numbers: Jacobians, null spaces, vibration-rotation corrections, and the integrals underneath an SCF calculation.

- 🔬 &nbsp;I built **[Quantize](https://github.com/Nathan-W123/Quantize)**, which recovers molecular geometries that spectra alone can't pin down — **4.0 mÅ** RMS bond error vs. 11.4 mÅ for quantum chemistry on its own.
- ⚛️ &nbsp;I wrote **[HF-SCF-Engine](https://github.com/Nathan-W123/HF-SCF-Engine)**, a Hartree–Fock calculator built from scratch, with no PySCF underneath.
- 📐 &nbsp;Ask me about rotational spectroscopy, electronic structure, SVD-regularised inverse problems, or making numerical code fast.
- 💬 &nbsp;Reach me at **[ncward@ucdavis.edu](mailto:ncward@ucdavis.edu)**, or just [open an issue](https://github.com/Nathan-W123/Nathan-W123/issues).

---

<table><tr><td valign="top" width="50%">

### Recent releases
<!-- releases starts -->
[Kumi v0.5.17](https://github.com/Nathan-W123/Kumi/releases/tag/desktop-v0.5.17) - 2026-09-04

[Kumi v0.5.16](https://github.com/Nathan-W123/Kumi/releases/tag/desktop-v0.5.16) - 2026-09-04
<!-- releases ends -->
</td><td valign="top" width="50%">

### Recently pushed
<!-- pushed starts -->
**[Website](https://github.com/Nathan-W123/Website)** - 2026-11-09

**[SASD-HFML-Project](https://github.com/Nathan-W123/SASD-HFML-Project)** - 2026-11-06<br><sub>Repo to automate the SASD high frequency mainline frequency changes, mapping, and queries</sub>

**[springback-precomp](https://github.com/Nathan-W123/springback-precomp)** - 2026-10-24

**[Quantize](https://github.com/Nathan-W123/Quantize)** - 2026-10-23

**[CFD-ML](https://github.com/Nathan-W123/CFD-ML)** - 2026-10-22

**[autocal-lite-](https://github.com/Nathan-W123/autocal-lite-)** - 2026-10-20
<!-- pushed ends -->
</td></tr></table>

<sub>
<!-- updated starts -->
Updated automatically on 2026-11-09.
<!-- updated ends -->
&mdash; <a href="https://github.com/Nathan-W123/Nathan-W123/blob/main/.github/workflows/build-readme.yml">how this works</a>.
</sub>
<a href="https://github.com/Nathan-W123/Nathan-W123/actions/workflows/build-readme.yml"><img align="right" alt="Build README" src="https://github.com/Nathan-W123/Nathan-W123/actions/workflows/build-readme.yml/badge.svg" /></a>

---

## Quantize &nbsp;<a href="https://github.com/Nathan-W123/Quantize"><img alt="Last commit" src="https://img.shields.io/github/last-commit/Nathan-W123/Quantize?style=flat-square&labelColor=000000&color=00d4ff&label=last%20commit" /></a>

**Hybrid molecular geometry inversion from rotational spectroscopy and quantum chemistry.**

Quantize estimates bond lengths and angles from isotopologue rotational constants, and it still works when the spectra alone *can't* pin down the structure: SVD splits the problem into what the data can see and what it can't, then quantum chemistry fills in the rest.

**The result** — fluorobenzene, 8 isotopologues, RMS bond error against the published structure:

| Method | RMS bond error |
|:--|--:|
| Quantum chemistry alone | 11.4 mÅ |
| Spectroscopy alone | 8.2 mÅ |
| **Quantize hybrid** | **4.0 mÅ** |

<sub>Self-consistent isotopologue set. Measured-data benchmarks (vinyl fluoride, acetyl fluoride, fluoroethane), along with their caveats, are in the <a href="https://github.com/Nathan-W123/Quantize">repo README</a>.</sub>

**How it gets there:**

| | Step | What happens |
|:--|:--|:--|
| **01** | Observe | A, B, C rotational constants from one or more isotopologues |
| **02** | Correct | B₀ → Bₑ: vibrational (harmonic + Coriolis + cubic anharmonic), electronic g-tensor, and BOB terms |
| **03** | Decompose | Stack the spectral Jacobians, then SVD to split range space from null space |
| **04** | Fill in | A damped Newton step on the Psi4 / ORCA energy surface, applied only where the data can't see |
| **05** | Quantify | Bootstrap + MCMC uncertainty, Kraitchman r<sub>s</sub> coordinates, auto-generated reports |

- **Validated physics:** with the cubic anharmonic term, the vibration-rotation constant α for CO reproduces the Dunham/Pekeris value to **0.1%**, tested against published CO and H₂O constants.
- **Torsion / large-amplitude motion:** RAM-lite torsion-rotation Hamiltonian, C₃ A/E tunnelling splittings, line intensities, and joint level + rotational-constant fitting.
- **Engineering:** config-driven CLI (`validate` / `run` / `report` / `uncertainty`), parallel multistart, Bayesian hyperparameter tuning, a large pytest suite, and benchmarks in GitHub Actions.

---

## Also built

**[HF-SCF-Engine](https://github.com/Nathan-W123/HF-SCF-Engine)** &nbsp;<a href="https://github.com/Nathan-W123/HF-SCF-Engine"><img alt="Last commit" src="https://img.shields.io/github/last-commit/Nathan-W123/HF-SCF-Engine?style=flat-square&labelColor=000000&color=00ffc8&label=last%20commit" /></a>
<br>A Hartree–Fock calculator written from scratch, with no PySCF underneath — McMurchie–Davidson integrals JIT-compiled with Numba, RI-JK density fitting, DIIS, point-group symmetry, and cc-pVXZ / aug-cc-pVXZ basis sets. Molecular orbitals render in 3D in a React + FastAPI web app.

---

## Toolkit

**Quantum chemistry** &nbsp;
![Psi4](https://img.shields.io/badge/Psi4-000000?style=flat-square&logoColor=00d4ff)
![ORCA](https://img.shields.io/badge/ORCA-000000?style=flat-square&logoColor=00ffc8)
![PySCF](https://img.shields.io/badge/PySCF-000000?style=flat-square&logo=python&logoColor=9d7bff)
&nbsp;·&nbsp; Basis Set Exchange, 3Dmol.js

**Scientific computing** &nbsp;
![Python](https://img.shields.io/badge/Python-000000?style=flat-square&logo=python&logoColor=00d4ff)
![NumPy](https://img.shields.io/badge/NumPy-000000?style=flat-square&logo=numpy&logoColor=00ffc8)
![SciPy](https://img.shields.io/badge/SciPy-000000?style=flat-square&logo=scipy&logoColor=9d7bff)
![Numba](https://img.shields.io/badge/Numba-000000?style=flat-square&logo=numba&logoColor=00d4ff)
&nbsp;·&nbsp; scikit-optimize, Matplotlib

**Apps & engineering** &nbsp;
![FastAPI](https://img.shields.io/badge/FastAPI-000000?style=flat-square&logo=fastapi&logoColor=00ffc8)
![React](https://img.shields.io/badge/React-000000?style=flat-square&logo=react&logoColor=00d4ff)
![Docker](https://img.shields.io/badge/Docker-000000?style=flat-square&logo=docker&logoColor=9d7bff)
&nbsp;·&nbsp; Tailwind, Streamlit, SQLite, pytest, GitHub Actions, Git

---

## Elsewhere

- **Site** — [nateward.me](https://nateward.me/#/)
- **Email** — [ncward@ucdavis.edu](mailto:ncward@ucdavis.edu)
- **GitHub** — [@Nathan-W123](https://github.com/Nathan-W123) (you are here)
