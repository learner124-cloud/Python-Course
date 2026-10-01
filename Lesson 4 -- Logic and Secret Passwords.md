⬅️ [[Lesson 3 -- Making Decisions with If and Else]] | ➡️ [[Lesson 5 -- For Loops and Repeating Magic]]

---

# 🔐 Lesson 4: Logic and Secret Passwords

In [[Lesson 3 -- Making Decisions with If and Else]], we learned how to check one condition with `if`. 

What happens when you need to check **two or three things at the exact same time**? For example:
- To enter the secret lab, you need the **password** AND the **secret fingerprint**!
- To ride the rollercoaster, you must be **tall enough** OR have a **grown-up with you**!

Python has 3 special logic words for this: `and`, `or`, and `not`.

---

### The Explainer: The 3 Logic Superpowers

1. **`and` (Both must be True!)**
   - Both sides must be correct. If even one side is False, the whole thing fails!
   - Example: `has_key and knows_password`

2. **`or` (At least one must be True!)**
   - If either the left side OR the right side is True, you win! Only fails if both are False.
   - Example: `is_saturday or is_sunday` (It's the weekend!)

3. **`not` (Flips True to False, and False to True!)**
   - The opposite flipper!
   - Example: `not is_raining` means "it is NOT raining (it's sunny!)"

---

### The Code: Guarding the Vault

Let's test these superpowers in real code:

```python
# Testing 'and'
has_key = True
knows_pin = True

if has_key and knows_pin:
    print("🔓 Safe opened! Here is the diamond!")
else:
    print("🔒 Alarm triggered! Access denied!")
```

Now let's test `or` with player input:

```python
day = input("What day is today? ").lower()

if day == "saturday" or day == "sunday":
    print("🎮 Woohoo! No school today, time for games!")
else:
    print("📚 School day! Time to learn something awesome.")
```

And here is `not` in action:

```python
is_game_over = False

if not is_game_over:
    print("Keep playing, hero! The battle is still on!")
```

---

### The Task: 🎯 The Secret Agent Clubhouse Bouncer

Agent Ali, your secret treehouse clubhouse needs an automated security bouncer!

Write a program that:
1. Asks the visitor: `"What is the secret club password? "`
2. Asks the visitor: `"How old are you? "` (use `int(input())`).
3. Uses `and` to check the rules:
   - To get in, the password must be `"superpython"` **AND** the visitor must be at least `8` years old (`age >= 8`).
4. If **both** are correct:
   - Print `"🎉 ACCESS GRANTED! Welcome inside the Treehouse HQ, secret agent!"`
5. If either is wrong:
   - Print `"🚨 BEEP BEEP! ACCESS DENIED! Only cool kid coders allowed!"`

> [!tip] Bonus Challenge!
> What if the secret password could be `"superpython"` OR `"alirocks"`? Try modifying your `if` condition using `or`!

---

⬅️ **Previous:** [[Lesson 3 -- Making Decisions with If and Else]] | ➡️ **Next Lesson:** [[Lesson 5 -- For Loops and Repeating Magic]]
