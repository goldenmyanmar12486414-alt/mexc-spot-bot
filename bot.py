import os, time, hashlib, hmac, requests

API_KEY = os.getenv('MEXC_API_KEY')
SECRET_KEY = os.getenv('MEXC_SECRET_KEY')
SYMBOLS = ["PAXGUSDT", "XLMUSDT", "HYPEUSDT", "SOLUSDT", "BNBUSDT"]
INVEST_PER_COIN = 24.0

def get_signature(params):
    query_string = '&'.join([f"{k}={v}" for k, v in sorted(params.items())])
    return hmac.new(SECRET_KEY.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()

def place_order(symbol):
    endpoint = "https://api.mexc.com/api/v3/order"
    timestamp = int(time.time() * 1000)
    params = {"symbol": symbol, "side": "BUY", "type": "MARKET", "quoteOrderQty": INVEST_PER_COIN, "timestamp": timestamp}
    params['signature'] = get_signature(params)
    return requests.post(endpoint, params=params, headers={"X-MEXC-APIKEY": API_KEY}).json()

if __name__ == "__main__":
    print("--- Start Buying ---")
    for coin in SYMBOLS:
        print(f"Buying {coin}..."); print(f"Result: {place_order(coin)}")
