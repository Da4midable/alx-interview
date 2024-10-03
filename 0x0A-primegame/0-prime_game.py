#!/usr/bin/python3
"""
This module defines the isWinner function to determine the winner of a game
played between Maria and Ben, where they take turns picking prime numbers from
a set and removing that prime and its multiples. Maria always plays first,
and both play optimally. The player that cannot make a move loses the game.

The function returns the name of the player who won the most rounds, or None
if the winner cannot be determined.
"""


def isWinner(x, nums):
    """
    Determines the winner after x rounds of the prime-number removal game.

    Args:
        x (int): The number of rounds played.
        nums (list): A list of integers where each element represents the
                     maximum number in the set for that round.

    Returns:
        str: "Maria" if Maria wins more rounds, "Ben" if Ben wins more rounds,
             or None if neither player wins more rounds.
    """

    def sieve_of_eratosthenes(max_n):
        """
        Generates list of boolean values indicating prime numbers up to max_n.

        Args:
            max_n (int): The maximum number to check for primality.

        Returns:
            list: A list where index i is True if i is prime, False otherwise.
        """
        is_prime = [True] * (max_n + 1)
        is_prime[0], is_prime[1] = False, False
        for i in range(2, int(max_n ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, max_n + 1, i):
                    is_prime[j] = False
        return is_prime

    if x <= 0 or not nums:
        return None

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n < 2:
            ben_wins += 1
            continue

        prime_count = 0
        for i in range(2, n + 1):
            if primes[i]:
                prime_count += 1

        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
