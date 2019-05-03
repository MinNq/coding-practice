# Adaptive mutation
I implemented an adaptive mutation rate schedule. The mutation rate will be tuned a little bit higher when a decrease in best-performance is detected and vice versa, starting from generation 5. This will eventually keep the mutation rate at around 0.3, which is a good rate for <code>n_weights = 10</code>.

# Notes

*  Repeated best performance after some generations doesn't always mean that the pool is lacking diversity and mutations. It just implies that there hasn't been any better individual to overtake the position of the current best (and uncrossovered, unmutated) individual yet.

*  Bigger population seems to improve the chance of having better results. This can best be observed at small population scale (e.g. 10, 20, 50, etc.)

# Some examples:

[Google Colab notebook]

![example 1][genetic_1]
![example 2][genetic_2]
![example 3][genetic_3]

[Google Colab notebook]: https://colab.research.google.com/drive/13FsDH_H3gL61crzzzssWE9admT-HDqR3
[genetic_1]: https://github.com/MinNq/CFS/blob/master/Genetic%20Linear%20Regression/genetic_1.png
[genetic_2]: https://github.com/MinNq/CFS/blob/master/Genetic%20Linear%20Regression/genetic_2.png
[genetic_3]: https://github.com/MinNq/CFS/blob/master/Genetic%20Linear%20Regression/genetic_3.png
