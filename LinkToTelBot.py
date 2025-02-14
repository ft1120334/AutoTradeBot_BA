#连接TelBot
def place_order_with_stop_loss(symbol, side, quantity, stop_loss_price):  
    order = client.create_order(  
        symbol=symbol,  
        side=side,  
        type=Client.ORDER_TYPE_MARKET,  
        quantity=quantity  
    )  
    stop_loss_order = client.create_order(  
        symbol=symbol,  
        side=Client.SIDE_SELL if side == Client.SIDE_BUY else Client.SIDE_BUY,  
        type=Client.ORDER_TYPE_STOP_LOSS,  
        quantity=quantity,  
        price=stop_loss_price  
    )  
    return order, stop_loss_order  
  
order, stop_loss_order = place_order_with_stop_loss('BTCUSDT', Client.SIDE_BUY, 0.001, 30000)  
print(order, stop_loss_order)  
