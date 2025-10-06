from tnlp.modifier_scoring import compute_complexity

def test_modifier_scoring():
    sentence = "Although it might be profitable, we are not certain."
    score = compute_complexity(sentence)
    assert score > 0

