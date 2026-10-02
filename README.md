<div align="center">

<img width="100%" alt="Nathan Ward: computational chemistry and molecular spectroscopy" src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customGradientList=0,0,0,0|25,0,212,255,0.5|50,0,255,200,0.5|75,157,123,255,0.5|100,0,0,0,1&height=260&section=header&text=Nathan%20Ward&fontAlignY=34&fontSize=70&fontColor=ffffff&stroke=00d4ff&strokeWidth=1.2&animation=fadeIn&desc=COMPUTATIONAL%20CHEMISTRY%20%E2%80%A2%20ROTATIONAL%20SPECTROSCOPY%20%E2%80%A2%20SCIENTIFIC%20SOFTWARE&descAlignY=58&descSize=14&descColor=00ffc8" />

<a href="https://github.com/DenverCoder1/readme-typing-svg">
  <img alt="Molecular structure from microwave spectra. Spectroscopy meets quantum chemistry. Writing electronic-structure code from scratch." src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=700&size=22&duration=2800&pause=700&color=00D4FF&center=true&vCenter=true&width=700&lines=Molecular+structure+from+microwave+spectra;Spectroscopy+%C3%97+quantum+chemistry;Writing+electronic-structure+code+from+scratch;If+the+data+can't+see+it%2C+let+theory+decide" />
</a>

<br>

<img alt="Focus: rotational spectroscopy" src="https://img.shields.io/badge/FOCUS-Rotational_Spectroscopy-000000?style=for-the-badge&logo=moleculer&logoColor=00d4ff" />
<img alt="Field: quantum chemistry" src="https://img.shields.io/badge/FIELD-Quantum_Chemistry-000000?style=for-the-badge&logo=electron&logoColor=00ffc8" />
<img alt="Builds: scientific software" src="https://img.shields.io/badge/BUILDS-Scientific_Software-000000?style=for-the-badge&logo=python&logoColor=9d7bff" />

</div>

<br>

<img width="100%" alt="" src="https://capsule-render.vercel.app/api?type=rectangles&color=00d4ff&height=4&section=header&text=&fontSize=0" />

<h2 align="center">ABOUT</h2>

<table>
<tr>
<td width="50%" valign="top">

I write software at the boundary of **experiment and theory**. Spectroscopists measure rotational constants, and quantum chemists compute potential energy surfaces. My work is getting the two to agree on what a molecule actually looks like.

That means working down to the numbers: Jacobians, null spaces, vibration-rotation corrections, and the integrals underneath an SCF calculation.

<!-- Optional: add a line about where you study/work and what you're looking for. -->

</td>
<td width="50%" align="center" valign="middle">

<img alt="Primary: geometry inversion" src="https://img.shields.io/badge/PRIMARY-Geometry_Inversion-000000?style=for-the-badge&logo=python&logoColor=00d4ff" />
<br>
<img alt="Secondary: electronic structure" src="https://img.shields.io/badge/SECONDARY-Electronic_Structure-000000?style=for-the-badge&logo=electron&logoColor=00ffc8" />
<br>
<img alt="Method: SVD plus Newton" src="https://img.shields.io/badge/METHOD-SVD_%2B_Newton-000000?style=for-the-badge&logo=numpy&logoColor=9d7bff" />
<br>
<img alt="Motto: validate against experiment" src="https://img.shields.io/badge/MOTTO-Validate_Against_Experiment-000000?style=for-the-badge&logo=checkmarx&logoColor=00d4ff" />

</td>
</tr>
</table>

<img width="100%" alt="" src="https://capsule-render.vercel.app/api?type=rectangles&color=00ffc8&height=4&section=header&text=&fontSize=0" />

<h2 align="center">FEATURED: <a href="https://github.com/Nathan-W123/Quantize">QUANTIZE</a></h2>

<p align="center"><b>Hybrid molecular geometry inversion from rotational spectroscopy and quantum chemistry.</b></p>

<p align="center">
Quantize estimates bond lengths and angles from isotopologue rotational constants. It still works when the spectra alone<br>
<i>can't</i> pin down the structure: SVD splits the problem into what the data can see and what it can't, and the quantum chemistry fills in the rest.
</p>

<table>
<tr>
<td width="20%" align="center" valign="top">

### 01

<img alt="Observe" src="https://img.shields.io/badge/OBSERVE-000000?style=for-the-badge&logo=databricks&logoColor=00d4ff" />
<br><sub>A, B, C rotational constants from one or more isotopologues</sub>

</td>
<td width="20%" align="center" valign="top">

### 02

