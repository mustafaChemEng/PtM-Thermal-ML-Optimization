# Power-to-Methane (PtM) Process Simulation & ML-Driven Energy Optimization

## Overview
This repository contains the simulation data, thermal integration analysis, and Python-based machine learning optimization for a 10,000 $Nm^3/h$ integrated Power-to-Methane (PtM) facility. The project bridges classical chemical process design with modern data science to minimize utility consumption and mechanical power requirements.

## Core Process Engineering Achievements
*   **Process Simulation:** Developed a rigorous steady-state model of an alkaline water electrolyzer, a direct air capture (DAC-TVSA) unit, and a four-stage adiabatic methanation reactor train using **AVEVA Process Simulation**.
*   **Thermal Autarky:** Synthesized a 14-exchanger network using the Composite Weighted Heat Exchanger Network (CWHEN) algorithm and Pinch Analysis ($\Delta T_{min} = 10^\circ\text{C}$). 
*   **Utility Reduction:** Recovered 67.28 MW of internal process heat, completely eliminating the need for external heating utilities (0 MW external hot utility).

## Machine Learning Optimization
To optimize the remaining mechanical energy penalty without violating catalyst temperature constraints ($<620^\circ\text{C}$), a surrogate model was built using **Python and XGBoost**.
*   Generated a 363-point thermodynamic dataset by varying reactor recycle split fractions, interstage cooling temperatures, and operating pressures.
*   Deployed an XGBoost Regressor to map the non-linear relationships between the process inputs and the compressor work/cooling duties.
*   **Result:** Reduced continuous compressor load to **11.71 MW** and cooling duty to **110.4 MW** by shifting the global optimum to 25 bar and $80^\circ\text{C}$ interstage cooling, while safely maintaining 98.47% pipeline-grade methane purity.

## Repository Contents
*   `data/`: Raw thermodynamic datasets exported from AVEVA APS case studies.
*   `src/`: Python scripts for data merging, XGBoost model training, and parameter optimization.
*   `docs/`: Process Flow Diagrams (PFD) and Grand Composite Curves.

---
**Project Authors:** Mustafa Ali Yahya Adam | Elias | Mozan