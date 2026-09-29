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
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
