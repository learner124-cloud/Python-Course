⬅️ [[Lesson 1 -- Basics Of Python]] | ➡️ [[Lesson 3 -- Making Decisions with If and Else]]

---

# 🤖 Lesson 2: Talking to Python with Input

In [[Lesson 1 -- Basics Of Python]], we learned how Python talks to *us* using `print()`. But what if you want to talk back to Python and tell it your name, your favorite food, or your secret superhero identity?

That's where the magical `input()` function comes in!

---

### The Explainer: What is `input()`?

Think of `input()` like Python holding a microphone up to your face and waiting for you to type something. 

When Python sees `input()`, it pauses everything and waits. As soon as you type your answer in the console and hit **Enter**, Python scoops up your words and gives them to a variable to remember!

```
You type words ➡️ input() grabs them ➡️ stored in a variable 📦
```

> [!tip] Strings by Default!
> Whatever you type into `input()` is always treated as a **String** (text with quotation marks). If you want Python to do math with a number you type, you turn it into an integer using `int()`:
> ```python
> age = int(input("How old are you? "))
> ```

---

### The Code: Listening and Answering

Here is how you ask someone for their name and greet them:

```python
# 1. Ask the player for their name
player_name = input("What is your name, recruit? ")

# 2. Print a personalized message!
print("Welcome to headquarters, " + player_name + "!")
```

You can also use Python's modern **F-strings** (formatted strings). Just put an `f` before the quotes, and put your variable inside `{}`:

```python
hero_name = input("Enter your hero name: ")
superpower = input("Enter your main power: ")

print(f"Watch out evil villains! {hero_name} is here with the power of {superpower}!")
```

And here is how to take numbers and do math:

```python
coins = int(input("How many gold coins did you find? "))
bonus_coins = 5

total = coins + bonus_coins
print(f"You now have {total} gold coins! Woohoo!")
```

---

### The Task: 🎯 Build "Ali's Super Robot Friend"

It's time to build your very own talking robot program, Ali!

Follow these steps:
1. Make Python print: `"Beep boop! I am Robo-9000!"`
2. Ask the user for their name using `input()` and save it in a variable named `user_name`.
3. Ask the user for their favorite video game and store it in `favorite_game`.
4. Ask how many hours they play each week using `int(input())`, and store it in `play_hours`.
5. Calculate how many hours they play in a whole month by multiplying `play_hours * 4`.
6. Print out an awesome friendly robot summary using all the variables!

> [!example] Expected Console Output
> ```text
> Beep boop! I am Robo-9000!
> What is your name? Ali
> What is your favorite video game? Minecraft
> How many hours do you play a week? 3
> Awesome, Ali! In one month you play 12 hours of Minecraft! You are a gaming legend!
> ```

---

⬅️ **Previous:** [[Lesson 1 -- Basics Of Python]] | ➡️ **Next Lesson:** [[Lesson 3 -- Making Decisions with If and Else]]
