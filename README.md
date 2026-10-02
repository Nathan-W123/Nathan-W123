<!--
  Profile README for github.com/Nathan-W123
  Put this file at README.md in a PUBLIC repo named exactly "Nathan-W123".
  Lines in HTML comments like this one don't render. Fill in or delete them before publishing.
-->

<h1 align="center">Nathan Ward</h1>

<p align="center">
  <b>Writing quantum chemistry code from scratch: integrals, SCF solvers, and the apps around them.</b>
  <br/>
  <!-- One line on who you are, e.g. "Chemistry @ University of X · interested in electronic structure & scientific computing" -->
</p>

<p align="center">
  <a href="https://github.com/Nathan-W123/HF-SCF-Engine"><b>HF-SCF-Engine</b></a>
  <!-- Add your links here, e.g.:
  · <a href="https://www.linkedin.com/in/YOUR-HANDLE"><b>LinkedIn</b></a>
  · <a href="mailto:YOUR-PUBLIC-EMAIL"><b>Email</b></a>
  · <a href="https://orcid.org/..."><b>ORCID</b></a> -->
</p>

---

## 👋 About me

I like knowing what's going on under the hood of computational chemistry. My Hartree–Fock engine doesn't wrap PySCF or Psi4: every integral, every Fock build, and every DIIS step is my own code in NumPy, SciPy, and Numba.

<!-- Optional 1–2 lines: what you're studying/working on, what you're looking for (internships, research positions, grad school), where you're based. -->

## 🔬 Featured project

### [HF-SCF-Engine](https://github.com/Nathan-W123/HF-SCF-Engine): a Hartree–Fock calculator written from scratch

A full-stack app. You enter a molecule and pick a basis set, and it returns the RHF energy, orbital energies, dipole moment, point group, and **interactive 3D molecular orbitals**.

- **Integrals by hand:** McMurchie–Davidson scheme with the Boys function: overlap, kinetic, nuclear attraction, and 4-centre ERIs, JIT-compiled with Numba
- **Scales past textbook size:** Cauchy–Schwarz screening, then **RI-JK density fitting** (def2-JKFIT) from 100 basis functions up
- **Robust convergence:** SAD initial guess, Pulay DIIS that resets and falls back to damping when it oscillates, and handling of near-linear dependence
- **Symmetry-aware:** point-group detection (C₂ᵥ, D₆ₕ, T_d, O_h, C∞ᵥ, …), SALC construction, and block-diagonalization
- **Basis sets:** STO-3G and 6-31G(\*\*) built in, plus cc-pVXZ and aug-cc-pVXZ from the Basis Set Exchange, and "calendar" sets (jul-, jun-, may-cc-pVXZ)
- **Validated:** the H₂O/cc-pVDZ RHF energy matches the reference value (−76.0268 Eₕ) to within 1 mEₕ, checked by a pytest test

<sub><b>Stack:</b> Python · NumPy · SciPy · Numba · FastAPI · SQLAlchemy · React · Tailwind CSS · 3Dmol.js · Docker · pytest</sub>

<!-- If you deploy it, add a live-demo link here. It's the single most convincing thing you can add. -->

## 🧭 What's next

<!-- Keep this honest and update it occasionally. If you won't maintain it, delete this section. Stale "currently working on" lines look worse than none. -->
- Open-shell systems (UHF)
- MP2 correlation energies
- Analytic gradients → geometry optimization

## 🛠️ Tools I use

<p>
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=py,fastapi,react,tailwind,docker,git,linux" alt="Python, FastAPI, React, Tailwind CSS, Docker, Git, Linux" />
  </a>
</p>

Scientific computing: **NumPy, SciPy, Numba**: vectorized linear algebra, JIT-compiled integral kernels, and eigensolvers.
