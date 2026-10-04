# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

When I first ran the program, I noticed several bugs with the hints and the New Game button.

- The Normal and Hard mode ranges were switched. This bug was in the app.py file.

- The New Game button did not work when clicked. This bug was in the app.py file.

- The Show Hint feature only showed one hint instead of the expected hints. This bug was in the app.py file.


**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|Normal | Range 1-50        | 1-100           | none                   |    
|New game button| New game  | Nothing happens | none                   |  
|Show hint| Lower when value is higher| Showing higher| none|

---

## 2. How did you use AI as a teammate?
- I used Claude as my AI teammate for this project. One example where an AI suggestion was correct was the logic for the hints. When the guessed score is higher than the target, the hint should tell the player to go lower, and that is exactly what the AI suggested. I verified this by using test cases and testing the hint functionality. The code worked correctly with the test cases I ran.

- One suggestion I did not accept was the code for the ranges of the individual levels. Claude suggested that the Normal and Hard ranges should be 100 and 200 respectively, but I chose to keep the ranges that were already given because changing them was outside the original intent of the program. The ranges themselves were not necessarily the bug. The actual issue was that the Normal and Hard ranges were switched. I decided that fixing the switched ranges was more appropriate than changing the intended ranges. Another one is one of the test case for checking if the range or hard is greater than that of normal. This is not necessary as the ranges are already set and hardcoded so to test them again is not needed and out of scope for this program. 
---

## 3. Debugging and testing your fixes

- I decided that a bug was fixed when I tested the feature again and it behaved the way I expected it to. One manual test I ran was clicking the New Game button. Before the fix, clicking the button did not start a new game. After making the fix, I clicked the button again and confirmed that a new game started correctly. I also tested the difficulty modes and the Show Hint feature to make sure they worked as expected.

- I used pytest to test the hint functionality. I tested different cases, such as when the guess was higher or lower than the target, to make sure the correct hint was returned. The tests passed, which showed me that the hint logic was working correctly after the fix.

- AI helped me understand and think of ways to test the bugs. It helped me identify what the expected behavior should be and suggested testing different cases after making changes to make sure the features were actually fixed.
---

## 4. What did you learn about Streamlit and state?

- Streamlit reruns your Python code from the top whenever the user interacts with the app, such as clicking a button. It's like the app refreshing itself and running the code again. Session state is like used to remember information between the reruns. You can think of it like a storage box for the current info, like score, number of tries, or the random number.

---

## 5. Looking ahead: your developer habits

- One strategy I want to reuse in future projects is testing my code after making changes. Testing each feature helped me find bugs and make sure my fixes actually worked. Becuase sometimes the change would break something else. 
- One thing I would do differently next time I work with AI on a coding task is be more specific with my prompts and explain the original purpose of the program. This would help the AI give suggestions that fit the project instead of suggesting unnecessary changes. It would also prevent me from explaining over and over again. 
- This project changed the way I think about AI code because I learned that AI can give useful suggestions, but I still need to understand and test the code myself. AI generated code is not always correct or necessary for the project as it could miss the context sometimes.
