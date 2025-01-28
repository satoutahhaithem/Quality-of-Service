import matplotlib.pyplot as plt

# Data from the text
data = [
    (0.0, 1.0, 2.99),
    (1.0, 2.0, 1.95),
    (2.0, 3.0, 1.93),
    (3.0, 4.0, 1.95),
    (4.0, 5.0, 1.93),
    (5.0, 6.0, 1.95),
    (6.0, 7.0, 1.95),
    (7.0, 8.0, 1.94),
    (8.0, 9.0, 1.94),
    (9.0, 10.0, 1.95),
    (10.0, 11.0, 1.95),
    (11.0, 12.0, 1.93),
    (12.0, 13.0, 1.96),
    (13.0, 14.0, 1.92),
    (14.0, 15.0, 1.95),
    (15.0, 16.0, 1.94),
    (16.0, 17.0, 1.95),
    (17.0, 18.0, 1.93),
    (18.0, 19.0, 1.96),
    (19.0, 20.0, 1.94),
    (20.0, 21.0, 1.95),
    (21.0, 22.0, 1.95),
    (22.0, 23.0, 1.93),
    (23.0, 24.0, 1.94),
    (24.0, 25.0, 1.94),
    (25.0, 26.0, 1.95),
    (26.0, 27.0, 1.94),
    (27.0, 28.0, 1.94),
    (28.0, 29.0, 1.96),
    (29.0, 30.0, 1.94),
    (30.0, 31.0, 1.95),
    (31.0, 32.0, 1.93),
    (32.0, 33.0, 1.93)
]

# Extracting time and bandwidth for plotting
time_intervals = [f"{start}-{end}" for start, end, _ in data]
bandwidth = [entry[2] for entry in data]

# Plotting Bandwidth over Time
plt.figure(figsize=(10, 6))
plt.plot(time_intervals, bandwidth, marker="o", color="blue", label="Bandwidth (Mbits/sec)")
plt.xlabel("Time Interval (seconds)")
plt.ylabel("Bandwidth (Mbits/sec)")
plt.title("Bandwidth Over Time")
plt.xticks(rotation=45)
plt.tight_layout()
plt.legend()
plt.show()
