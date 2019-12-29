# Genetic Linear Regression

My implementation of genetic algorithm for linear regression.

<!-- more -->

## Contents
- [Important Notes](#important-notes)
- [Examples](#examples)

## Important Notes

- Repeated best performance after some generations doesn't always mean that the pool is lacking diversity and mutations. It just implies that there hasn't been any better individual to overtake the position of the current best (and uncrossovered, unmutated) individual yet.

- Bigger population seems to improve the chance of having better results. This can best be observed at small population scale (e.g. 10, 20, 50, etc.)

## Examples:

![example 1][genetic_1]
![example 2][genetic_2]
![example 3][genetic_3]

[genetic_1]: genetic_1.png
[genetic_2]: https://github.com/MinNq/coding-practice/blob/master/Genetic%20Linear%20Regression/genetic_2.png
[genetic_3]: https://github.com/MinNq/coding-practice/blob/master/Genetic%20Linear%20Regression/genetic_3.png
