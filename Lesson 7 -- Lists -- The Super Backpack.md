⬅️ [[Lesson 6 -- While Loops and Game Loops]] | ➡️ [[Lesson 8 -- Looping Through Lists]]

---

# 🎒 Lesson 7: Lists -- The Super Backpack

So far, each variable we made could only hold ONE item:
```python
favorite_food = "Pizza"
```

What if you have a list of all your favorite foods? Or your Minecraft inventory full of diamonds, swords, apples, and torches? 

You need a **List**! In Python, a list is like a magical superhero backpack that holds as many items as you want!

---

### The Explainer: How to Create a List

To make a list, you place your items inside square brackets `[` and `]`, separated by commas:

```python
backpack = ["Laser Blaster", "Health Potion", "Grappling Hook"]
```

#### The Secret of Indexing (Position Numbers)
Just like in [[Lesson 5 -- For Loops and Repeating Magic]], Python numbers list slots starting at **0**:

| Position (Index) | Item in Backpack |
| :---: | :--- |
| `backpack[0]` | `"Laser Blaster"` (The 1st item!) |
| `backpack[1]` | `"Health Potion"` (The 2nd item!) |
| `backpack[2]` | `"Grappling Hook"` (The 3rd item!) |

> [!important] Don't Forget Zero!
> If you want the first item, ask for `backpack[0]`! If you ask for `backpack[1]`, you get the second item!

---

### The Code: List Magic Tricks

#### 1. Adding an Item: `.append()`
When you find loot, pack it in with `.append()`:

```python
inventory = ["Shield", "Sword"]
inventory.append("Magic Wand")

print(inventory)
# Output: ['Shield', 'Sword', 'Magic Wand']
```

#### 2. Removing an Item: `.remove()` or `.pop()`
When you use up a potion, remove it:

```python
inventory.remove("Shield")
print(inventory)
# Output: ['Sword', 'Magic Wand']
```

#### 3. Counting Items: `len()`
How many items are in your bag? Use `len()` (short for length):

```python
total_items = len(inventory)
print(f"You have {total_items} items in your bag!")
```

---

### The Task: 🎯 Ali's Superhero Gadget Belt

Agent Ali, it's time to pack your gadget belt for the next mission!

Write a program that:
1. Creates a list called `gadgets` with 3 cool items: `"Night Vision Goggles"`, `"Smoke Bomb"`, and `"Jetpack"`.
2. Prints: `"Initial Gadget Belt:"` followed by the list.
3. Prints the very first gadget using `gadgets[0]`.
4. Asks Ali to type a brand new gadget to add using `new_gadget = input("Find a new gadget to pack: ")`.
5. Uses `.append(new_gadget)` to add it to the belt.
6. Prints the total number of gadgets on the belt using `len(gadgets)`.
7. Uses `.pop(1)` or `.remove("Smoke Bomb")` to use up the smoke bomb, and prints the updated list!

> [!tip] Try it yourself!
> Look how cool it feels to watch your inventory expand and shrink in the console!

---

⬅️ **Previous:** [[Lesson 6 -- While Loops and Game Loops]] | ➡️ **Next Lesson:** [[Lesson 8 -- Looping Through Lists]]
