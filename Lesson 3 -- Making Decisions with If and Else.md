⬅️ [[Lesson 2 -- Talking to Python with Input]] | ➡️ [[Lesson 4 -- Logic and Secret Passwords]]

---

# 🚦 Lesson 3: Making Decisions with If and Else

Welcome to Lesson 3! Up until now, our Python programs just ran from top to bottom without thinking. 

Today, we are going to give Python a **brain** so it can make smart choices!

---

### The Explainer: How Does Python Make Decisions?

In real life, you make decisions all the time:
- **IF** it is raining outside, you take an umbrella.
- **ELSE** (if it's not raining), you wear sunglasses!

In Python, we use the `if`, `elif` (short for *else if*), and `else` keywords to do the exact same thing! 

To check conditions, Python uses [[Comparison Operators in Python]] (like `==`, `>`, `<`).

> [!important] The Rule of Indentation (The 4 Spaces)
> Python uses spaces (indentation) to know which lines belong inside the decision. Whenever you see a colon `:` at the end of an `if` line, press **Tab** (or 4 spaces) on the next line!
> 
> ```python
> if condition:
>     # This line is pushed inside! Python runs this only if True!
> ```

---

### The Code: Fork in the Road

Here is a simple decision:

```python
score = int(input("What score did you get in the game? "))

if score >= 100:
    print("🏆 AMAZING! You unlocked the Golden Trophy!")
else:
    print("Keep playing! You need 100 points for the trophy.")
```

Now let's use `elif` to check multiple possibilities (like grades or ranks):

```python
level = int(input("Enter your hero level: "))

if level >= 20:
    print("You are a Legendary Champion! ⚡")
elif level >= 10:
    print("You are an Elite Warrior! ⚔️")
elif level >= 1:
    print("You are a Brave Novice! 🛡️")
else:
    print("Invalid level! Must be at least level 1.")
```

---

### The Task: 🎯 The Three Magic Mystery Doors

Ali, you have stumbled into a mysterious wizard's dungeon with three glowing doors!

Write a Python game that:
1. Greets the player: `"🚪 You stand before 3 magic doors: Door 1, Door 2, or Door 3."`
2. Asks the player: `"Which door do you open (1, 2, or 3)? "` and converts it with `int(input())`.
3. Uses `if`, `elif`, and `else` to show what happens:
   - **If they pick 1**: `"🐉 A baby dragon pops out and gives you a bag of gold!"`
   - **If they pick 2**: `"🍕 You found an infinite pepperoni pizza buffet! Delicious!"`
   - **If they pick 3**: `"👻 A friendly ghost challenges you to a dance-off!"`
   - **Else (any other number)**: `"⚠️ Whoops! A trapdoor opened and you slid back to the entrance!"`

> [!tip] Test Every Door!
> Run your program 4 times and try typing `1`, `2`, `3`, and `99` to see all the different endings!

---

⬅️ **Previous:** [[Lesson 2 -- Talking to Python with Input]] | ➡️ **Next Lesson:** [[Lesson 4 -- Logic and Secret Passwords]]
