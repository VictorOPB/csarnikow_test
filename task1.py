import matplotlib.pyplot as plt

# Pseudo-random number generator parameters (LCG method)
seed = 42
a = 1664525
c = 1013904223
m = 2**32

def random_number(seed):
    global a, c, m
    seed = (a * seed + c) % m
    return seed

def movavg(f, w):
    moving_averages = []
    for i in range(len(f) - w + 1):
        window = f[i:i + w]
        moving_averages.append(sum(window) / w)
    return moving_averages

# Generate a time series
num_points = 100
time_series = [i if i <= num_points / 2 else num_points - i for i in range(num_points)]

# Manually create white noise with the desired amplitude
noise_amplitude = 5

# Seed the pseudo-random number generator
rng_seed = seed

white_noise = []
for _ in range(num_points):
    rng_seed = random_number(rng_seed)
    noise = (rng_seed / m) * 2 * noise_amplitude - noise_amplitude # Rescaling the white noise to the desired amplitude
    white_noise.append(noise)

noisy_series = [value + noise for value, noise in zip(time_series, white_noise)]

# Set the window length for the moving average
window_length = 10

# Calculate simple moving average
smoothed_series = movavg(noisy_series, window_length)

# Plot the original time series and the moving average
if __name__ == '__main__':
    plt.figure(figsize=(10, 6))
    plt.plot(range(num_points), noisy_series, label='Noisy Time Series', color='black', alpha=0.7)
    plt.plot(range(window_length - 1, num_points), smoothed_series,
             label=f'Moving Average (w={window_length})', color='red', linewidth=2)
    plt.xlabel('Time (s)')
    plt.ylabel("Series' Values")
    plt.title('Moving Average on Triangular Time Series with Noise')
    plt.legend()
    plt.grid(True)
    plt.show()
