# 🧩 Python Functions — Introduction

---

## 🔹 Definition

A **function** in Python is a **block of reusable code** that performs a specific task.

✅ It allows you to **group related statements** together.  
✅ You can **call** the function whenever you need it, instead of rewriting the same code.

---

## 🧠 Advantages of Functions

```
Code Reusability  
Improved Modularity  
```

- **Code Reusability** → You can reuse the same logic multiple times.  
- **Modularity** → Divides the program into smaller, logical parts, making it easier to read and maintain.  

---

## 🔸 Types of Functions in Python

| Type | Description | Example |
|-------|-------------|----------|
| **Built-in Functions** | Functions already defined by Python | `print()`, `min()`, `max()`, `len()`, `input()` |
| **User-defined Functions** | Functions created by the user as per requirement | `add()`, `display()`, `greetings()` |

---

### 1️⃣ Built-in Functions
These are predefined functions that come with Python.  
You just need to use them — no need to define.

```python
print("Hello World")

num = int(input("Enter a number: "))
print("Minimum:", min(10, 20, 5))
print("Maximum:", max(10, 20, 5))
```

---

### 2️⃣ User-defined Functions

These are functions that **you define** to perform specific tasks.

📘 **Syntax:**
```python
def function_name(parameters):
    # body of the function
    statement(s)
```

---

## 🔹 Why Use Functions?

If you need to **execute the same code multiple times**,  
instead of writing it again and again — define it once as a **function**.

### Example (Without Function)
```python
a = 10
if a % 2 == 0:
    print('Even')
else:
    print('Odd')

b = 20
if b % 2 == 0:
    print('Even')
else:
    print('Odd')

c = 30
if c % 2 == 0:
    print('Even')
else:
    print('Odd')
```

🔸 The above code repeats the same logic 3 times.

---

### Example (Using Function)
```python
def Even_Odd(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

Even_Odd(10)
Even_Odd(13)
Even_Odd(24)
```

✅ Output:
```
Even
Odd
Even
```

---

# 🧩 Python `eval()` Function

## 🔹 Definition
`eval()` evaluates a string expression as Python code and returns the result.
Syntax:
    eval(expression, globals=None, locals=None)

---

## 🔹 Purpose
✅ Evaluate Python expressions dynamically  
✅ Convert string input → actual data types  
✅ Perform runtime computations  

---

## 🔹 Examples
x = 5
print(eval('x + 10'))          # 15
print(eval('10 + 20 * 3'))     # 70
print(eval('len([1,2,3])'))    # 3

---

## 🔹 With Input
a = input("Enter: ")       # "[1,2,3]" → string
b = eval(input("Enter: ")) # [1,2,3] → list

| Function | Output Type | Safe? |
|-----------|--------------|-------|
| input() | Always string | ✅ |
| eval(input()) | Depends on input | ⚠️ Risky |

---

## 🔒 Security Warning
⚠️ `eval()` executes arbitrary code — do not use with untrusted input.
Example:
    eval("__import__('os').system('rm -rf /')")  # 🚫 Dangerous!

---

## 🔹 Safe Alternative
Use `ast.literal_eval()` for safe parsing of literals only.
    import ast
    data = ast.literal_eval(input("Enter: "))  # Safe
    print(data, type(data))

---

## 🔹 Collections Examples

| Type | Example Input | Output Type |
|------|----------------|-------------|
| List | [1,2,3] | <class 'list'> |
| Tuple | (1,2,3) | <class 'tuple'> |
| Set | {1,2,3} | <class 'set'> |
| Dict | {'a':1, 'b':2} | <class 'dict'> |

---

## ✨ Key Takeaways
- `eval()` executes a string as Python code  
- Very powerful but unsafe if misused  
- Prefer `ast.literal_eval()` for safe literal conversion  

💡 "Use `eval()` wisely — dynamic, but dangerous!" 🐍
