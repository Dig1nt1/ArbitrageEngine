import ccxt
import smtplib
import schedule
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Initialize ACE Exchange and Coinbase
ace = ccxt.ace()
coinbase = ccxt.coinbase()

# Trading pair
trading_pair = "ETH/USDT"

# Exchange fees
ace_fee = 0.1 / 100  # 0.1% trading fee
coinbase_fee = 0.5 / 100  # 0.5% trading fee

# Secure Email Configuration (Use App Password, NOT your real password!)
EMAIL_ADDRESS = "sarkardiganta40@gmail.com"
EMAIL_PASSWORD = "your-app-password"  # Update with new App Password
RECIPIENT_EMAIL = "sarkardiganta40@gmail.com"

# Track last arbitrage state to avoid duplicate emails
last_sent_status = None


def send_email(subject, message):
    """Sends an email with UTF-8 encoding to handle Unicode characters."""
    try:
        print("📩 Attempting to send email...")  # Debugging log

        msg = MIMEMultipart()
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = RECIPIENT_EMAIL
        msg["Subject"] = subject
        msg.attach(MIMEText(message, "plain", "utf-8"))

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, RECIPIENT_EMAIL, msg.as_string())
        server.quit()

        print(f"✅ Email Sent: {subject}")  # Debugging log
    except Exception as e:
        print(f"⚠️ Email Error: {e}")


def calculate_profit(buy_price, sell_price, fee1, fee2):
    """Calculates the net profit after fees."""
    buy_price_with_fee = buy_price * (1 + fee1)
    sell_price_with_fee = sell_price * (1 - fee2)
    return sell_price_with_fee - buy_price_with_fee


def check_arbitrage():
    """Checks for arbitrage opportunities and sends email alerts."""
    global last_sent_status

    try:
        print("🔄 Fetching prices...")  # Debugging log

        ace_ticker = ace.fetch_ticker(trading_pair)
        coinbase_ticker = coinbase.fetch_ticker(trading_pair)

        if "last" not in ace_ticker or "last" not in coinbase_ticker:
            print("⚠️ Price data missing from exchange.")
            return

        ace_price = ace_ticker["last"]
        coinbase_price = coinbase_ticker["last"]

        print(f"✅ ACE Price: {ace_price} USDT")  # Debugging log
        print(f"✅ Coinbase Price: {coinbase_price} USDT")  # Debugging log

        profit = calculate_profit(ace_price, coinbase_price, ace_fee, coinbase_fee)
        print(f"📊 Profit Calculation: {profit:.2f} USDT")  # Debugging log

        current_status = "profit" if profit > 0 else "loss"

        if current_status != last_sent_status:
            subject = "🚀 Arbitrage Profit Opportunity!" if profit > 0 else "❌ Loss-Making Arbitrage Opportunity"
            message = f"Buy: {ace_price} USDT (ACE)\nSell: {coinbase_price} USDT (Coinbase)\nNet Profit: {profit:.2f} USDT"

            send_email(subject, message)
            last_sent_status = current_status  # Update last sent status

    except Exception as e:
        print(f"⚠️ Error fetching data: {e}")


# Run bot every 3 seconds (avoid spam email limits)
schedule.every(3).seconds.do(check_arbitrage)

# Run indefinitely
while True:
    schedule.run_pending()
    time.sleep(5)  # Prevent excessive CPU usage
