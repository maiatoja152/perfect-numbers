# Perfect Numbers
A small project I made after I became curious about [perfect numbers](https://en.wikipedia.org/wiki/Perfect_number) while reading about them in the textbook [How to Prove It: A Structured Approach](https://www.amazon.ca/How-Prove-Structured-Daniel-Velleman/dp/1108439535). Check if numbers are perfect or [amicable](https://en.wikipedia.org/wiki/Amicable_numbers) (a similar concept to perfect numbers), or efficiently search for perfect numbers using [Mersenne primes](https://en.wikipedia.org/wiki/Mersenne_prime).

## Usage
- Efficiently search for perfect numbers using Mersenne primes and the [Lucas-Lehmer primality test](https://en.wikipedia.org/wiki/Lucas%E2%80%93Lehmer_primality_test) in a range of *p* values. Mersenne numbers are calculated using the formula *2^(p-1)(2^p-1)*.

        python3 perfect-numbers.py perfect-search *lower_p* *upper_p*

- Check if numbers are perfect.

        python3 perfect-numbers.py perfect *numbers...*

- Check if a pair of numbers is amicable.

        python3 perfect-numbers.py amicable *num1* *num2*
