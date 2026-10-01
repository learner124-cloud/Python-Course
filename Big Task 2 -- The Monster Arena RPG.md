⬅️ [[Lesson 10 -- Modules and Random Adventures]] | 🏠 [[Introduction to Python]]

---

# ⚔️ Big Task 2: The Monster Arena RPG

👑 **Grand Mini-Project Milestone #2 & Course Finale** (After Lessons 6 – 10)

Ali, look at how far you've come! You started with printing simple words, and now you have the powers of:
- 🔄 `while` loops & game loops ([[Lesson 6 -- While Loops and Game Loops]])
- 🎒 Inventory lists with `.append()` and `.remove()` ([[Lesson 7 -- Lists -- The Super Backpack]])
- 🔍 Searching through items with loops and `in` ([[Lesson 8 -- Looping Through Lists]])
- ⚡ Creating custom superpowers with `def` functions ([[Lesson 9 -- Functions -- Your Custom Superpowers]])
- 🎲 Random dice rolls and dramatic timing ([[Lesson 10 -- Modules and Random Adventures]])

Now, it is time for the **Ultimate Boss Project**: A complete, playable, turn-based **Monster Arena RPG Game**!

---

### 📜 The Story: The Colosseum of Code

> Deep in the Digital Kingdom, the great **Giga-Golem** has challenged the greatest coder in the realm: **Hero Ali**!
> Can you use your potions, calculate your sword strikes, and defeat the beast in battle?

---

### 🎮 Game Features Ali Will Build

1. **Player Stats & Inventory**:
   - `player_hp = 100`
   - `potions = ["Small Potion", "Mega Potion"]`
2. **Monster Stats**:
   - `monster_name = "Giga-Golem"`
   - `monster_hp = 90`
3. **Turn-Based Battle Loop**:
   - Runs `while player_hp > 0 and monster_hp > 0:`
   - Every round, Ali chooses an action:
     - `1. Attack ⚔️`: Roll random damage between `15` and `30`!
     - `2. Drink Potion 🧪`: Restores `25` HP and uses up a potion from your list!
     - `3. Cast Magic Spell ✨`: A high-risk, high-reward attack!
4. **Monster Turn**:
   - If the monster is still alive, it strikes back with `random.randint(10, 22)` damage!
5. **Dramatic Suspense**:
   - Uses `time.sleep(1)` between turns so the battle feels like a real video game!
6. **Victory / Defeat Screen**:
   - Declares Ali the Grand Champion of Python!

---

### 💻 The Complete Working Arena Game Code

Create a file named `monster_arena.py` and run your game:

```python
# =======================================================
# 👑 BIG TASK 2: MONSTER ARENA RPG
# Master Coded by: Hero Ali
# =======================================================

import random
import time

print("=" * 45)
print("⚔️ WELCOME TO THE DIGITAL MONSTER ARENA! ⚔️")
print("=" * 45)

hero_name = input("Enter your Hero Name: ")
player_hp = 100
potions = ["Healing Berry", "Super Elixir"]

monster_name = "Giga-Golem"
monster_hp = 90

print(f"\n⚡ {hero_name} steps onto the battlefield!")
print(f"👹 A wild {monster_name} roars angrily! (HP: {monster_hp})\n")

# --- Custom Functions ---
def show_status():
    print("-" * 30)
    print(f"👤 {hero_name} HP: {player_hp} | 🎒 Potions: {len(potions)}")
    print(f"👹 {monster_name} HP: {monster_hp}")
    print("-" * 30)

# --- The Main Battle Loop ---
while player_hp > 0 and monster_hp > 0:
    show_status()
    print("Choose your action:")
    print("1. Sword Strike ⚔️")
    print("2. Drink Potion 🧪")
    print("3. Lightning Spell ⚡")
    
    choice = input("What do you want to do (1, 2, or 3)? ")
    print()

    # Action 1: Sword Attack
    if choice == "1":
        damage = random.randint(15, 25)
        monster_hp -= damage
        print(f"💥 {hero_name} slashes with their sword for {damage} damage!")

    # Action 2: Heal with Potion
    elif choice == "2":
        if len(potions) > 0:
            used_potion = potions.pop(0)
            player_hp += 30
            if player_hp > 100:
                player_hp = 100  # Cap HP at max 100
            print(f"🧪 You drank {used_potion}! Restored 30 HP!")
        else:
            print("❌ Your potion bag is empty! You lost your turn!")

    # Action 3: Magic Spell
    elif choice == "3":
        damage = random.randint(5, 40)
        monster_hp -= damage
        print(f"⚡ Crackle! A blast of lightning shocks {monster_name} for {damage} damage!")

    else:
        print("⚠️ You stumbled and hesitated! No action taken!")

    time.sleep(1)

    # Check if Monster is defeated
    if monster_hp <= 0:
        print(f"\n🎉 BOOM! The mighty {monster_name} crumbles into dust!")
        break

    # Monster's Turn to Attack!
    print(f"\n👹 {monster_name} retaliates with an Earth Slam!")
    time.sleep(1)
    monster_damage = random.randint(10, 22)
    player_hp -= monster_damage
    print(f"💥 Ouch! You took {monster_damage} damage!\n")
    time.sleep(1)

# --- Battle Outcome ---
print("\n" + "=" * 45)
if player_hp > 0:
    print(f"🏆 VICTORY! {hero_name} WON THE BATTLE! 🏆")
    print("You are officially crowned the Python Arena Champion!")
else:
    print("💀 You fought bravely, but were defeated! Try again!")
print("=" * 45)
```

---

### 🎨 Awesome Customization Ideas for Ali

Once you test the game, you can make it even cooler:
1. **New Monsters**: Change the monster to an *Alien Robot* or *Shadow Dragon*!
2. **Super Loot**: Add a special sword that gives bonus attack points!
3. **Sound Effects**: Print cool sound words like `KAPOW!`, `SWOOSH!`, or `ZAAAP!`!

---

### 🎓 Ali's Graduation Certificate

```
================================================================
🎓 CERTIFICATE OF ACHIEVEMENT
This certifies that:
                  🌟 AGENT ALI 🌟
has successfully conquered the Python Beginner Course!
You have built variables, loops, decisions, lists, functions,
and your very own video games!
================================================================
```

---

⬅️ **Previous Lesson:** [[Lesson 10 -- Modules and Random Adventures]] | 🏠 **Back to Course Roadmap:** [[Introduction to Python]]
