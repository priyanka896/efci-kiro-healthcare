def validate_output(text):
    blocked_terms = ["prescribe", "dosage", "should take"]
    for term in blocked_terms:
        if term in text.lower():
            return False
    return True