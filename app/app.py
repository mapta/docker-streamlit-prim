import itertools

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st


# From Python Cookbook
def erat2( ):
    D = {  }
    yield 2
    for q in itertools.islice(itertools.count(3), 0, None, 2):
        p = D.pop(q, None)
        if p is None:
            D[q*q] = q
            yield q
        else:
            x = p + q
            while x in D or not (x&1):
                x += p
            D[x] = p

def get_primes_erat(n):
  return list(itertools.takewhile(lambda p: p<n, erat2()))

def get_prime_distribution(n):
    hist, bins = np.histogram(get_primes_erat(n), bins=np.linspace(1.5, n-0.5, n-1))
    prime_count = np.cumsum(hist)
    return prime_count

max_int = 1000
df = pd.DataFrame()
integers = list(range(2, max_int))
df['Integers'] = integers
df['Prime Counting Function'] = integers/np.log(integers)
df['Number of Primes'] = get_prime_distribution(max_int)

st.title("Prime Number Theorem")

quote = "_In number theory, the prime number theorem (PNT) describes the asymptotic distribution of the prime numbers among the positive integers. It formalizes the intuitive idea that primes become less common as they become larger by precisely quantifying the rate at which this occurs._"
st.markdown(quote)

fig, ax = plt.subplots()
ax.plot(df['Integers'], df['Prime Counting Function'], 'k-', label='Prime Counting Function')
ax.plot(df['Integers'], df['Number of Primes'], 'b-', label='Actual Number of Primes')
ax.legend()
ax.set_xlabel("n")

st.pyplot(fig)