⬅️ [[Introduction to Python]] | ➡️ [[Lesson 2 -- Talking to Python with Input]]

---

### Print

In python you get output in a textbox named Console. Here is one image of it:

![[Pasted image 20260919142258.png]]

To get something in this black box of text, you need to use the print function:

```python
print()
```

This function takes whatever it has inside it and puts it inside the black box for you to see.

### Data Types

There are 4 main data types in python:

String: A string in python is whatever is inside quotation marks, doesn't matter what's inside. ex: 

```python
"Hello User4592@#$^&*"
```

Integer: An integer in python is a whole number without any decimals. ex:

```python
53
```

Float: Float in python is a number with decimals. ex:

```python
53.01
```

Boolean: Boolean in python means True or False. ex:

```python
is_game_active = True
is_game_over = False
```

### Variables

Variables are like a container in Python — they store data and values so you can use them whenever you want! A variable can have almost any name, but it must follow 3 golden rules:

1. **Cannot start with a number**: You cannot name a variable `1player`, but you CAN name it `player1` or `num1`!
2. **No spaces or special characters**: You cannot use `!@#$%^&*` or spaces in a variable name.
3. **Follow a naming style**: In Python, programmers love using [[Snake Case or Camel Case]] to connect multiple words together (like `hero_name` or `superPower`).

Example of variables in action:

```python
num1 = 6
num2 = 5
print(num1 + num2)
```

Here `num1` and `num2` are variables. They store the numbers 6 and 5, and Python adds them together to print `11`!

---

### Arithmetic Operators

Arithmetic operators are the math symbols you use to do calculations in Python. Here are the 4 main ones:

1. **Addition (`+`)**: Adds numbers together.
2. **Subtraction (`-`)**: Subtracts one number from another.
3. **Multiplication (`*`)**: Multiplies numbers (in Python we use the asterisk `*` symbol!).
4. **Division (`/`)**: Divides numbers.

Let's test all four math superpowers:

```python
# Addition
print(10 + 5)   # Output: 15

# Subtraction
print(20 - 8)   # Output: 12

# Multiplication
print(4 * 5)    # Output: 20

# Division
print(50 / 2)   # Output: 25.0
```

---

### The Task: 🎯 Ali's Super Agent Identity Card

Now it's your turn to write real Python code, Ali! Open your Python editor and complete this mission:

1. Create a variable called `agent_name` and set it to `"Agent Ali"`.
2. Create a variable called `agent_age` and set it to your age (`10`).
3. Create a variable called `gadget_power` and set it to `100`.
4. Use `print()` to display your agent details on the console.
5. Create a variable `power_boost` with value `50`. Calculate your boosted power using `gadget_power + power_boost` and print the result!

> [!tip] Hint
> Your code can look something like this:
> ```python
> agent_name = "Agent Ali"
> agent_age = 10
> print(agent_name)
> print(agent_age)
> 
> gadget_power = 100
> power_boost = 50
> print(gadget_power + power_boost)
> ```

---

⬅️ **Previous:** [[Introduction to Python]] | ➡️ **Next Lesson:** [[Lesson 2 -- Talking to Python with Input]]

