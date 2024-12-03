# Advent of Code - 2024

## Brief

This is my attempt to learn [clojure](https://clojure.org/) language. I will try to solve the problems using clojure and will try to incorporate unit tests.

The solution will roughly follow this structure:

```txt
<day>
  ├── input
  |   ├── sample.in
  │   └── star.in
  ├── src
  |   ├── main.clj (for getting the input)
  │   └── calc.clj (for the solution)
  └── test
      └── main.clj (for testing the main.clj)
```

## Other Language

This is my attempt to solve using Googhe Sheets. The sheet can be found [here](https://docs.google.com/spreadsheets/d/1J0_s6Qru7S0bcDWFz4C_9dLVCnyoUltKFkDm2KEm9TA)

## Learnings

### Day 1

- Installing clojure, setting up IDE, and familiarize with clojure REPL
- Reading input from file
- Separating into different files
- Unit test in clojure
- `map`, `reduce`, `apply`, `def`, `defn`, `let`
- basic math, basic string manipulation

### Day 2

- Reading 2D vector from file
- Use `for` to iterate over the vector and do brute force

### Day 3

- Regex operations `re-find`, `re-matcher`, `re-seq`
- Using `loop` and `recur` for basic recursion
