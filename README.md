# Student-Relative Reliability Gating for Risk-Controlled Knowledge Distillation

Frozen benchmark artifact (v4) accompanying the manuscript
*Student-Relative Reliability Gating for Risk-Controlled Knowledge
Distillation in Engineering Time-Series Forecasting*, submitted to
**Results in Engineering** (Elsevier).

The artifact contains everything needed to audit and regenerate every
number, table, and figure in the paper: the pre-registered configuration
(frozen **2026-07-13T05:42:41 UTC**, before the confirmatory run), the
complete result files, the publication figures, the executed notebook, and
a SHA-256 manifest covering all result artifacts.

## What the study shows, in one paragraph

Knowledge distillation from an unreliable teacher degrades a deployed
forecaster (negative transfer). We qualify each candidate teacher against
the **standalone student** (not against naive persistence) on rolling
calibration origins, and drive a three-action policy (reject / attenuate /
accept) with an exact `g = 0` rejection state. On 6 public series x 3
strong students (DLinear, PatchTST, N-HiTS) x 3 teacher tiers (exact
statevector quantum, noisy-quantum surrogate, matched classical control),
all five pre-registered claims passed: hard student-relative rejection
produced zero observed negative transfer in 270 dataset-origin blocks, and
the soft gate is Holm-significantly protective in 14/18 cells with large
effects against unreliable teachers. Protection concentrates in the
rejection action; the intermediate attenuation band is reported as a
validated boundary, not as a success.

## Repository layout

```
.
|-- notebooks/            executed end-to-end benchmark notebook (v4)
|-- results/              all frozen result artifacts (CSV / JSON / NPZ)
|   |-- config_v4.json            pre-registered thresholds & hypotheses (frozen)
|   |-- v4_confirmatory_H1.csv    primary Wilcoxon+Holm tests
|   |-- v4_confirmatory_H2_H3.csv non-inferiority bounds
|   |-- v4_risk_endpoints.csv     NT rate, tail regret, benefit retention
|   |-- v4_risk_coverage.csv      risk-coverage frontier
|   |-- v4_sensitivity_DM.csv     Diebold-Mariano + ESS audit
|   |-- v4_runs.csv / v4_regret_* raw run-level records
|   |-- dataset_sources.json      source URLs + SHA-256 of the six datasets
|   `-- ...               legacy (v3) study artifacts, ablations, fidelity
|-- figures/              publication figures (PDF)
|-- scripts/
|   `-- verify_checksums.py       integrity gate against the manifest
|-- checksums_sha256.json SHA-256 manifest of all result artifacts
|-- requirements_freeze.txt       frozen Python environment (pip freeze)
`-- paper/                manuscript sources (added upon acceptance)
```

## Reproduce

**1. Verify artifact integrity** (no dependencies beyond Python 3):

```bash
python scripts/verify_checksums.py
```

**2. Re-derive every table and figure from the frozen CSVs.** Each table
in the paper names its source file (e.g., Table 5 -> `v4_risk_endpoints.csv`);
the notebook's Part IV and Part V cells regenerate all figures and the
programmatic claim verification from `results/` alone, without retraining.

**3. Full retraining** (optional, ~10 h on a single NVIDIA T4):

```bash
pip install -r requirements_freeze.txt
jupyter nbconvert --to notebook --execute \
  notebooks/student-relative-reliability-gating-for-risk-contr.ipynb
```

Set `RUN_MODE = "smoke"` in the configuration cell for a minutes-scale dry
run. Datasets are downloaded inside the notebook and checked against the
hashes in `results/dataset_sources.json`. The benchmark is checkpointed at
(dataset, origin, seed) granularity and resumes after interruption.

Environment used for the frozen run: Python 3.12.13, PyTorch 2.10.0+cu128,
NumPy 2.0.2, SciPy 1.16.3, pandas 2.3.3, Linux, single NVIDIA Tesla T4
(`results/environment.json`); total wall-clock 589 min.

## Pre-registration and honest reporting

`results/config_v4.json` freezes the hypotheses (H1-H4, S1), thresholds
(tau_reject = 0.5, tau_accept = 0.9), the non-inferiority margin (5%), the
divergence rule, and the experimental unit (dataset x origin blocks) with a
UTC timestamp prior to the confirmatory run.
`results/claims_check_v4.json` is the programmatic pass/fail verification.
Negative and boundary findings (classical-teacher attenuation band; legacy
C2 audit failure) are reported in the paper and reproducible from the same
files.

## License and citation

Code under the MIT License (see `LICENSE`); result data and figures under
CC-BY-4.0. Cite via `CITATION.cff`. A versioned release of this repository
is archived on Zenodo (DOI added upon reservation).
