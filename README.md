# python_project_4
# explanation video 
link:

# 📊 Data Analyzer and Transformer Program

> Turn raw numbers into clear insights — with pure Python.

A lightweight, beginner-friendly CLI tool to **input**, **summarize**, **filter**, and **transform** 1D numeric datasets. Built with only Python built-ins + recursion. No external dependencies.

---

## ✨ Features

- **1D Array Input** — Enter space-separated numbers in one go
- **Instant Summary** — Count, Min, Max, Sum, Average using Python built-ins
- **Recursive Factorial** — Classic recursion demo built-in
- **Data Filtering** — Filter values by condition (even / odd / greater than X)
- **Data Transformation** — Map operations like square, cube, double
- **Zero Dependencies** — Runs on any Python 3.x

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher

### Run

```bash
python data_analyzer.py
```

---

## 🧩 Menu Overview

```
1. Input Data
2. Display Summary
3. Filter Data
4. Transform Data
5. Factorial Calculator
6. Exit
```

---

## 💡 Usage Example

```
Enter data for a 1D array (separated by spaces): 5 10 15 20 25

Data has been stored successfully!

Data Summary:
- Total elements: 5
- Minimum value: 5
- Maximum value: 25
- Sum of all values: 75
- Average value: 15.0
```

---

## 🛠️ Functions

| Function | Description |
|---|---|
| `input_data()` | Takes space-separated integers from user and stores in `data` |
| `display_summary()` | Shows total, min, max, sum, average using `len()`, `min()`, `max()`, `sum()` |
| `factorial(n)` | Recursive factorial: `n * factorial(n-1)` |
| `filter_data()` | Returns subset based on condition (e.g. `x % 2 == 0`) |
| `transform_data()` | Applies lambda/map operation to each element |

---

## 🧠 Concepts Used

- Global variables & functions
- List comprehension
- Built-in functions: `len`, `min`, `max`, `sum`, `round`
- Recursion
- `map()` / `filter()` with `lambda`

---

## 📈 Sample Transformations

- Square: `[x**2 for x in data]`
- Even filter: `[x for x in data if x % 2 == 0]`
- Normalize: `[(x - min(data)) / (max(data) - min(data)) for x in data]`

---

## 🤝 Contributing

1. Fork the repo
2. Create a branch: `git checkout -b feature-name`
3. Commit: `git commit -m "Add feature"`
4. Push and open a PR

---

## 📄 License

MIT License — free to use and modify.

---

Made with ❤️ in Python
