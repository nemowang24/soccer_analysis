from scipy.stats import poisson

#Question 2 (b)

lam = 1200
k=1000
prob_cdf = poisson.cdf(k, lam)
print(f"The probability to have less than 1000 patient vists in the next day is {prob_cdf}\n")

#Question 2 (c)
print(f"There is {prob_cdf*365} days to expect have less than 1000 patient visits during each day")