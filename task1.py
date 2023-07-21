import matplotlib.pyplot as plt
import random # Built-in module for generating random numbers

def movavg(f, w):
  moving_averages = []
  for i in range(len(f) - w + 1):
      window = f[i:i + w]
      moving_averages.append(sum(window) / w)
  return moving_averages

# Generate a time series
num_points = 100
time_series = [i if i <= num_points/2 else num_points - i for i in range(num_points)]

# Add manual noise to the triangular time series
noise_amplitude = 5
noisy_series = [value + random.uniform(-noise_amplitude, noise_amplitude) for value in time_series]

# Set the window length for the moving average
window_length = 10

# Calculate simples moving average
smoothed_series = movavg(noisy_series, window_length)

# Plot the original time series and the moving average
if __name__ == '__main__':
  plt.figure(figsize=(10, 6))
  plt.plot(range(num_points), noisy_series, label='Noisy Time Series', color='black', alpha=0.7)
  plt.plot(range(window_length - 1, num_points), smoothed_series, label=f'Moving Average (w={window_length})', color='red', linewidth=2)
  plt.xlabel('Time (s)')
  plt.ylabel("Series' Values")
  plt.title('Moving Average on Triangular Time Series with Noise')
  plt.legend()
  plt.grid(True)
  plt.show()
