# RHCA Evaluation Framework (Anonymous Submission)

This repository provides materials and a minimal runnable example for the RHCA evaluation framework.

## Overview

RHCA evaluates model behavior in multi-turn interactions using four dimensions:

* Reasoning Transparency (R)
* Helpfulness (H)
* Consistency (C)
* Context Alignment (A)

## Contents

* `scoring_rubric.txt` – evaluation criteria
* `example_scenarios.json` – sample multi-turn scenarios
* `run_evaluation.py` – simple script to load and evaluate scenarios
* `requirements.txt` – no external dependencies

## How to Run

```bash
python run_evaluation.py
```

## Reproducibility

This repository provides a simple, executable example of the RHCA framework.
It shows how scenarios and rubric can be used together for evaluation.

## Notes

* Anonymized for double-blind review
* Script is a minimal demonstration (not a full system)
