# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- The game's purpose is to be a guessing game that requires the user to guess a random number within a certain number of tries.
- I found multiple bugs, such as the hints being flipped, the New Game button not working, and the ranges being incorrect for the different modes. Furthermore, I made some changes to the logic, such as changing the number of tries used from 1 to 0 and disabling the developer debug section because it was defeating the purpose of the game.
- The fixes I applied included switching the hint statements, fixing the New Game button's status, setting the number of tries used to 0, resetting the score, and setting the correct ranges. The developer debug section was commented out, and the ranges were updated for each mode.  

## 📸 Demo Walkthrough

1. Start the game. Run python -m streamlit run app.py. The sidebar shows the difficulty default Normal, the range (1 to 50) and the attempts allowed 8. The main panel shows Guess a number between 1 and 50 and attempts left: 8.
2. Make a first guess. Type a number such as 25 and click Submit Guess. The game replies with a hint:
- "📈 Go HIGHER!" means your guess was too low.
- "📉 Go LOWER!" means your guess was too high. Attempts left drops by one, and the score changes.
3. Keep guessing based on the hint, for example by moving halfway toward the secret each time.
4. Try a bad entry. Type something like abc and submit. The game shows "That is not a number." The entry still counts as an attempt.
5. Turn hints off. Untick Show hint, then submit another guess. The Higher/Lower message no longer appears, but the attempt and score still update. Tick it again to get the hints back.
6. Change the difficulty. Pick a different level in the sidebar. The range and attempt limit update.
7. Win. When you guess the secret, the game shows "🎉 Correct!", balloons, and "You won! The secret was N. Final score: x". Further guesses are ignored with "You already won. Start a new game to play again."
8. Lose. If you use every attempt without finding it, the game shows "Out of attempts! The secret was N. Score: …" and locks.
9. Play again. Click New Game 🔁. A new random secret is picked, and the score, attempts and history reset.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
tests\test_game_logic.py .....................                                                                                                     [100%]
=============================== 17 passed in 0.09s ===========================================================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]