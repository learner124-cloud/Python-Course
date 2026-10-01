⬅️ [[Big Task 1 -- The Secret Agent Mission]] | ➡️ [[Lesson 7 -- Lists -- The Super Backpack]]

---

# 🔄 Lesson 6: While Loops and Game Loops

In [[Lesson 5 -- For Loops and Repeating Magic]], we learned about `for` loops. A `for` loop is great when you know *in advance* how many times you want to repeat something (like 5 times or 10 times).

But what if you are playing a video game, and you want the game to keep running **WHILE the player is still alive**? 

You don't know if the player will survive 2 minutes or 2 hours! That is where the **While Loop** shines!

---

### The Explainer: How Does a `while` Loop Work?

A `while` loop checks a condition:
- If the condition is `True`, it runs the code inside.
- Then it checks the condition again. Still `True`? Run again!
- It keeps looping **until** the condition becomes `False`!

```
Is condition True?
   ├── YES ➡️ Run code block ➡️ Go back and check again
   └── NO  ➡️ Exit loop and continue rest of program!
```

> [!caution] The Infinite Loop Monster! 🧟
> If your condition NEVER turns `False`, Python will loop forever and never stop!
> If this ever happens and your console goes crazy, press **Ctrl + C** on your keyboard to instantly freeze and stop Python!

---

### The Code: Counting and Escaping

Here is a `while` loop that counts to 3:

```python
count = 1

while count <= 3:
    print(f"Loop count: {count}")
    count = count + 1  # ⬅️ Super important! Without this, count stays 1 forever!

print("Done looping!")
```

#### The Secret Weapon: `break`
You can instantly escape any loop using the word `break`:

```python
while True:
    answer = input("Say 'stop' to end the loop: ")
    if answer.lower() == "stop":
        print("You found the exit! Goodbye!")
        break  # ⬅️ Shatters the loop immediately!
    print("Looping again...")
```

---

### The Task: 🎯 The Secret Number Guessing Game

Ali, let's create a classic guessing game where the player keeps guessing until they get it right!

Follow these steps:
1. Set a secret number variable: `secret_number = 7`.
2. Create a variable `guess = 0`.
3. Start a `while` loop that runs `while guess != secret_number:`
4. Inside the loop:
   - Ask the player: `"Guess a secret number between 1 and 10: "`
   - Convert the answer with `int(input())` and store it in `guess`.
   - If `guess < secret_number`: print `"Too low! Try again! 📈"`
   - If `guess > secret_number`: print `"Too high! Try again! 📉"`
5. Outside the loop (when they finally guess 7!):
   - Print `"🎉 BINGO! You guessed the secret number 7! You win!"`

> [!tip] Watch the Indentation!
> The victory message goes outside the while loop (no spaces at the front), so it only runs once the player gets the number right!

---

⬅️ **Previous:** [[Big Task 1 -- The Secret Agent Mission]] | ➡️ **Next Lesson:** [[Lesson 7 -- Lists -- The Super Backpack]]
