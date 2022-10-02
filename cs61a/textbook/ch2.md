# Chapter 2: Building Abstractions with Data

## 2.1 Introduction

### 2.1.1 Native Data Types

> Values that share a class also share behavior.

- What is literals?
  - [useful answer](https://ithelp.ithome.com.tw/articles/10271062?sc=iThomeR)
  - There are expressions that evaluate to values of native types, called literals.
  - There are built-in functions and operators to manipulate values of native types.

## 2.3 Sequences

- A sequence is an ordered collection of values.
  - Length
  - Element Selection

### 2.3.1 Lists

- For sequences, addition and multiplication do not add or multiply elements, but instead combine and replicate the sequences themselves.

### 2.3.2 Sequence Iteration

```
for <name> in <expression>:
    <suite>
```

- Evaluate the header expression, which must yield an iterable value.
- For each element value in that iterable value, in order:
  - Bind name to that value in the current frame.
  - Execute the suite.
- Sequence Unpacking
- Ranges
  - A range is another built-in type of sequence in Python, which represents a range of integers.

### 2.3.3 Sequence Processing

- List Comprehensions
  - In Python, a list comprehension is an expression that performs such a computation.
- Aggregation
- Higher-Order Functions
- Conventional Names
  - apply_to_all -> map
  - keep_if -> filter

```py
# List Comprehensions
[<map expression> for <name> in <sequence expression> if <filter expression>]
>>> [x+1 for x in odds]
>>> [x for x in odds if 25 % x == 0]
# Aggregation
[1] + [x for x in range(2, n) if n % x == 0]
# Conventional Names
filter = lambda filter_fn, s: [x for x in s if filter_fn(x)]
filter = lambda filter_fn, s: list(filter(filter_fn, s))
```

### 2.3.4 Sequence Abstraction

- satisfy length and element selection
- e.g. list, range
- more behavior
  - Membership: x in arr
  - Slicing: A slice of a sequence is any contiguous span of the original sequence, designated by a pair of integers.

### 2.3.5 Strings

The native data type for text in Python is called a string, and corresponds to the constructor str.

- Membership
  - It matches substrings rather than elements.
- Multiline Literals
  - \n (pronounced "backslash en") is a single element that represents a new line.
- String Coercion
  - A string can be created from any object in Python by calling the str constructor function with an object value as its argument.
