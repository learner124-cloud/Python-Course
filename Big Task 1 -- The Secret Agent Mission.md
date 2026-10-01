⬅️ [[Lesson 5 -- For Loops and Repeating Magic]] | ➡️ [[Lesson 6 -- While Loops and Game Loops]]

---

# 🕵️ Big Task 1: The Secret Agent Mission

⭐ **Mini-Project Milestone #1** (After Lessons 1 – 5)

Congratulations, Ali! You have mastered the core foundations of Python:
- 🖨️ Printing & Data Types ([[Lesson 1 -- Basics Of Python]])
- 📦 Variables & Math ([[Lesson 1 -- Basics Of Python]])
- 🎤 Asking questions with `input()` ([[Lesson 2 -- Talking to Python with Input]])
- 🚦 Making decisions with `if`, `elif`, `else` ([[Lesson 3 -- Making Decisions with If and Else]])
- 🔐 Super logic with `and`, `or`, `not` ([[Lesson 4 -- Logic and Secret Passwords]])
- 🔄 Repeating actions with `for` loops ([[Lesson 5 -- For Loops and Repeating Magic]])

Now, it is time to combine all these superpowers together to build your **very first complete text-adventure game**!

---

### 📜 The Story Briefing

> Evil villain **Dr. Glitch** has locked the city's supercomputer inside his high-tech fortress! 
> Only **Agent Ali** can sneak inside, disable the security systems, crack the vault code, and save the day!

---

### 🎯 Mission Objectives (Step-by-Step)

Your program must have **4 interactive phases**:

#### Phase 1: Agent Identification
- Welcome the player and ask for their agent name.
- Store their name in a variable like `agent_name`.
- Give them a starting energy score: `energy = 100`.
- Print a cool welcome message: `"Welcome, Agent {agent_name}! Initial energy: 100"`.

#### Phase 2: The Electric Gate Puzzle
- The gate is locked with a math puzzle!
- Print: `"⚡ To hack the electric gate, calculate: 25 multiplied by 4 minus 10!"`
- Ask the player for their answer using `int(input("Enter code: "))`.
- The correct code is `25 * 4 - 10` (which is `90`!).
- Use an `if` statement:
  - If they get it right: `"✅ Gate hacked! Security system deactivated!"`
  - If they get it wrong: `"⚡ Zap! An electric shock hit you! -20 energy!"` (subtract 20 from energy).

#### Phase 3: The Laser Hallway (The Loop!)
- Dr. Glitch placed 5 red laser beams in the hallway!
- Use a `for` loop with `range(1, 6)` to disarm all 5 lasers:

```python
for laser in range(1, 6):
    print(f"🔴 Jumping over Laser #{laser}... Deactivated!")
```

- Print `"🏃 Phew! All 5 lasers cleared!"`

#### Phase 4: The Final Vault Choice
- Agent Ali arrives at the vault! There are 3 buttons:
  - `1`: Blue Button
  - `2`: Red Button
  - `3`: Golden Button
- Ask the player: `"Which button do you press (1, 2, or 3)? "`
- Use `if`, `elif`, and `else`:
  - **Button 1**: Dr. Glitch's confetti trap goes off! (Harmless fun).
  - **Button 2**: The alarm sounds, but Ali grabs the USB drive just in time!
  - **Button 3**: The vault opens smoothly! Ali recovers the master data chip!
  - **Else**: Invalid button, but Ali kicks the door open anyway like a true hero!

#### Phase 5: Mission Debriefing
- Print a victory banner:
  ```text
  ===========================================
  🎉 MISSION ACCOMPLISHED, AGENT ALI! 🎉
  You defeated Dr. Glitch and saved the city!
  Final Energy: 100 / 100
  ===========================================
  ```

---

### 💡 Starter Code Template for Ali

Open a new Python file called `secret_agent_game.py` and assemble your mission:

```python
# ---------------------------------------------
# Big Task 1: The Secret Agent Mission
# Coded by: Agent Ali
# ---------------------------------------------

print("🕵️ Dr. Glitch's Fortress Infiltration 🕵️")

# Phase 1: Agent ID
agent_name = input("Enter your Agent Codename: ")
energy = 100
print(f"Welcome, Agent {agent_name}! Energy Level: {energy}")

# Phase 2: Math Puzzle
print("\n--- Phase 2: The Security Gate ---")
gate_answer = int(input("Crack the code: What is 25 * 4 - 10? "))
if gate_answer == 90:
    print("✅ Access Granted! Gate unlocked!")
else:
    print("⚡ BZZT! Wrong code! Lost 20 energy!")
    energy = energy - 20

# Phase 3: Laser Hallway
print("\n--- Phase 3: Laser Grid ---")
for laser in range(1, 6):
    print(f"🔴 Jumping over Laser #{laser}... CLEARED!")

# Phase 4: Vault Choice
print("\n--- Phase 4: The Vault Door ---")
choice = int(input("Pick a button (1: Blue, 2: Red, 3: Gold): "))
if choice == 1:
    print("🎉 Confetti explodes everywhere! You grab the data!")
elif choice == 2:
    print("🚨 Sirens blare, but your super speed saves the day!")
elif choice == 3:
    print("🏆 The vault slides open silently. Flawless victory!")
else:
    print("💥 You karate-kick the door open!")

# Phase 5: Victory!
print("\n========================================")
print(f"MISSION COMPLETE! Agent {agent_name} Wins!")
print(f"Final Energy Score: {energy}")
print("========================================")
```

---

### 🏅 Agent Ali's Badge of Honor

When you finish and run your code in the console, you have officially graduated to **Python Level 2: Game Coder**! 🎖️

👉 **Next Lesson:** [[Lesson 6 -- While Loops and Game Loops]]