<img alt="Correct" src="https://img.shields.io/badge/CORRECT-000000?style=for-the-badge&logo=wolframmathematica&logoColor=00ffc8" />
<br><sub>B₀ → Bₑ: vibrational (harmonic + Coriolis + cubic anharmonic), electronic g-tensor, and BOB terms</sub>

</td>
<td width="20%" align="center" valign="top">

### 03

<img alt="Decompose" src="https://img.shields.io/badge/DECOMPOSE-000000?style=for-the-badge&logo=numpy&logoColor=9d7bff" />
<br><sub>Stack the spectral Jacobians and use SVD to split range space from null space</sub>

</td>
<td width="20%" align="center" valign="top">

### 04

<img alt="Fill in" src="https://img.shields.io/badge/FILL_IN-000000?style=for-the-badge&logo=electron&logoColor=00d4ff" />
<br><sub>A damped Newton step on the Psi4 / ORCA energy surface, applied only where the data can't see</sub>

</td>
<td width="20%" align="center" valign="top">

### 05

<img alt="Quantify" src="https://img.shields.io/badge/QUANTIFY-000000?style=for-the-badge&logo=plotly&logoColor=00ffc8" />
<br><sub>Bootstrap + MCMC uncertainty, Kraitchman r<sub>s</sub> coordinates, and auto-generated reports</sub>

</td>
</tr>
</table>

<div align="center">

| Fluorobenzene, 8 isotopologues | RMS bond error |
|:--|--:|
| Quantum chemistry alone | 11.4 mÅ |
| Spectroscopy alone | 8.2 mÅ |
| **Quantize hybrid** | **4.0 mÅ** |

<sub>Self-consistent isotopologue set vs. the published structure. Measured-data benchmarks (vinyl fluoride, acetyl fluoride, fluoroethane), along with their caveats, are in the <a href="https://github.com/Nathan-W123/Quantize">repo README</a>.</sub>

</div>

- **Validated physics:** with the cubic anharmonic term, the vibration-rotation constant α for CO reproduces the Dunham/Pekeris value to **0.1%**, tested against published CO and H₂O constants.
- **Torsion / large-amplitude motion:** RAM-lite torsion-rotation Hamiltonian, C₃ A/E tunnelling splittings, line intensities, and joint level + rotational-constant fitting.
- **Engineering:** config-driven CLI (`validate` / `run` / `report` / `uncertainty`), parallel multistart, Bayesian hyperparameter tuning, a large pytest suite, and benchmarks in GitHub Actions.

<img width="100%" alt="" src="https://capsule-render.vercel.app/api?type=rectangles&color=9d7bff&height=4&section=header&text=&fontSize=0" />

<h2 align="center">ALSO BUILT</h2>

<table>
<tr>
<td width="100%" valign="top">

### [HF-SCF-Engine](https://github.com/Nathan-W123/HF-SCF-Engine)

A Hartree–Fock calculator written from scratch, with no PySCF underneath. It uses McMurchie–Davidson integrals JIT-compiled with Numba, RI-JK density fitting, DIIS, point-group symmetry, and cc-pVXZ / aug-cc-pVXZ basis sets. Molecular orbitals are shown in 3D in a React + FastAPI web app.

<img alt="Python" src="https://img.shields.io/badge/Python-000000?style=flat-square&logo=python&logoColor=00d4ff" />
<img alt="Numba" src="https://img.shields.io/badge/Numba-000000?style=flat-square&logo=numba&logoColor=00ffc8" />
<img alt="FastAPI" src="https://img.shields.io/badge/FastAPI-000000?style=flat-square&logo=fastapi&logoColor=00ffc8" />
<img alt="React" src="https://img.shields.io/badge/React-000000?style=flat-square&logo=react&logoColor=00d4ff" />

</td>
</tr>
</table>

<img width="100%" alt="" src="https://capsule-render.vercel.app/api?type=rectangles&color=00d4ff&height=4&section=header&text=&fontSize=0" />

<h2 align="center">TOOLKIT</h2>

<h3 align="center">Quantum Chemistry</h3>

<div align="center">

