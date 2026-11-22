# Power-to-Methane (PtM) Process Simulation & ML-Driven Energy Optimisation

## Overview
Simulation data, heat integration work and Python machine-learning optimisation for a 10,000 Nm³/h Power-to-Methane plant, from the Graduation Project II at Bolu Abant İzzet Baysal University (team of 3; supervisors Prof. Turgay Pekdemir and Prof. Kadir Geliş).

## Process simulation
- Full plant model in **AVEVA Process Simulation** (Peng–Robinson): alkaline water electrolyser, direct air capture (DAC-TVSA) CO₂ supply, three-stage compression and four adiabatic methanation reactors, starting from the team's first Excel material balance.
- CO₂ capture unit modelled as a two-bed, three-layer TVSA (alumina, silica gel, amine-silica) with LDF kinetics, dual-site Langmuir isotherms and a non-isothermal energy balance; cyclic steady state after about 10 cycles, sizing the CO₂ supply at about 505 kmol/h (4:1 H₂:CO₂).

## Heat integration
- 14-exchanger network designed by pinch analysis (ΔTmin = 10 °C), using methanation and compressor waste heat for reactor feed preheating and DAC regeneration.

## Machine-learning optimisation
- 363-point dataset from AVEVA case studies, varying reactor recycle split, interstage cooling temperature and operating pressure.
- XGBoost surrogate model mapping these inputs to compressor work.
- **Result:** 25 bar with 80 °C interstage cooling cut compressor power from **12.11 MW to 11.71 MW (about 3 %)** at **98.5 % CH₄**.

## Safety finding
Some case-study points reached Reactor 1 outlet temperatures of **925–960 °C**, far above the **620 °C** catalyst limit. These were traced to the recycle-split setting, which shows the recycle loop needs tight control to keep the methanation exotherm within limits.

## Repository contents
- `data/`: case-study dataset exported from AVEVA Process Simulation.
- `src/`: Python scripts for data merging, the XGBoost model and the parameter study.
- `docs/`: supporting figures.
- `CWHEN*.pdf`, `Figure_6_*.png`: heat exchanger network and pinch analysis working figures from the project report.

---
**Project authors:** Mustafa Ali Yahya Adam | Elias | Mozan
