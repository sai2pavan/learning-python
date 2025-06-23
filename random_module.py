Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

======== RESTART: C:\Users\PAVAN\Desktop\python_work\random_practise.py ========
=== random.seed() Demo ===

1. Without setting a seed:
Random number: 55
Random number: 48
Random number: 98

Each time you run this, you get different numbers.

2. Now let's use random.seed(42):
Random number: 82
Random number: 15
Random number: 4

These numbers will be the SAME every time you run it.
3. Let's reset the seed to 42 again:
Random number again: 82
Random number again: 15
Random number again: 4

See? Same numbers again — seed 'locks in' the randomness.
4. Now using a different seed (123):
Random number with seed 123: 7
Random number with seed 123: 35
Random number with seed 123: 12

Different seed = different sequence.
5. Finally, setting no seed again:
Fresh random number: 35
Fresh random number: 2
Fresh random number: 26

Back to random each time you run it.

=== Summary ===
- random.seed(n) makes random predictable (reproducible)
- Use it when testing, debugging, or doing simulations
- Don't use it if you want fresh randomness every time
