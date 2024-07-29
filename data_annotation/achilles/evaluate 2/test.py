from math import comb


def card_draw_probability(card_type, suite, num_draws):
    """
    Calculates the probability of drawing a specific card from a standard 52-card deck at least once within a given number of draws.

    Args:
        card_type: The rank of the desired card (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K).
        suite: The suit of the desired card (D, H, C, S).
        num_draws: The number of cards to be drawn.

    Returns:
        The probability of drawing the specified card at least once within the given number of draws.
    """

    total_cards = 52
    target_card_count = 1

    # Total ways to draw num_draws cards from the deck
    total_ways = comb(total_cards, num_draws)

    # Ways to draw num_draws cards without the specific card
    remaining_cards = total_cards - target_card_count
    ways_without_target = comb(remaining_cards, num_draws)

    # Calculate the probability
    probability_not_drawing_target = ways_without_target / total_ways
    probability_drawing_target = 1 - probability_not_drawing_target

    return probability_drawing_target


# Example usage:
card_type = 'A'
suite = 'H'
num_draws = 5

probability = card_draw_probability(card_type, suite, num_draws)
print(f"Probability of drawing {card_type}{suite} in {num_draws} draws: {probability:.4f}")
