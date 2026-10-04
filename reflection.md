# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

The first time I ran the game, the core game loop appeared mostly functional. However, there were two major bugs I noticed very quickly. Firstly, the hints were backwards and prompted me to go HIGHER when I was too high, and LOWER when I was too low. This made the hint feature unhelpful. Secondly, once the game ended, I couldn't get the new game button to work properly without refreshing the page. The new game button appeared to update the guess counter in the dev panel but I couldn't actually make guesses nor receive hints for that new game session.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input                    | Expected Behavior      | Actual Behavior             | Console Output / Error | Suspected Code Location |
|--------------------------|------------------------|-----------------------------|------------------------|-------------------------|
| guess of 60              | Hint: go lower         | Hint: go higher             | "None"                 | app.py, check_guess():  |
| press new game           | new game guessing      | non-responsive guess button | "None"                 | app.py, lines 147-188   | 
| submit second-last guess | allowed one more guess | told game is over           | "None"                 | app.py, lines 181-188   |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

I used Claude Code on this project.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

One example of an AI suggestion that was correct was when I had the AI help me debug the issue with hints offering the wrong suggestions. The AI suggestion is listed below:

  try:
    if guess > secret:
      return "Too High", "📉 Go LOWER!"
    else:
      return "Too Low", "📈 Go HIGHER!"
  except TypeError:
    g = str(guess)
    if g == secret:
      return "Win", "🎉 Correct!"
    if g > secret:
      return "Too High", "📉 Go LOWER!"
    return "Too Low", "📈 Go HIGHER!"

This result was correct as it simply removed the lines of code offering unhelpful suggestions such as "return 'Too low', 'Go LOWER!'" with it's helpful, reversed counterpart. I verified this result by passing it into the test case I made using agent mode, and then by playing the game and testing the behavior that way. 

- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

One example of an AI suggestion I did not accept was one the agent gave while I was working to resolve the attempt counter bug. It gave me a very myopic suggestion that involved only changing the "st.session_state.attempts" line. The fix it offered was correct, but it failed to capture the full scope of the bug such as the code displaying the attempt count PRIOR to incrementing attempts, which kept the attempt counter permanently displaying a "past" state from the last turn. I fixed this by adding some additional context to my next prompt, to which it gave a more comprehensive fix. I verified both the "incorrectness" of the bad suggestion and the correctness of the fixed prompt by running a game for each, and later generating a test case for guess attempts.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

I decided whether a bug was really fixed by using a three step process. First, I inspected Claude's output to see how well the bug fix mapped to the logic outline I'd have it generate for me in a previous prompt. I had to rely on a little intuition in some cases, as I'm no expert, but if the code looked sensible enough and didn't leave any apparent loose ends I would move on to the next step. The next step I took was opening an instance of the game and playing a few rounds, testing different inputs and button clicks to see if what broke before the bug-fix would break again. If the game ran as intended, I'd move on to the third step where I'd have Claude generate a test case using a prompt that specifically laid out the problem I wanted to test for. By passing that test, I felt confident that the bug in the code was fixed.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

  One of the tests I ran is contained in the test_new_game_lets_you_guess_again(): function located in test_game_logic.py. I'll admit, the logic of the test case is difficult to fully wrap my head around. It's manipulating state variables to mimic the state of a game that just finished playing, and then submits a guess after "New Game" was pressed in order to check if the game is actually responding to player input in a new game. If it responds normally, the test case passes.

- Did AI help you design or understand any tests? How?

Yes. For the most part, I had Claude design generate the test cases. I'm not very experienced in writing test cases, so much of my role was in providing a specific prompt of the edge case I wanted to check for. 

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

  I want to reuse the habit of having AI explain the underlying logic behind a bug before I move to resolve it. I think it makes me a better programmer if I slow down and try to understand what's going on when something

- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

This project changed the way I think about AI generated code by making me more aware of how important human oversight and "scaffolding" is in order to get AI to generate good code. It's like the AI gets more intelligent when provided more comprehensive prompts, so the quality of AI output depends (at least in part) on the technical proficiency of the person using it. 
