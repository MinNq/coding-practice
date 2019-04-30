One day, I just thought that, I should try doing Linear Regression with a Genetic Algorithm instead of Gradient Descent. That idea turns out to be unexpectedly terrible. A tip for you fellow coders: never use GA for LR.

See my painful example [here].

I actually did modify the vanilla GA with an adaptive scheme for mutation rate. It will get slightly lower when the performance gets better and vice versa. However, regrardless of method used, best individuals are often found in the first or early generations and the pool seems not to evolve at all. Maybe it's because of insufficient number of weights, iteration, or population.

And again, GA might be a good approach to some problem, but not this one.

[here]: https://colab.research.google.com/drive/1GWkg1rqtwzGM3_3_xKg-T0gwKOeAGvQk
