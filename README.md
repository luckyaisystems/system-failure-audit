# system-failure-audit

A deterministic logic engine for classifying failure modes across input, operator, and execution layers — inspired by PLC safety interlocks and AI-assisted decision systems.

![System Failure Audit Diagram](https://github.com/luckyaisystems/system-failure-audit/blob/main/Screenshot%202026-05-03%204.01.12%20PM.png)

## Failure Mode Classification Table

This table mirrors the structure used in industrial automation safety systems, where each layer isolates a different class of failure:

| Layer           | Failure Type     | Description                                                |
|-----------------|------------------|------------------------------------------------------------|
| Input Layer     | Model Error      | Bad, missing, corrupted, or out-of-range data             |
| Decision Layer  | Operator Error   | Bias, emotion, logic violation, or unsafe decision path   |
| Execution Layer | Execution Decay  | Timing failures, actuator breakdown, or incomplete execution |

This matches your polished diagram and gives the project a clean, readable reference.

## Code Description

The `failure_audit.py` script implements a deterministic 3-layer failure classifier:

- **Input Layer (Model Error)** — Detects bad or corrupted data  
- **Decision Layer (Operator Error)** — Detects bias, emotion, or logic violations  
- **Execution Layer (Execution Decay)** — Detects timing failures, actuator breakdowns, or incomplete execution  

This mirrors how PLCs perform:

- Input validation  
- Logic scan cycles  
- Output execution checks  

It is the same structure used in industrial automation, safety interlocks, and AI decision-audit systems.

## Example Output

```text
Input Layer: PASS
Decision Layer: FAIL — Operator logic violation detected
Execution Layer: PASS

Overall System Status: FAILURE — Operator Error
```

This demonstrates how the classifier isolates the failure point in a system.
