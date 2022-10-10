"""
A program to verify the truth of the statement ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z for all predicate values.

A predicate in programming is an expression that uses one or more values with the result of a Boolean type.
Predicates, just like utterances, take on two meanings: true and false, so all operations of propositional
logic apply to them.
"""
values_combinations = [
    [0,0,0],
    [0,0,1],
    [0,1,0],
    [0,1,1],
    [1,0,0],
    [1,0,1],
    [1,1,0],
    [1,1,1],
]

# ¬(X ⋁ Y ⋁ Z) +
results_1 = list()

# ¬X ⋀ ¬Y ⋀ ¬Z *
results_2 = list()

print('| x | y | z | ¬(X ⋁ Y ⋁ Z) |  ¬X ⋀ ¬Y ⋀ ¬Z |')

for x, y, z in values_combinations:
    expression_1 = not(x or y or z)
    expression_2 = not x and not y and not z
    results_1.append(expression_1)
    results_2.append(expression_2)

    print(f'| {x} | {y} | {z} |    {expression_1}     |    {expression_2}     |')

print(f"The statement ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z  is {results_1 == results_2}.")
