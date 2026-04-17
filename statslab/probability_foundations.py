def addition_rule(p_a, p_b, p_a_and_b=0):
    """
    Calculates P(A or B) = P(A) + P(B) - P(A and B).
    """
    return p_a + p_b - p_a_and_b

def multiplication_rule(p_a, p_b_given_a=None, independent=False):
    """
    Calculates P(A and B).
    If independent, P(A and B) = P(A) * P(B).
    If dependent, P(A and B) = P(A) * P(B|A).
    """
    if independent:
        # Assuming second parameter is p_b in this case
        return p_a * p_b_given_a
    return p_a * p_b_given_a

def conditional_probability(p_a_and_b, p_b):
    """
    Calculates P(A | B) = P(A and B) / P(B).
    """
    if p_b == 0:
        return "P(B) cannot be zero"
    return p_a_and_b / p_b

def bayes_theorem(p_b_given_a, p_a, p_b):
    """
    Calculates P(A | B) = (P(B | A) * P(A)) / P(B).
    """
    if p_b == 0:
        return "P(B) cannot be zero"
    return (p_b_given_a * p_a) / p_b

def set_intersection_size(set_a, set_b):
    """
    Returns the size of the intersection of two sets.
    """
    return len(set(set_a).intersection(set(set_b)))

def set_union_size(set_a, set_b):
    """
    Returns the size of the union of two sets.
    """
    return len(set(set_a).union(set(set_b)))