![Psi4](https://img.shields.io/badge/Psi4-000000?style=flat-square&logo=electron&logoColor=00d4ff)
![ORCA](https://img.shields.io/badge/ORCA-000000?style=flat-square&logo=electron&logoColor=00ffc8)
![PySCF](https://img.shields.io/badge/PySCF-000000?style=flat-square&logo=python&logoColor=9d7bff)
![Basis Set Exchange](https://img.shields.io/badge/Basis_Set_Exchange-000000?style=flat-square&logo=databricks&logoColor=00d4ff)
![3Dmol.js](https://img.shields.io/badge/3Dmol.js-000000?style=flat-square&logo=javascript&logoColor=00ffc8)

</div>

<h3 align="center">Scientific Computing</h3>

<div align="center">

![Python](https://img.shields.io/badge/Python-000000?style=flat-square&logo=python&logoColor=00d4ff)
![NumPy](https://img.shields.io/badge/NumPy-000000?style=flat-square&logo=numpy&logoColor=00ffc8)
![SciPy](https://img.shields.io/badge/SciPy-000000?style=flat-square&logo=scipy&logoColor=9d7bff)
![Numba](https://img.shields.io/badge/Numba-000000?style=flat-square&logo=numba&logoColor=00d4ff)
![scikit-optimize](https://img.shields.io/badge/scikit--optimize-000000?style=flat-square&logo=scikitlearn&logoColor=00ffc8)
![Matplotlib](https://img.shields.io/badge/Matplotlib-000000?style=flat-square&logo=python&logoColor=9d7bff)

</div>

<h3 align="center">Apps & Engineering</h3>

<div align="center">

![FastAPI](https://img.shields.io/badge/FastAPI-000000?style=flat-square&logo=fastapi&logoColor=00ffc8)
![React](https://img.shields.io/badge/React-000000?style=flat-square&logo=react&logoColor=00d4ff)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-000000?style=flat-square&logo=tailwindcss&logoColor=00d4ff)
![Streamlit](https://img.shields.io/badge/Streamlit-000000?style=flat-square&logo=streamlit&logoColor=9d7bff)
![SQLite](https://img.shields.io/badge/SQLite-000000?style=flat-square&logo=sqlite&logoColor=00d4ff)
![Docker](https://img.shields.io/badge/Docker-000000?style=flat-square&logo=docker&logoColor=00d4ff)
![pytest](https://img.shields.io/badge/pytest-000000?style=flat-square&logo=pytest&logoColor=00ffc8)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-000000?style=flat-square&logo=githubactions&logoColor=9d7bff)
![Git](https://img.shields.io/badge/Git-000000?style=flat-square&logo=git&logoColor=00d4ff)

</div>

<img width="100%" alt="" src="https://capsule-render.vercel.app/api?type=rectangles&color=00ffc8&height=4&section=header&text=&fontSize=0" />

<h2 align="center">GITHUB STATS</h2>

<div align="center">

<img height="170" alt="Nathan's GitHub stats" src="https://github-stats-extended.vercel.app/api?username=Nathan-W123&show_icons=true&hide_border=true&bg_color=000000&title_color=00d4ff&icon_color=00ffc8&text_color=c9d1d9&disable_animations=true" />
<img height="170" alt="Nathan's most used languages" src="https://github-stats-extended.vercel.app/api/top-langs/?username=Nathan-W123&layout=compact&hide_border=true&bg_color=000000&title_color=00d4ff&text_color=c9d1d9&langs_count=6&disable_animations=true" />

</div>

<img width="100%" alt="" src="https://capsule-render.vercel.app/api?type=rectangles&color=9d7bff&height=4&section=header&text=&fontSize=0" />

<h2 align="center">CONNECT</h2>

<div align="center">

[![GitHub](https://img.shields.io/badge/GITHUB-Nathan--W123-000000?style=for-the-badge&logo=github&logoColor=ffffff)](https://github.com/Nathan-W123)
<!-- Uncomment and fill in:
[![LinkedIn](https://img.shields.io/badge/LINKEDIN-YOUR--HANDLE-000000?style=for-the-badge&logo=linkedin&logoColor=00d4ff)](https://www.linkedin.com/in/YOUR-HANDLE)
[![Email](https://img.shields.io/badge/EMAIL-YOUR--EMAIL-000000?style=for-the-badge&logo=gmail&logoColor=00ffc8)](mailto:YOUR-EMAIL)
[![ORCID](https://img.shields.io/badge/ORCID-0000--0000--0000--0000-000000?style=for-the-badge&logo=orcid&logoColor=9d7bff)](https://orcid.org/0000-0000-0000-0000)
-->

</div>

<br>

<img width="100%" alt="" src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customGradientList=0,0,0,0|25,157,123,255,0.5|50,0,255,200,0.5|75,0,212,255,0.5|100,0,0,0,1&height=150&section=footer&reversal=true&text=Measure%20%E2%80%A2%20Compute%20%E2%80%A2%20Reconcile&fontSize=18&fontColor=ffffff&animation=fadeIn" />
