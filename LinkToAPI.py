#连接Binance API#
//使用python-binance库连接Binance API
from binance.client import Client  
api_key = '你的API Key'  
api_secret = '你的Secret Key'  
client = Client(api_key, api_secret)  

#实时数据监听#
//使用python-binance的Websocket接口监听实时数据：
cancel = client.cancel_order(  
    symbol='BTCUSDT',  
    orderId=order['orderId']  
)  
print(cancel)  
