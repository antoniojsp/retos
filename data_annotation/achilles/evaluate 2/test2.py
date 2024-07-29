def card_draw_probability(card_type, suite, num_draws):
    """
    Calculates the probability of drawing a specific card from a standard 52-card deck.

    Args:
        card_type: The rank of the desired card (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K).
        suite: The suit of the desired card (D, H, C, S).
        num_draws: The number of cards to be drawn.

    Returns:
        The probability of drawing the specified card within the given number of draws.
    """

    # There's only one card of each type and suite combination
    target_card_count = 1
    total_cards = 52

    # Calculate the probability of NOT drawing the card in a single draw
    probability_not_drawing = (total_cards - target_card_count) / total_cards

    # Calculate the probability of NOT drawing the card in any of the draws
    probability_not_drawing_in_n_draws = probability_not_drawing ** num_draws

    # The probability of drawing the card is the complement of not drawing it
    probability_drawing = 1 - probability_not_drawing_in_n_draws

    return probability_drawing


# Example usage:
card_type = 'A'
suite = 'H'
num_draws = 5

probability = card_draw_probability(card_type, suite, num_draws)
print(f"Probability of drawing the {card_type}{suite} in {num_draws} draws: {probability:.4f}")
