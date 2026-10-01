⬅️ [[Lesson 8 -- Looping Through Lists]] | ➡️ [[Lesson 10 -- Modules and Random Adventures]]

---

# ⚡ Lesson 9: Functions -- Your Custom Superpowers

We already know functions that Python built for us, like `print()`, `input()`, and `len()`. 

Did you know you can invent **your own functions** with your own custom names and superpowers? 

Whenever you write a set of code you want to use over and over again, you can bundle it into a **Function**!

---

### The Explainer: How to Build a Function

Think of a function like a **vending machine** or a **magic spell**:
1. **Define it**: You teach Python the recipe using the keyword `def` (short for *define*).
2. **Parameters (Ingredients)**: You can give the function information inside `()` to work with.
3. **Call it**: Whenever you want Python to do that action, you just say its name with `()`!

```
def spell_name(parameter):
    # What the spell does!
```

> [!important] Don't Forget to Call It!
> Defining a function is just teaching Python how to do something. Python won't actually DO it until you call the function by typing its name with `()`!

---

### The Code: Defining and Calling

Here is a simple greeting function:

```python
def superhero_shout():
    print("💥 POW! BAM! Super-Ali to the rescue! 💥")

# Now call the function whenever danger strikes!
superhero_shout()
superhero_shout()
```

#### Functions with Parameters (Passing Information)
We can pass information inside the parentheses:

```python
def greet_hero(hero_name, power_level):
    print(f"⚡ Welcome {hero_name}! Power level is over {power_level}!")

# Call it with different heroes:
greet_hero("Ali", 9000)
greet_hero("Batman", 500)
```

#### Returning Answers with `return`
A function can do calculations and hand back the final answer:

```python
def double_damage(base_attack):
    critical_hit = base_attack * 2
    return critical_hit

final_attack = double_damage(45)
print(f"Critical Strike dealt {final_attack} damage!")
```

---

### The Task: 🎯 The Wizard Spell Caster

Grand Wizard Ali, it's time to build your spellbook!

Write a program with a custom function:
1. Define a function called `cast_spell(spell_name, target)`:
   - Inside the function, make it print:
     `f"✨ Ali waves his glowing wand and casts {spell_name} at the {target}!"`
2. Define a second function called `calculate_damage(level)`:
   - Inside, multiply `level * 15`.
   - Use `return` to return that number!
3. Below your functions, call `cast_spell("Mega Fireball", "Goblin King")`.
4. Call `damage = calculate_damage(5)`.
5. Print: `f"💥 Direct hit! The spell dealt {damage} points of damage!"`

> [!tip] Clean Code Superhero
> Look how organized your program looks when you use functions! You can cast 10 different spells with just one line each!

---

⬅️ **Previous:** [[Lesson 8 -- Looping Through Lists]] | ➡️ **Next Lesson:** [[Lesson 10 -- Modules and Random Adventures]]
