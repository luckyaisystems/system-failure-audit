def classify_failure(input_quality, logic_integrity, execution_accuracy):
    """
    Classifies system failure based on decision layer inputs.
    Values: 0 (Fail) to 1 (Pass)
    """
    if input_quality < 0.5:
        return "INPUT FAILURE: Raw data or SoS tiering is corrupted."
    elif logic_integrity < 0.5:
        return "MODEL ERROR: Surface-level logic/narrative bias detected."
    elif execution_accuracy < 0.5:
        return "EXECUTION DECAY: Sound plan, failed implementation."
    else:
        return "SYSTEM NOMINAL: Logical output achieved."

# Example: Auditing the 30% win-rate week
print(f"Audit Result: {classify_failure(input_quality=0.8, logic_integrity=0.3, execution_accuracy=0.9)}")
