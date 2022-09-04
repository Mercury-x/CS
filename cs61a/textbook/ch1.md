# Chapter 1

## 1.2 Elements of Programing

### 1.2.4 Names and the Enviroment

> Assignment is our simplest means of abstraction, for it allows us to use simple names to refer to the results of compound operations, such as the area computed above. In this way, complex programs are constructed by building, step by step, computational objects of increasing complexity.

> The possibility of binding names to values and later retrieving those values by name means that the interpreter must maintain some sort of memory that keeps track of the names, values, and bindings. This memory is called an environment.

> When executing an assignment statement, Python evaluates the expression to the right of = before changing the binding to the name on the left. Therefore, one can refer to a name in right-side expression, even if it is the name to be bound by the assignment statement.

```py
# so the expression like:
x = y = z = 1
# is valid in python, because python will evaluate the right expression before changing the bind of left
# and the assignment is just a operation that changing bind.
>>> x = y = z = 1
>>> x, y, z = 1, 2, 3
>>> x, y, z
(1, 2, 3)
```

> Apply the function that is the value of the operator subexpression to the arguments that are the values of the operand subexpressions.

### 1.2.6 The Non-Pure Print Function

> Pure functions. Functions have some input (their arguments) and return some output (the result of applying them). Pure functions have the property that applying them has no effects beyond returning a value. Moreover, a pure function must always return the same value when called twice with the same arguments.

> Non-pure functions. In addition to returning a value, applying a non-pure function can generate side effects, which make some change to the state of the interpreter or computer.

so Non-pure functions can not be used effectivefly in nested expressions.

> In computer science, an operation, function or expression is said to have a side effect if it modifies some state variable value(s) outside its local environment, which is to say if it has any observable effect other than its primary effect of returning a value to the invoker of the operation.
