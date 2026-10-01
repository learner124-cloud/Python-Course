⬅️ [[Lesson 4 -- Logic and Secret Passwords]] | ➡️ [[Big Task 1 -- The Secret Agent Mission]]

---

# 🔄 Lesson 5: For Loops and Repeating Magic

Imagine if your coach told you to do 50 jumping jacks. In code, would you type `print("Jumping jack!")` 50 times? No way, that's exhausting! 😴

Computers NEVER get tired. They can do things thousands of times in a blink of an eye. 

To repeat instructions without retyping them, we use a magical Python tool called a **For Loop**!

---

### The Explainer: How `for` and `range()` Work

In Python, a `for` loop works with a helper function named `range()`.

Think of `range(5)` like a list of numbers: `0, 1, 2, 3, 4`.
The loop picks up each number one by one, stores it in a counter variable, and runs the code block!

> [!important] Python Counts from 0!
> In computer science, Python starts counting at `0` instead of `1`:
> - `range(5)` counts: `0, 1, 2, 3, 4` (That is still 5 numbers in total!)
> - If you want to count from 1 to 5, you write: `range(1, 6)` (Python stops right before the second number!).
> - If you want to count backwards: `range(10, 0, -1)` (Starts at 10, counts down by -1, stops at 1).

---

### The Code: Casting Repeating Spells

Let's print a message 4 times:

```python
for step in range(4):
    print("👟 Step number", step)
```

Now let's count from 1 to 10:

```python
for number in range(1, 11):
    print(f"Number: {number}")
```

We can even make Python calculate math tables automatically! Look at the 7 Times Table:

```python
print("--- 7 Times Table ---")
for i in range(1, 11):
    result = 7 * i
    print(f"7 x {i} = {result}")
```

---

### The Task: 🎯 The NASA Rocket Blastoff Countdown!

Commander Ali, your mission to Mars is ready for launch!

Write a Python countdown program:
1. Print `"🚀 NASA Countdown Starting..."`
2. Use a `for` loop with `range(10, 0, -1)` to count down from `10` down to `1`.
3. Inside the loop, print each second: `"T-minus 10...", "T-minus 9..."` and so on.
4. When the loop finishes, print:
   `"🔥 3... 2... 1... BLASTOFF! 🚀 The rocket zooms into space!"`
5. **Bonus**: Add a second loop that prints `"✨ Flying past star 1"`, `"✨ Flying past star 2"` up to star 5!

> [!tip] Code Preview
> ```python
> print("🚀 NASA Countdown Starting...")
> for sec in range(10, 0, -1):
>     print(f"T-minus {sec}...")
> print("🔥 BLASTOFF! 🚀")
> ```

---

### 🌟 Milestone Reached!
Congratulations Ali! You have finished the first 5 lessons! 
Now you are ready for your very first **Big Task Mini-Project**!

👉 **Next Up:** [[Big Task 1 -- The Secret Agent Mission]]
