[繁體中文完整說明](README.zh-Hant.md)

# HC Reasoning

**An AI agent skill for checking whether a conclusion is actually supported by the evidence behind it.**

HC Reasoning helps users trace a conclusion backward: what the data supports, which assumptions are carrying the argument, whether the proposed solution addresses the actual problem, and what still needs to be checked before acting.

It is designed for practical situations such as reports, operational decisions, plans, and claims that look plausible but may skip important intermediate steps.

## What this project demonstrates

- Structured evidence checking instead of accepting a plausible conclusion at face value.
- Separation between observations, assumptions, alternative explanations, and decision-relevant unknowns.
- Problem-framing checks: whether the proposed action addresses the mechanism that could be causing the problem.
- Reusable agent instructions packaged as an installable skill.
- Worked examples that expose reasoning steps, limitations, and what additional evidence would change the conclusion.
- Cross-platform packaging for supported AI-agent environments.

## Design principle

A useful answer should make it easier to see:

**What is supported → what is inferred → what is still unknown → what to check next**

The skill does not guarantee that a conclusion is correct. It is a structured aid for inspecting support, gaps, and decision assumptions.

## Intellectual provenance

HC Reasoning is an independent adaptation inspired in part by Minerva University's historical descriptions of Habits of Mind and Foundational Concepts. It is not affiliated with or endorsed by Minerva University, and it does not reproduce Minerva's full curriculum.

See the [Traditional Chinese README](README.zh-Hant.md) and repository source/provenance documentation for the detailed scope and citations.

## Installation

For supported Claude, ChatGPT/Codex, and coding-agent installation routes, see the [full Traditional Chinese guide](README.zh-Hant.md#安裝).

For Skills CLI:

```sh
npx skills@latest add https://github.com/kcchien/hc-reasoning
```

## Example use

Ask the skill to review a report, proposed decision, or plan and identify:

1. what the available evidence can support;
2. which assumptions are necessary for the conclusion;
3. plausible alternative explanations;
4. what information would materially change the decision.

## License

[MIT](LICENSE)
