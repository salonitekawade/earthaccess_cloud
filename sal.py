import random

def nominal_group_technique(options):
    """
    Implements the Nominal Group Technique for group decision-making.

    Args:
        options: A list of options to consider.

    Returns:
        The most preferred option based on group voting.
    """

    # Individual brainstorming
    individual_scores = {}
    for option in options:
        score = random.randint(1, 5)  # Replace with actual scoring mechanism
        individual_scores[option] = score

    # Group discussion and voting
    group_scores = {}
    for option in options:
        group_score = sum(individual_scores[option] for _ in range(len(individual_scores)))
        group_scores[option] = group_score

    # Determine the most preferred option
    most_preferred_option = max(group_scores, key=group_scores.get)
    return most_preferred_option

# Example usage
options = ["Option A", "Option B", "Option C"]
preferred_option = nominal_group_technique(options)
print("Most preferred option:", preferred_option)