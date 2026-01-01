import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# --- 1. Generate random stock price data ---
np.random.seed(42)
n = 200
price = np.cumsum(np.random.normal(loc=0.1, scale=1, size=n)) + 100
dates = pd.date_range(start="2023-01-01", periods=n)
df = pd.DataFrame({'Close': price}, index=dates)

# --- 2. Calculate EMAs ---
df['EMA50'] = df['Close'].ewm(span=50).mean()
df['EMA100'] = df['Close'].ewm(span=100).mean()

# --- 3. Determine trend ---
if df['EMA50'].iloc[-1] > df['EMA100'].iloc[-1]:
    trend = 'bullish'
    color_fib = 'yellow'
    # Structural low to high
    swing_low_idx = df['Close'].idxmin()
    swing_high_idx = df.loc[swing_low_idx:].idxmax()[0]
else:
    trend = 'bearish'
    color_fib = 'yellow'
    # Structural high to low
    swing_high_idx = df['Close'].idxmax()
    swing_low_idx = df.loc[swing_high_idx:].idxmin()[0]

swing_low = df.loc[swing_low_idx, 'Close']
swing_high = df.loc[swing_high_idx, 'Close']

# Fibonacci 61.8% level
fib_618 = swing_high - (swing_high - swing_low) * 0.618 if trend == 'bullish' else swing_low + (swing_high - swing_low) * 0.618

# --- 4. Plotting ---
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(14, 6))

# Price & EMAs
ax.plot(df.index, df['Close'], color='white', label='Price', linewidth=1.2)
ax.plot(df.index, df['EMA50'], color='red', label='50 EMA')
ax.plot(df.index, df['EMA100'], color='blue', label='100 EMA')

# Fibonacci lines
ax.axhline(fib_618, color=color_fib, linestyle='--', label='Fib 61.8%')

# Signal arrows
signal_idx = df.index[-1]
signal_price = fib_618

if trend == 'bullish':
    ax.annotate('Buy Signal',
                xy=(signal_idx, signal_price),
                xytext=(signal_idx, signal_price + 2),
                arrowprops=dict(facecolor='green', shrink=0.05),
                color='green', fontsize=10)
else:
    ax.annotate('Sell Signal',
                xy=(signal_idx, signal_price),
                xytext=(signal_idx, signal_price - 2),
                arrowprops=dict(facecolor='red', shrink=0.05),
                color='red', fontsize=10)

# Labels & Layout
ax.set_title(f"Trend: {trend.upper()} | Fibonacci Retracement Signal", fontsize=14)
ax.set_ylabel("Price")
ax.set_xlabel("Date")
ax.legend()
ax.grid(True, linestyle='--', alpha=0.3)
plt.tight_layout()
plt.show()
