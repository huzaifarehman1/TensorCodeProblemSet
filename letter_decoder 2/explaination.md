# Letter Decoder 2 - Explanation

## Problem Understanding

The goal is to recover the original letter from the output of a fixed neural network.

The input to the network is a sparse vector of size 26:

```
0 → A
1 → B
2 → C
...
25 → Z
```

Only one value is non-zero.

For example:

```
A with value 5:

[5,0,0,0,...,0]

C with value 2:

[0,0,2,0,...,0]
```

The position of the non-zero value represents the letter, while the value itself is an unknown positive number.

The neural network is:

```
Input(26)
    ↓
Linear(128, bias=False)
    ↓
ReLU
    ↓
Linear(50, bias=False)
    ↓
Output(50)
```

The model uses:

```python
torch.manual_seed(35)
```

so the weights are fixed and can be recreated exactly.

---

# Key Observation

The network has no biases:

\[
f(x)=W_2(ReLU(W_1x))
\]

This gives the network a useful property called **positive homogeneity**.

For positive values:

\[
ReLU(ax)=aReLU(x)
\]

Therefore:

\[
f(ax)=af(x)
\]

This means if we know the output for a letter with input value `1`, we can generate the output for any other positive value by simply multiplying.

---

# Creating Letter Fingerprints

For every letter, we create a one-hot vector:

Example for letter C:

```
[0,0,1,0,...,0]
```

Then pass it through the network:

\[
v_i=f(e_i)
\]

where:

- \(e_i\) is the one-hot vector of letter `i`
- \(v_i\) is the fingerprint of that letter

We store 26 fingerprints:

```
fingerprint[0] → A
fingerprint[1] → B
...
fingerprint[25] → Z
```

---

# Why Cosine Similarity Is Not Optimal

A common approach is cosine similarity:

sim = cos(A,B)/(|A|*|B|)

Cosine only checks the direction of vectors.

For example:

```
[1,2,3]

[10,20,30]
```

have cosine similarity 1 because they point in the same direction.

However, cosine completely ignores the magnitude.

In this problem, the magnitude contains information about the unknown input value, so ignoring it can cause confusion between similar fingerprints.

---

# Reconstruction Approach

For a test output vector:

\[
y
\]

we know that:

\[
y=a(f_i)
\]

where:

- \(f_i\) is a fingerprint
- \(a\) is the unknown positive input value

For every possible letter, we find the best value of \(a\).

We want:

 
||y-a(f_i)||^2


to be as small as possible.

The optimal scale factor comes from calculas is here:

a = dot product(y,f_i) / dot product(f_i,f_i)

This gives the multiplier that makes the fingerprint closest to the test output.

---

# Prediction Process

For each test sample:

1. Try every possible letter.
2. Take its fingerprint.
3. Calculate the optimal scale:

a = dot product(y,f_i) / dot product(f_i,f_i)

4. Reconstruct the output:

y = a*f_i

5. Calculate reconstruction error:

\[
error = ||sample - y||^2
\]

6. Select the letter with the smallest error.

The correct letter should produce an almost zero reconstruction error.

---

# Why This Works

The network structure guarantees:

\[
f(ax)=af(x)
\]

because:

- Linear layers have no bias
- ReLU preserves positive scaling

Therefore every letter creates a unique direction in the 50-dimensional output space.

The task becomes finding which fingerprint direction generated the output and recovering the unknown scale.

This method uses both:

- direction information
- magnitude information

making it more accurate than cosine similarity.