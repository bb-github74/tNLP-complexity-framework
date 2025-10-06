MODIFIER_WEIGHTS = {
    'hedging': 1.5,
    'boosting': 1.0,
    'negation': 2.0,
    'evidentiality': 1.2,
    'concessive': 1.3,
}

MODIFIERS = {
    'hedging': ['perhaps', 'likely', 'might', 'could'],
    'boosting': ['definitely', 'strongly', 'clearly'],
    'negation': ['not', 'never', 'no'],
    'evidentiality': ['reportedly', 'according to', 'it is said'],
    'concessive': ['although', 'even though', 'however'],
}

def compute_complexity(sentence):
    score = 0
    sentence_lower = sentence.lower()
    for category, words in MODIFIERS.items():
        count = sum(1 for word in words if word in sentence_lower)
        score += MODIFIER_WEIGHTS[category] * count
    return score

