# 🐍 Snake Case or Camel Case?

⬅️ Back to: [[Lesson 1 -- Basics Of Python]]

When we create variables in Python, we cannot put spaces between words. For example, Python will get confused if you write:
```python
super hero power = 100  # ❌ ERROR! Python hates spaces here!
```

To join words together nicely, programmers invented cool naming styles! The two most famous ones are **Snake Case** and **Camel Case**.

---

### 🐍 1. Snake Case (Python's Favorite!)

In **snake_case**, all words are in lowercase letters, and you separate each word with an underscore `_` (like a snake crawling on the ground).

```python
hero_name = "Agent Ali"
super_power_level = 9000
favorite_video_game = "Minecraft"
```

> [!tip] Python Pro Tip
> Python developers LOVE snake_case! Whenever you create variable names in Python, snake_case is the standard style to use.

---

### 🐫 2. Camel Case

In **camelCase**, the first word starts with a small letter, and every new word starts with a CAPITAL letter — just like the humps on a camel's back!

```python
heroName = "Agent Ali"
superPowerLevel = 9000
favoriteVideoGame = "Minecraft"
```

> [!note] Where is Camel Case used?
> Camel case is super popular in languages like JavaScript, but Python programmers usually stick with snake_case for variables!

---

### 🧠 Quick Quiz for Ali

Which of these are valid **snake_case** variables?
1. `secret_code = "xyz"`  ✅ (Yes! Underscores and small letters)
2. `secret code = "xyz"`  ❌ (No! Has spaces)
3. `Secret_Code = "xyz"`  ❌ (No! Has capital letters)
4. `laser_blaster_power = 99` ✅ (Yes! Perfect snake_case)

---

⬅️ Return to: [[Lesson 1 -- Basics Of Python]] | ➡️ Next up: [[Lesson 2 -- Talking to Python with Input]]
