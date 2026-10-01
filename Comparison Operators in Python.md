# ⚖️ Comparison Operators in Python

⬅️ Back to: [[Lesson 3 -- Making Decisions with If and Else]]

In Python, **comparison operators** are special symbols used to compare two things (like numbers, words, or variables).

Whenever you use a comparison operator, Python answers with a **Boolean**: either `True` or `False`!

---

### The 6 Comparison Super-Symbols

| Symbol | What It Means | Kid Example | Python Result |
| :---: | :--- | :--- | :---: |
| `==` | **Equal to** (Are they exactly the same?) | `5 == 5` | `True` |
| `!=` | **Not equal to** (Are they different?) | `5 != 10` | `True` |
| `>` | **Greater than** (Is left bigger?) | `10 > 3` | `True` |
| `<` | **Less than** (Is left smaller?) | `2 < 8` | `True` |
| `>=` | **Greater than or equal to** | `10 >= 10` | `True` |
| `<=` | **Less than or equal to** | `7 <= 5` | `False` |

---

### ⚠️ The Golden Trap: `=` vs `==`

This is the #1 mistake that beginners (and even grown-up programmers!) make:

- `=` (One equals sign): **Assigns** a value to a variable container.

```python
hero_health = 100  # "Set hero_health to 100!"
```

- `==` (Two equals signs): **Asks a question**: "Are these two things equal?"

```python
hero_health == 100  # "Is hero_health equal to 100? Yes (True) or No (False)?"
```

> [!tip] Memory Trick
> Think of `==` as two detective eyes 🧐 looking closely to see if both sides match!

---

### 🧪 Try It in Python

```python
score = 50

print(score == 50)  # Output: True
print(score > 100)  # Output: False
print(score < 80)   # Output: True
print(score != 0)   # Output: True
```

---

⬅️ Return to: [[Lesson 3 -- Making Decisions with If and Else]]
