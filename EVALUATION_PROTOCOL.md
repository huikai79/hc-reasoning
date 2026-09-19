# Evaluation Protocol

This document defines the minimum record for **future** comparative evaluations. It does not retroactively make historical evaluations reproducible.

## Purpose

Examples show how the skill may be used. Comparative evaluation asks a different question: whether a specific skill version improves a predefined task set under controlled conditions.

Do not use README examples as the primary evaluation set.

## Minimum comparison

For a material skill change, prefer paired runs with the same:

- task/case;
- model and reasoning mode when controllable;
- tool availability;
- attachment/source visibility;
- output requirement;
- execution window as close as practical.

At minimum compare:

- **baseline** — model without this skill;
- **candidate** — the exact skill/package version under review.

When useful, retain a previous released skill version as a third arm.

## Leakage control

Keep evaluation-only material outside the runtime skill:

- expected answer;
- known failure list;
- grader notes;
- preferred model/framework choice;
- gold terminology or hidden assumptions.

A case already used repeatedly to tune the skill is a development case, not a strong holdout.

## Run record

For each run record:

```text
case_id
case_version
skill_commit_sha
packaged_skill_hash (if applicable)
model
mode / reasoning effort
tool availability
run timestamp
run/repeat number
raw response
grader result
fatal failure (if any)
notes
```

If a variable cannot be controlled, record it rather than implying exact reproducibility.

## Evaluation dimensions

Use only dimensions that are defined before looking at candidate outputs. Typical dimensions include:

- task relevance/correctness;
- unsupported factual additions;
- assumption/inference separation;
- handling of missing information;
- useful alternatives or trade-offs;
- actionability;
- unnecessary verbosity;
- failure to follow explicit user constraints.

A skill-specific dimension is acceptable when it measures the purpose of the skill rather than rewarding its vocabulary.

## Hard failures

Treat these separately from aggregate preference:

- inventing decisive facts;
- silently converting missing evidence into a negative fact;
- materially changing the user's stated goal;
- unsafe or irreversible action without required authorization;
- using hidden evaluation guidance that leaked into the runtime context.

## Repeats and claims

One favorable generation is exploratory evidence only.

Do not claim a general improvement unless results remain favorable across multiple relevant cases/runs without a compensating increase in serious failures or task omissions.

If the result is mixed, publish the mixed result.

## Packaging check

Evaluate the version users actually install. The repository root and packaged plugin copies are validated for mirror drift in CI; record the commit used by the evaluation.

## Retention

Future evaluation artifacts should be stored in a dedicated evaluation-results location or external archive with:

- case-set version;
- date;
- exact skill commit;
- raw outputs;
- grading record;
- known contamination/holdout status.

Do not commit secrets or private user data as evaluation fixtures.
