"""
🌙 Antsa's Minimal Config - built on Moon Dev's architecture 🚀
Compatible with MoonDev agents but stripped for strategy-only use.
"""

# ==========================================================
# 🌍 Exchange & Environment Settings
# ==========================================================
EXCHANGE = 'paper'  # Options: 'paper', 'binance', 'hyperliquid', 'solana'
WALLET_ADDRESS = "YOUR_WALLET_ADDRESS_HERE"

# ==========================================================
# 💰 Position & Risk Management
# ==========================================================
usd_size = 100           # Default position size
max_usd_order_size = 10  # Max order per trade
CASH_PERCENTAGE = 10     # Keep 10% cash buffer
MAX_POSITION_PERCENTAGE = 25
STOPLOSS_PRICE = 0.0     # Placeholder - not used yet
BREAKOUT_PRICE = 0.0     # Placeholder - not used yet
SLEEP_AFTER_CLOSE = 300  # Sleep 5 min after closing position

# Risk Agent thresholds
MAX_LOSS_USD = 50
MAX_GAIN_USD = 100
MINIMUM_BALANCE_USD = 25
USE_AI_CONFIRMATION = False

# ==========================================================
# 🤖 AI Model Settings
# ==========================================================
AI_MODEL = "claude-3-haiku-20240307"  # Options: groq, xai, deepseek, ollama, openai
AI_MAX_TOKENS = 1024
AI_TEMPERATURE = 0.7

# ==========================================================
# ⚙️ Strategy Parameters
# ==========================================================
ENABLE_STRATEGIES = True
STRATEGY_MIN_CONFIDENCE = 0.7
SLEEP_BETWEEN_RUNS_MINUTES = 10

# ==========================================================
# 🧠 Training / Backtest Parameters
# ==========================================================
DATA_TIMEFRAME = '1H'
DAYSBACK_4_DATA = 5
SAVE_OHLCV_DATA = False

# ==========================================================
# 📊 Debug / Logging
# ==========================================================
LOG_LEVEL = "INFO"
SAVE_RESULTS = True

# ==========================================================
# 🪐 Function: get_active_tokens
# ==========================================================
def get_active_tokens():
    """Return which tokens to trade based on selected exchange"""
    if EXCHANGE == 'hyperliquid':
        return ['BTC', 'ETH', 'SOL']
    elif EXCHANGE == 'binance':
        return ['BTCUSDT', 'ETHUSDT']
    else:
        return ['TEST']

tokens_to_trade = get_active_tokens()
