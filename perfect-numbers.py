import argparse
import math
import multiprocessing


def get_sum_of_lesser_divisors(num: int) -> int:
    assert num > 0
    if num == 1:
        return 0

    total = 1
    for i in range(2, math.isqrt(num) + 1):
        if num % i == 0:
            factor = num // i
            total += i
            # Do not add the factor in the case of a perfect square
            if i != factor:
                total += factor
    return total


def is_perfect_number(num: int) -> bool:
    return get_sum_of_lesser_divisors(num) == num


def are_amicable_numbers(num1: int, num2: int) -> bool:
    return get_sum_of_lesser_divisors(num1) == num2 \
        and get_sum_of_lesser_divisors(num2) == num1


def is_prime(num: int) -> bool:
    if num < 2:
        return False

    for i in range(2, math.isqrt(num) + 1):
        if num % i == 0:
            return False
    return True


def lucas_lehmer_primality_test(p: int) -> bool:
    mersenne_num = 2 ** p - 1
    s = 4
    for _ in range(p - 2):
        s = (s ** 2 - 2) % mersenne_num
    return s == 0


def check_mersenne_prime(p: int) -> tuple[int, bool]:
    if is_prime(p):
        # Lucas-Lehmer primality test is only defined for p > 2
        if p == 2 or lucas_lehmer_primality_test(p):
            return (p, True)
    
    return (p, False)


def perfect_search(lower_p: int, upper_p: int) -> None:
    print(f"Searching for perfect numbers for {lower_p} <= p <= {upper_p}...")
    with multiprocessing.Pool() as pool:
        results = pool.map(check_mersenne_prime, range(lower_p, upper_p + 1))

    numbers_found = 0
    for p, is_mersenne_prime in results:
        if is_mersenne_prime:
            # Display the perfect number or only the formula if it's too large.
            if p <= 100:
                perfect_number = str(2 ** (p - 1) * (2 ** p - 1))
            else:
                perfect_number = f"2^({p}-1)(2^{p}-1)"
            print(f"Perfect number found at p={p}:", perfect_number)
            numbers_found += 1
    print(numbers_found, "perfect numbers found.")


def process_perfect_args(args: argparse.Namespace) -> None:
    for num in args.numbers:
        print(num, is_perfect_number(num))


def process_amicable_args(args: argparse.Namespace) -> None:
    print(are_amicable_numbers(*args.numbers))


def process_perfect_search_args(args: argparse.Namespace) -> None:
    if args.lower_p >= args.upper_p:
        raise ValueError("lower_p must be less than upper_p")
    perfect_search(args.lower_p, args.upper_p)


def positive_integer(user_input: str) -> int:
    integer = int(user_input)
    if integer <= 0:
        raise ValueError("Must be a positive integer.")
    return integer

def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check if numbers are perfect or amicable, or search for perfect numbers.",
    )
    subparsers = parser.add_subparsers(required=True)

    parser_perfect = subparsers.add_parser(
        "perfect",
        description="Check if numbers are perfect.",
    )
    parser_perfect.add_argument("numbers", type=positive_integer, nargs="+")
    parser_perfect.set_defaults(function=process_perfect_args)

    parser_amicable = subparsers.add_parser(
        "amicable",
        description="Check if a pair of numbers is amicable.",
    )
    parser_amicable.add_argument("numbers", type=positive_integer, nargs=2)
    parser_amicable.set_defaults(function=process_amicable_args)

    parser_perfect_search = subparsers.add_parser(
        "perfect-search",
        description="Search for perfect numbers within a range of Mersenne numbers (2^p-1).",
    )
    parser_perfect_search.add_argument("lower_p", type=positive_integer)
    parser_perfect_search.add_argument("upper_p", type=positive_integer)
    parser_perfect_search.set_defaults(function=process_perfect_search_args)
    
    return parser.parse_args()


args: argparse.Namespace = get_args()
args.function(args)