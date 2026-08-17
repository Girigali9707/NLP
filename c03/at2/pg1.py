import math

# Given counts
C_data = 3
C_data_science = 3
C_science_is = 2
C_science_drives = 1
C_data_science_is = 2

# 1. MLE Bigram
p_science_data = C_data_science / C_data
print("1. P(science | data) =", p_science_data)

# 2. Backoff for "data science improves"
# improves is not present in corpus
p_improves = 0
print("2. P(data science improves) =", p_improves)

# 3. Deleted Interpolation
lambda1 = 0.5
lambda2 = 0.3
lambda3 = 0.2

# Trigram probability
p_tri = C_data_science_is / C_data_science

# Bigram probability
p_bi = C_science_is / 3

# Unigram probability of "is"
p_uni = 2 / 12

p_interpolation = (
    lambda1 * p_tri +
    lambda2 * p_bi +
    lambda3 * p_uni
)

print("3. Interpolated probability =", round(p_interpolation, 3))

# 4. Entropy
p_is = 0.66
p_drives = 0.33

entropy = -(p_is * math.log2(p_is) +
            p_drives * math.log2(p_drives))

print("4. Entropy =", round(entropy, 3), "bits")