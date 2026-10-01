⬅️ [[Lesson 7 -- Lists -- The Super Backpack]] | ➡️ [[Lesson 9 -- Functions -- Your Custom Superpowers]]

---

# 🔍 Lesson 8: Looping Through Lists

In [[Lesson 7 -- Lists -- The Super Backpack]], we stored our treasures inside lists. 

Now, what if you have a list of 100 Pokemon, and you want to show each one on the screen? Or what if you want to search through your backpack to see if you have a `Golden Key`?

We combine **Lists** with **For Loops**!

---

### The Explainer: The Magic `for item in list`

Instead of typing `backpack[0]`, `backpack[1]`, `backpack[2]`, Python lets you say:

> "For every item in my list, do this code!"

```python
for item in my_list:
    # Python automatically picks up each item one by one!
    print(item)
```

And to check if something is inside a list, you can use the English word `in`:
```python
if "Golden Key" in backpack:
    print("You can unlock the treasure chest!")
```

---

### The Code: Inspecting the Inventory

Let's look at each pet in an animal shelter:

```python
pets = ["Golden Retriever", "Robo-Hamster", "Fire Lizard", "Ninja Cat"]

print("--- 🐾 Pet Shelter Directory ---")
for pet in pets:
    print(f"Adopt a friendly {pet} today!")
```

Now let's check if a specific item is in our supplies:

```python
supplies = ["Torch", "Compass", "Canteen", "Rope"]

item_to_check = input("What item do you want to look for? ")

if item_to_check in supplies:
    print(f"✅ Yes! You have {item_to_check} in your supplies!")
else:
    print(f"❌ Oh no! You forgot to pack {item_to_check}!")
```

---

### The Task: 🎯 The Alien Safari Creature Scanner

Space Explorer Ali, your spaceship has landed on Planet Zog! Your scanner is tracking wild alien creatures.

Write a program that:
1. Creates a list named `aliens` containing 5 wacky alien species:
   `["Glow Squid", "Three-Eyed Toad", "Crystal Tiger", "Plasma Slime", "Mega Dragon"]`
2. Uses a `for` loop to scan and print each alien with a numbered tracker:
   ```text
   👾 Sighting 1: Glow Squid
   👾 Sighting 2: Three-Eyed Toad
   ...
   ```
3. Asks the player: `"Enter a creature to search for in your scanner: "`
4. Uses `if ... in aliens:`:
   - If found: `"🌟 Creature spotted on Planet Zog! Adding to Research Log!"`
   - If not found: `"🛸 Unknown creature! It must be hiding on the dark side of the moon!"`

> [!tip] Numbering items in a loop
> You can create a counter variable `number = 1` before the loop, and inside the loop add `number = number + 1`!

---

⬅️ **Previous:** [[Lesson 7 -- Lists -- The Super Backpack]] | ➡️ **Next Lesson:** [[Lesson 9 -- Functions -- Your Custom Superpowers]]
