# ArbitrageEngine
ArbitrageEngine is an automated cryptocurrency arbitrage trading bot that scans multiple exchanges for profitable opportunities in real-time. It fetches live price data, calculates potential arbitrage profits (after fees), and sends email alerts whenever a trading opportunity arises.

📌 Features

✅ Multi-exchange price tracking (Binance, Coinbase, ACE, etc.)

✅ Real-time arbitrage opportunity detection

✅ Email notifications for both profit and loss scenarios

✅ Customizable trading pairs and execution frequency

✅ Secure email configuration using app passwords

📖 How It Works

The bot fetches the latest prices of BTC/USDT (or other pairs) from multiple exchanges.

It calculates the potential arbitrage profit after deducting exchange fees.

If a profit-making opportunity is found, an email alert is sent.

The bot runs continuously at a user-defined interval (default: every 3 seconds).

🛠 Installation & Setup

Prerequisites
Ensure you have Python 3+ installed along with the required libraries:

```pip install ccxt schedule smtplib```

🔐 Email Configuration

Enable 2-Step Verification on your Google account.

Generate an App Password.

Replace the placeholder in the script:

```EMAIL_ADDRESS = "your-email@gmail.com"```

```EMAIL_PASSWORD = "your-app-password"```


🏆 Future Improvements

🔄 Auto-execute trades instead of just sending alerts

📈 Support for multiple trading pairs

📊 Web-based dashboard to monitor arbitrage activity

💱 Supported Exchanges
CryptoArbBot supports the following exchanges via CCXT:

Binance
Coinbase
Kraken
Bitfinex
Huobi
KuCoin
OKX
Bitstamp
Gate.io
Bybit
Crypto.com
Bittrex
Poloniex
AscendEX
Phemex
BitMart
EXMO
HitBTC
Bibox
Indodax
ACE
ZB.com
LBank
CoinTiger
WhiteBit
BigONE
ProBit
XT.COM
etc.
## Check All Supported Exchanges

You can check all the supported exchanges using this code:

```python
import ccxt

# Fetch all supported exchanges
exchanges = ccxt.exchanges

print("Supported Exchanges:")
for exchange in exchanges:
    print(exchange)


