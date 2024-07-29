def probability_of_drawing_card(card_type, suite, draws):
    """
    Calculates the probability of drawing a specific card from a standard 52-card deck.

    Args:
      card_type: The rank of the card (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K).
      suite: The suit of the card (D, H, C, S).
      draws: The number of cards to be drawn.

    Returns:
      The probability of drawing the specified card within the given number of draws,
      rounded to four decimal places.
    """

    # Input validation:
    valid_card_types = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    valid_suites = ['D', 'H', 'C', 'S']

    if card_type not in valid_card_types:
        raise ValueError("Invalid card type. Must be one of: " + str(valid_card_types))
    if suite not in valid_suites:
        raise ValueError("Invalid card suite. Must be one of: " + str(valid_suites))
    if not isinstance(draws, int) or draws <= 0:
        raise ValueError("Invalid number of draws. Must be a positive integer.")

    # There's only one card of each type and suite in a deck
    target_card_count = 1

    # Calculate the probability of NOT drawing the card on each draw
    probability_of_not_drawing = 1.0
    for _ in range(draws):
        probability_of_not_drawing *= (52 - target_card_count) / 52
        target_card_count = max(0, target_card_count - 1)  # Card can only be drawn once

    # Probability of drawing the card is 1 minus the probability of not drawing it
    probability_of_drawing = 1 - probability_of_not_drawing

    return round(probability_of_drawing, 4)


# Example usage:
card_type = 'A'
suite = 'H'
draws = 3

probability = probability_of_drawing_card(card_type, suite, draws)
print(f"The probability of e the {card_type}{suite} in {draws} draws is: {probability}")
