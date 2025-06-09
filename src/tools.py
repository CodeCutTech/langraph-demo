from dotenv import load_dotenv
from langchain_tavily import TavilySearch
import re

load_dotenv()

web_search = TavilySearch(max_results=3)


def search_and_extract_signals(
    stock_symbol: str, query: str, keywords: list[str], prefix: str, default_msg: str
) -> str:
    """Generic function to search and extract signals based on keywords"""
    results = web_search.invoke(query)

    signals = []
    for result in results:
        content = result.get("content", "")
        if any(word in content.lower() for word in keywords):
            signals.append(f"• {result.get('title', 'News')}: {content[:200]}...")

    if signals:
        return f"{prefix} for {stock_symbol}:\n" + "\n".join(signals[:2])
    else:
        return f"{prefix} {stock_symbol}: {default_msg}"


# ===================================== #
#  BULL AGENT TOOLS (Optimistic/Buy)   #
# ===================================== #


def find_positive_news(stock_symbol: str):
    """Search for positive news and developments about a stock"""
    query = f"{stock_symbol} stock positive news earnings growth revenue profit upgrade"
    keywords = ["profit", "growth", "upgrade", "beat", "strong", "positive", "bullish"]
    prefix = "🐂 POSITIVE SIGNALS"
    default = "Limited positive news found, but that could mean it's undervalued!"
    return search_and_extract_signals(stock_symbol, query, keywords, prefix, default)


def calculate_growth_potential(stock_symbol: str):
    """Calculate basic growth metrics and bullish indicators"""
    query = f"{stock_symbol} stock price earnings revenue growth rate market cap"
    results = web_search.invoke(query)

    growth_indicators = []
    for result in results:
        content = result.get("content", "").lower()

        # Look for growth percentages
        percentages = re.findall(r"(\d+(?:\.\d+)?)\s*%", content)
        if percentages:
            growth_indicators.extend([f"{p}%" for p in percentages[:3]])

        # Look for positive growth terms
        if any(
            term in content
            for term in ["increase", "growth", "up", "higher", "rose", "gained"]
        ):
            growth_indicators.append("Positive trend detected")

    if growth_indicators:
        return f"📈 GROWTH POTENTIAL for {stock_symbol}: {', '.join(growth_indicators[:3])}"
    else:
        return f"📈 {stock_symbol}: Growth data limited, but could indicate overlooked opportunity!"


# ===================================== #
#  BEAR AGENT TOOLS (Pessimistic/Sell)  #
# ===================================== #


def find_negative_news(stock_symbol: str):
    """Search for negative news and risks about a stock"""
    query = f"{stock_symbol} stock negative news risks decline losses downgrade warning"
    keywords = [
        "loss",
        "decline",
        "risk",
        "warning",
        "downgrade",
        "weak",
        "negative",
        "bearish",
        "concern",
    ]
    prefix = "🐻 WARNING SIGNALS"
    default = "No major red flags found, but market volatility always poses risks!"
    return search_and_extract_signals(stock_symbol, query, keywords, prefix, default)


def assess_market_risks(stock_symbol: str):
    """Assess overall market risks and bearish indicators"""
    query = f"{stock_symbol} stock market risks volatility debt competition regulatory concerns"
    results = web_search.invoke(query)

    risk_factors = []
    for result in results:
        content = result.get("content", "").lower()

        # Look for risk terms
        if any(
            term in content
            for term in [
                "risk",
                "volatile",
                "uncertain",
                "concern",
                "debt",
                "competition",
            ]
        ):
            risk_factors.append("Market risk identified")

        # Look for negative percentages
        negative_changes = re.findall(r"down\s+(\d+(?:\.\d+)?)\s*%", content)
        if negative_changes:
            risk_factors.extend([f"Down {p}%" for p in negative_changes[:2]])

    if risk_factors:
        return f"⚠️ RISK ASSESSMENT for {stock_symbol}: {', '.join(risk_factors[:3])}"
    else:
        return f"⚠️ {stock_symbol}: Risk factors unclear - proceed with extreme caution!"


# ===================================== #
#  CHAIRMAN AGENT TOOLS (Decision maker) #
# ===================================== #


def get_current_market_sentiment(stock_symbol: str):
    """Get overall market sentiment and recent performance"""
    query = f"{stock_symbol} stock current price today market sentiment analyst rating"
    keywords = ["price", "trading", "market", "analyst"]
    prefix = "📊 CURRENT MARKET DATA"
    default = "Market data limited - need more information for decision"

    results = web_search.invoke(query)
    sentiment_data = []
    for result in results:
        content = result.get("content", "")
        title = result.get("title", "")
        if any(word in (title + content).lower() for word in keywords):
            sentiment_data.append(f"• {title}: {content[:150]}...")

    if sentiment_data:
        return f"{prefix} for {stock_symbol}:\n" + "\n".join(sentiment_data[:2])
    else:
        return f"{prefix} {stock_symbol}: {default}"


def make_investment_decision(stock_symbol: str, bull_points: str, bear_points: str):
    """Make final investment recommendation based on bull and bear arguments"""

    def count_points(points: str) -> int:
        return len(points.split("•")) if "•" in points else 1

    def check_signals(text: str, keywords: list[str]) -> bool:
        return any(word in text.lower() for word in keywords)

    # Score calculation
    bull_score = count_points(bull_points)
    bear_score = count_points(bear_points)

    # Signal detection
    strong_bull_signals = check_signals(
        bull_points, ["growth", "profit", "upgrade", "strong"]
    )
    strong_bear_signals = check_signals(
        bear_points, ["risk", "decline", "warning", "concern"]
    )

    # Decision logic
    if bull_score > bear_score and strong_bull_signals:
        recommendation = "BUY"
        confidence = "High"
    elif bear_score > bull_score and strong_bear_signals:
        recommendation = "SELL/AVOID"
        confidence = "High"
    else:
        recommendation = "HOLD/RESEARCH MORE"
        confidence = "Medium"

    return (
        f"🎯 FINAL DECISION for {stock_symbol}: {recommendation}\n"
        f"Confidence Level: {confidence}\n"
        f"Bull Arguments: {bull_score} points\n"
        f"Bear Arguments: {bear_score} points\n"
        f"Recommendation: Based on current analysis, {recommendation.lower()} position"
    )
