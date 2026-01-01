Forex Limit Order Book Simulation:

This project analyses real time foreign exchange market activity by studying the order book (the list of buy and sell orders). It looks at how prices move based on supply and demand and uses data analysis to identify patterns that may help with trading decisions. The goal is to better understand short term market behavior rather than predict long term trends.

Project Roadmap:
31/12/2025 - Present

This project is made of 3 layers:

- Core LOB engine 
- Order flow simulator
- Analytics & visualisation (graphs)

## Key Metrics & Formulas

### Mid Price
The fair price between buyers and sellers.

$$
\text{Mid Price} = \frac{\text{Best Bid} + \text{Best Ask}}{2}
$$

---

### Bid-Ask Spread
Measures market tightness and liquidity.

$$
\text{Spread} = \text{Best Ask} - \text{Best Bid}
$$

---

### Order Book Imbalance (OBI)
Indicates whether buying or selling pressure dominates.

$$
\text{OBI} =
\frac{\sum \text{Bid Volume} - \sum \text{Ask Volume}}
{\sum \text{Bid Volume} + \sum \text{Ask Volume}}
$$

Values range from **−1 (sell pressure)** to **+1 (buy pressure)**.

---

### Weighted Mid-Price
Gives more influence to the side with higher available volume.

$$
\text{Weighted Mid} =
\frac{\text{Ask} \times \text{Bid Volume} + \text{Bid} \times \text{Ask Volume}}
{\text{Bid Volume} + \text{Ask Volume}}
$$

---

### Short-Term Log Return
Used to measure immediate price movement.

$$
r_t = \log\left(\frac{P_t}{P_{t-1}}\right)
$$

---

### Order Flow
Tracks net aggressive trading activity.

$$
\text{Order Flow} =
\text{Market Buy Volume} - \text{Market Sell Volume}
$$
