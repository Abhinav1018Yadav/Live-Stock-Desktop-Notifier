import time 
from plyer import notification 
import yfinance as yf 



a=float(input("enter the bencemark price: "))

while True:
    appl = yf.Ticker("AAPL")
    data = appl.info
    cp = data["currentPrice"]


    if cp < a:
        notification.notify(
            title = "Apple Inc. (DOWN)",
            message = "CurrentPrice = {cp} \nDayLow = {dl} \nDayHigh = {dh}".format(
                        cp = data["currentPrice"],
                        dl = data["dayLow"],
                        dh = data["dayHigh"]),
            app_icon = "stock_bear.ico",
            timeout = 20
        )
        time.sleep(10)

    elif cp >= a:
        notification.notify(
            title = "Apple Inc. (UP)",
            message = "CurrentPrice = {cp} \nDayLow = {dl} \nDayHigh = {dh}".format(
                        cp = data["currentPrice"],
                        dl = data["dayLow"],
                        dh = data["dayHigh"]),
            app_icon = "stock.ico",
            timeout = 20
        )
        time.sleep(10)

