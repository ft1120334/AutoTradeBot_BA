//获取对币最新价格
price = client.get_symbol_ticker(symbol='BTCUSDT')  
print(price['price'])  

#下单与撤单
order = client.create_order(                       //下单
    symbol='BTCUSDT',  
    side=Client.SIDE_BUY,  
    type=Client.ORDER_TYPE_MARKET,  
    quantity=0.001  
)  
print(order)  

cancel = client.cancel_order(                     //撤单
    symbol='BTCUSDT',  
    orderId=order['orderId']  
)  
print(cancel)  
