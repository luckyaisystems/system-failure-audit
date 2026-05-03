# system-failure-audit
A deterministic logic engine for classifying failure modes across input, operator, and execution layers — inspired by PLC safety interlocks and AI‑assisted decision systems
![System Failure Audit Diagram](https://github.com/luckyaisystems/system-failure-audit/blob/main/Screenshot%202026-05-02%2010.11.22%20PM.png)
## Code Description

The `failure_audit.py` script implements a deterministic 3-layer failure classifier:

- **Input Layer (Model Error):** Detects bad or corrupted data  
- **Decision Layer (Operator Error):** Detects bias, emotion, or logic violations  
- **Execution Layer (Execution Decay):** Detects timing failures or action breakdowns  

This mirrors how PLCs perform:

- Input validation  
- Logic scan cycles  
- Output execution checks  

It is the same structure used in industrial automation, safety interlocks, and AI decision-audit systems.
```
## Example Output

Running the script produces:

--- Decision Audit Result ---
Audit Status: CRITICAL: Operator Error. Bias or emotion bypassed the Interceptor protocol.

```

This demonstrates how the classifier isolates the failure point in a system.
