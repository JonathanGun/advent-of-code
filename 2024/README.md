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

This is my attempt to solve using Googhe Sheets. The sheet can be found in this list:
* [Day 1 - Day 4](https://docs.google.com/spreadsheets/d/1J0_s6Qru7S0bcDWFz4C_9dLVCnyoUltKFkDm2KEm9TA)
* [Day 5](https://docs.google.com/spreadsheets/d/1cUUujvuAzJt4X-iOSZlPNawLPMGgD1FNMVPLfEHIvBs)
* [Day 13](https://docs.google.com/spreadsheets/d/1E6joo-I5f8YErVa0WhSB6Aaiy5w3jmh9HwfdeNORaoQ)

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

### Day 4

- `get-in` function to access 2D vector
- `atom` to create mutable variable
- `swap!` to change the value of atom

### Day 5

- `sort` and `sort-by` function, using custom comparator
- set operations like `clojure.set/intersection`, `clojure.set/difference`, `clojure.set/union`
