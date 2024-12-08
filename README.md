# Algorithm Selection and Auto-Tuning in AutoPas Seminar Paper

This repository contains my seminar paper and presentation materials for the `Seminar in Methods for Molecular Dynamics` course conducted at the Technical University of Munich (TUM). (!!TODO!! Short summary)

## Table of Contents

1. Introduction
2. AutoPas
    - Algorithm Library
    - Tunable Parameters
    - Auto-Tuning Framework
3. Benefits of Auto-Tuning
4. Drawbacks of Auto-Tuning
5. Early Stopping Optimization
    - Evaluation: Exploding Liquid Simulation
    - Analysis and Discussion
6. Comparison with Other MD Engines
    - GROMACS
    - LAMMPS
    - ls1 mardyn
7. Conclusion

## Abstract

Simulating molecular dynamics (MD) presents a significant computational challenge due to the vast number of particles involved in modern experiments. Naturally, researchers have put much effort into developing algorithms and frameworks that can efficiently simulate these systems. This paper focuses on the AutoPas framework, a modern particle simulation library that uses dynamic optimization techniques to achieve high performance in complex simulation scenarios. We compare AutoPas with other prominent MD engines, such as GROMACS, LAMMPS, and ls1 mardyn, and investigate a possible improvement to AutoPas' auto-tuning capabilities by introducing an early stopping mechanism aiming to reduce the overhead of parameter space exploration. Our evaluation shows that such a mechanism can reduce the total simulation time by up to 18.9\% in specific scenarios, demonstrating the potential of this improvement.

Index Terms: `molecular dynamics`, `auto-tuning`, `AutoPas`, `early-stopping`, `GROMACS`, `LAMMPS`, `ls1 mardyn`

## Paper

The seminar paper is available in LaTeX format in this repository. You can access the rendered version in PDF format by clicking the following link:

[Read the Seminar Paper (PDF)](latex/auto-tuning.pdf)

## Slides

The presentation slides are available in PDF format and can be accessed via the following link:

[View the Seminar Slides (PDF)](presentation/slides.pdf)
