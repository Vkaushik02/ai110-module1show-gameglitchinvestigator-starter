import pytest
from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score

def test_too_high_guess_tells_player_to_go_lower():
    # Regression: hints were reversed. A guess above the secret
    # must say "Too High" and tell the player to go LOWER.
    outcome, message = check_guess(80, 50)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_too_low_guess_tells_player_to_go_higher():
    # A guess below the secret must say "Too Low" and tell the player to go HIGHER.
    outcome, message = check_guess(20, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_correct_guess_wins():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"


def test_difficulty_ranges_increase_easy_to_normal_to_hard():
    # Range size must grow with difficulty.
    def size(d):
        low, high = get_range_for_difficulty(d)
        return high - low + 1

    assert size("Easy") < size("Normal") < size("Hard")


def test_each_difficulty_returns_expected_range():
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 50)
    assert get_range_for_difficulty("Hard") == (1, 100)


def test_unknown_difficulty_falls_back_to_normal_range():
    assert get_range_for_difficulty("Impossible") == get_range_for_difficulty("Hard")


# edge case test cases: 
#1
@pytest.mark.parametrize("raw", [None, ""])
def test_parse_guess_rejects_empty_input(raw):
    # No input at all: the game should ask for a guess, not call it "not a number".
    assert parse_guess(raw) == (False, None, "Enter a guess.")

#2
@pytest.mark.parametrize("raw", ["abc", "12abc", "1.2.3", "1.0e999"])
def test_parse_guess_rejects_non_numeric_input(raw):
    # "1.0e999" parses as a float but overflows int(); it must be rejected, not crash.
    assert parse_guess(raw) == (False, None, "That is not a number.")

#3
@pytest.mark.parametrize(
    "raw, expected",
    [("-5", -5), ("0", 0), ("  42 ", 42), ("3.9", 3), ("-3.9", -3)],
)
def test_parse_guess_handles_negatives_decimals_and_whitespace(raw, expected):
    # Decimals truncate toward zero; negatives parse (range is not checked here).
    assert parse_guess(raw) == (True, expected, None)

