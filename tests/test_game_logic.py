from streamlit.testing.v1 import AppTest

from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

#TEST: Updated test case for too high guess using agent mode
def test_guess_too_high():
    # If secret is 50 and guess is 60, outcome should be "Too High" and the
    # hint should tell the player to go LOWER (regression test for the
    # reversed-hint bug).
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

#TEST: Updated test case for too low guess using agent mode
def test_guess_too_low():
    # If secret is 50 and guess is 40, outcome should be "Too Low" and the
    # hint should tell the player to go HIGHER (regression test for the
    # reversed-hint bug).
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

#TEST: Added test case for new game button using agent mode
def test_new_game_lets_you_guess_again():
    # Regression test: after finishing a game, clicking "New Game" must
    # reset status back to "playing" so the player can submit new guesses
    # and receive hints, not just reset the attempt counter.
    at = AppTest.from_file("../app.py")
    at.run()

    # Simulate a just-finished game.
    at.session_state.status = "lost"
    at.session_state.attempts = 8
    at.run()

    at.button[1].click().run()  # "New Game 🔁"

    assert at.session_state.status == "playing"
    assert at.session_state.attempts == 0

    # Submitting a guess right after New Game should actually be processed.
    at.text_input[0].input("50").run()
    at.button[0].click().run()  # "Submit Guess 🚀"

    assert not at.exception
    assert at.session_state.attempts == 1

#TEST: Added test case for mismatched guess attempts using agent mode
def test_invalid_guess_does_not_use_an_attempt():
    # Regression test: attempts should only increment for a validly parsed
    # guess, not just for clicking Submit. An invalid guess (e.g. blank or
    # non-numeric input) must leave the attempt count untouched, and the
    # "Attempts left" banner must reflect that immediately (no stale count).
    at = AppTest.from_file("../app.py")
    at.run()

    at.text_input[0].input("not a number").run()
    at.button[0].click().run()  # "Submit Guess 🚀"

    assert at.session_state.attempts == 0
    assert "Attempts left: 8" in at.info[0].value

    at.text_input[0].input("50").run()
    at.button[0].click().run()  # "Submit Guess 🚀"

    assert at.session_state.attempts == 1
    assert "Attempts left: 7" in at.info[0].value