# Bot de Arbitraje Triangular
"""
Encargado de operar solmanete con:
    BTC
"""
from binance.client import Client
from binance.enums import *
import time
from datetime import datetime
import math
from binance_key import BinanceKey
import json

# El BOT empieza a partir de aquí

api_key = BinanceKey['api_key']
api_secret = BinanceKey['api_secret']

client = Client(api_key, api_secret)

def run():
    #Iniciar Bot de Arbitraje
    while 1:
        try:
            initialize_arb()
        except:
            print("Reiniciando el bot de BTC\n\n")

    pass


def set_time_binance():
    gt = client.get_server_time()
    tt = time.gmtime(int((gt["serverTime"])/1000))


def initialize_arb():
    welcome = "\n\n-----------------------------------------------------------------------------------\n\n"
    welcome += "El Bot de BTC empieza ahora a leer oportunidades de arbitraje"
    bot_start_time = str(datetime.now())
    welcome += "\nEl bot se ha iniciado a las: {}\n\n".format(bot_start_time)
    
    print(welcome)
    #data_log_to_file(welcome)

    try:
        list_of_arb_sym = [
            ['BTCUSDT', '1INCHUSDT', '1INCHBTC'],
            ['BTCUSDT', 'AAVEUSDT', 'AAVEBTC'],
            ['BTCUSDT', 'ALGOUSDT', 'ALGOBTC'],
            ['BTCUSDT', 'ALICEUSDT', 'ALICEBTC'],
            ['BTCUSDT', 'ANKRUSDT', 'ANKRBTC'],
            ['BTCUSDT', 'ANTUSDT', 'ANTBTC'],
            ['BTCUSDT', 'ATAUSDT', 'ATABTC'],
            ['BTCUSDT', 'ATOMUSDT', 'ATOMBTC'],
            ['BTCUSDT', 'AUDIOUSDT', 'AUDIOBTC'],
            ['BTCUSDT', 'AVAXUSDT', 'AVAXBTC'],
            ['BTCUSDT', 'BALUSDT', 'BALBTC'],
            ['BTCUSDT', 'BANDUSDT', 'BANDBTC'],
            ['BTCUSDT', 'BATUSDT', 'BATBTC'],
            ['BTCUSDT', 'BCHUSDT', 'BCHBTC'],
            ['BTCUSDT', 'BLZUSDT', 'BLZBTC'],
            ['BTCUSDT', 'BNBUSDT', 'BNBBTC'],
            ['BTCUSDT', 'BNTUSDT', 'BNTBTC'],
            ['BTCUSDT', 'CAKEUSDT', 'CAKEBTC'],
            ['BTCUSDT', 'CELOUSDT', 'CELOBTC'],
            ['BTCUSDT', 'CHZUSDT', 'CHZBTC'],
            ['BTCUSDT', 'COMPUSDT', 'COMPBTC'],
            ['BTCUSDT', 'COTIUSDT', 'COTIBTC'],
            ['BTCUSDT', 'CRVUSDT', 'CRVBTC'],
            ['BTCUSDT', 'CTSIUSDT', 'CTSIBTC'],
            ['BTCUSDT', 'DASHUSDT', 'DASHBTC'],
            ['BTCUSDT', 'DATAUSDT', 'DATABTC'],
            ['BTCUSDT', 'DCRUSDT', 'DCRBTC'],
            ['BTCUSDT', 'DNTUSDT', 'DNTBTC'],
            ['BTCUSDT', 'DOGEUSDT', 'DOGEBTC'],
            ['BTCUSDT', 'DOTUSDT', 'DOTBTC'],
            ['BTCUSDT', 'EGLDUSDT', 'EGLDBTC'],
            ['BTCUSDT', 'ENJUSDT', 'ENJBTC'],
            ['BTCUSDT', 'EOSUSDT', 'EOSBTC'],
            ['BTCUSDT', 'EPSUSDT', 'EPSBTC'],
            ['BTCUSDT', 'ETCUSDT', 'ETCBTC'],
            ['BTCUSDT', 'ETHUSDT', 'ETHBTC'],
            ['BTCUSDT', 'FETUSDT', 'FETBTC'],
            ['BTCUSDT', 'FILUSDT', 'FILBTC'],
            ['BTCUSDT', 'FORTHUSDT', 'FORTHBTC'],
            ['BTCUSDT', 'FTMUSDT', 'FTMBTC'],
            ['BTCUSDT', 'GRTUSDT', 'GRTBTC'],
            ['BTCUSDT', 'GTCUSDT', 'GTCBTC'],
            ['BTCUSDT', 'GXSUSDT', 'GXSBTC'],
            ['BTCUSDT', 'HARDUSDT', 'HARDBTC'],
            ['BTCUSDT', 'HBARUSDT', 'HBARBTC'],
            ['BTCUSDT', 'ICPUSDT', 'ICPBTC'],
            ['BTCUSDT', 'ICXUSDT', 'ICXBTC'],
            ['BTCUSDT', 'IOTAUSDT', 'IOTABTC'],
            ['BTCUSDT', 'KAVAUSDT', 'KAVABTC'],
            ['BTCUSDT', 'KEEPUSDT', 'KEEPBTC'],
            ['BTCUSDT', 'KLAYUSDT', 'KLAYBTC'],
            ['BTCUSDT', 'KMDUSDT', 'KMDBTC'],
            ['BTCUSDT', 'KNCUSDT', 'KNCBTC'],
            ['BTCUSDT', 'KSMUSDT', 'KSMBTC'],
            ['BTCUSDT', 'LINKUSDT', 'LINKBTC'],
            ['BTCUSDT', 'LPTUSDT', 'LPTBTC'],
            ['BTCUSDT', 'LRCUSDT', 'LRCBTC'],
            ['BTCUSDT', 'LTCUSDT', 'LTCBTC'],
            ['BTCUSDT', 'LTOUSDT', 'LTOBTC'],
            ['BTCUSDT', 'LINKUSDT', 'LINKBTC'],
            ['BTCUSDT', 'LPTUSDT', 'LPTBTC'],
            ['BTCUSDT', 'LRCUSDT', 'LRCBTC'],
            ['BTCUSDT', 'LTCUSDT', 'LTCBTC'],
            ['BTCUSDT', 'LTOUSDT', 'LTOBTC'],
            ['BTCUSDT', 'LUNAUSDT', 'LUNABTC'],
            ['BTCUSDT', 'MANAUSDT', 'MANABTC'],
            ['BTCUSDT', 'MATICUSDT', 'MATICBTC'],
            ['BTCUSDT', 'MTLUSDT', 'MTLBTC'],
            ['BTCUSDT', 'NANOUSDT', 'NANOBTC'],
            ['BTCUSDT', 'NEOUSDT', 'NEOBTC'],
            ['BTCUSDT', 'NKNUSDT', 'NKNBTC'],
            ['BTCUSDT', 'OGNUSDT', 'OGNBTC'],
            ['BTCUSDT', 'OMUSDT', 'OMBTC'],
            ['BTCUSDT', 'OMGUSDT', 'OMGBTC'],
            ['BTCUSDT', 'ONEUSDT', 'ONEBTC'],
            ['BTCUSDT', 'ONTUSDT', 'ONTBTC'],
            ['BTCUSDT', 'PAXGUSDT', 'PAXGBTC'],
            ['BTCUSDT', 'PERPUSDT', 'PERPBTC'],
            ['BTCUSDT', 'QTUMUSDT', 'QTUMBTC'],
            ['BTCUSDT', 'RENUSDT', 'RENBTC'],
            ['BTCUSDT', 'RLCUSDT', 'RLCBTC'],
            ['BTCUSDT', 'RUNEUSDT', 'RUNEBTC'],
            ['BTCUSDT', 'RVNUSDT', 'RVNBTC'],
            ['BTCUSDT', 'SKLUSDT', 'SKLBTC'],
            ['BTCUSDT', 'SNXUSDT', 'SNXBTC'],
            ['BTCUSDT', 'SOLUSDT', 'SOLBTC'],
            ['BTCUSDT', 'STMXUSDT', 'STMXBTC'],
            ['BTCUSDT', 'STXUSDT', 'STXBTC'],
            ['BTCUSDT', 'SUPERUSDT', 'SUPERBTC'],
            ['BTCUSDT', 'SUSHIUSDT', 'SUSHIBTC'],
            ['BTCUSDT', 'SXPUSDT', 'SXPBTC'],
            ['BTCUSDT', 'TFUELUSDT', 'TFUELBTC'],
            ['BTCUSDT', 'THETAUSDT', 'THETABTC'],
            ['BTCUSDT', 'TLMUSDT', 'TLMBTC'],
            ['BTCUSDT', 'TRUUSDT', 'TRUBTC'],
            ['BTCUSDT', 'TRXUSDT', 'TRXBTC'],
            ['BTCUSDT', 'UNIUSDT', 'UNIBTC'],
            ['BTCUSDT', 'VETUSDT', 'VETBTC'],
            ['BTCUSDT', 'WAVESUSDT', 'WAVESBTC'],
            ['BTCUSDT', 'WRXUSDT', 'WRXBTC'],
            ['BTCUSDT', 'XLMUSDT', 'XLMBTC'],
            ['BTCUSDT', 'XMRUSDT', 'XMRBTC'],
            ['BTCUSDT', 'XRPUSDT', 'XRPBTC'],
            ['BTCUSDT', 'XTZUSDT', 'XTZBTC'],
            ['BTCUSDT', 'YFIUSDT', 'YFIBTC'],
            ['BTCUSDT', 'ZECUSDT', 'ZECBTC'],
            ['BTCUSDT', 'ZILUSDT', 'ZILBTC']        ]

        #Cargar cantidades de los balances
        tickers = client.get_orderbook_tickers()
        while 1:
            #Cargar función de Beneficio de Arbitraje
            calc_profit_list = []
            exp_profit = 0  #Beneficio esperado marcado inicialmente como 0
            m=0

            for i in range(0,2):
                if exp_profit>0:
                    break

                for arb_market in list_of_arb_sym:
                    calc_profit_list.append(arbitrage_bin(arb_market, tickers, 1, 1))

                for exch_market in calc_profit_list:
                    if exch_market[4]>exp_profit:
                        exp_profit = exch_market[4]
                        m = n

                    n += 1

            exp_profitx = float("%0.3f" % (exp_profit))
            if m>4:
                m -= 4
                arb_list_data = []
                
            for i in range(0,180):
                #Recoger Datos del Arbitraje en una lista formateada de 5 ciclos, 30 segundos por ciclo
                try:
                    arb_list_data.append(arbitrage_bin(list_of_arb_sym[m], tickers, 1, 1, 'Yes', 'Yes'))

                except:
                    pass
             
    
    except Exception as e:
        print(e)
        #data_log_to_file(e)
        excp_err = "\nFALLO AL INICIAR\n"
        print(excp_err)
        #data_log_to_file(excp_err)
        raise

"""
def data_log_to_file(message):
    with open('BNB_DataLog.txt', 'a+') as f:
        f.write(message)
"""

def round_decimals_down(number:float, decimals:int=2):
    if not isinstance(decimals, int):
        raise TypeError("decimal places must be an integer")
    elif decimals < 0:
        raise ValueError("decimal places has to be 0 or more")
    elif decimals == 0:
        return math.floor(number)

    factor = 10 ** decimals
    return math.floor(number * factor) / factor


def arbitrage_bin(list_of_sym, tickers, cycle_num=10, cycle_time=30, place_order='Yes', real_order='Yes'):
    # Create Triangular Arbitrage Function


    fee_percentage = 0.225

    #Crear función de arbitraje con Python - Binance
    for i in range(0,1): #Inicializar Exchange
        if 1:
            #Determinar el número de ciclo
            for k in range(0, cycle_num):
                i=0
                
                info_1 = client.get_order_book(symbol=list_of_sym[0])
                price_1 = float(info_1["asks"][0][0])
                info_2 = client.get_order_book(symbol=list_of_sym[1])
                price_2 = float(info_2["bids"][0][0])
                #info_3 = client.get_order_book(symbol=list_of_sym[2])
                #price_3 = float(info_3["asks"][0][0])
                info_3 = client.get_ticker(symbol=list_of_sym[2])
                price_3 = float(info_3["lastPrice"])


                opp_arb_first = float(100.000* price_1) 
                opp_arb_second = float(opp_arb_first/price_2)
                opp_arb_third = float(opp_arb_second*price_3)
                opp_arb_str = "Que daría: "+ str(opp_arb_third)
                # print(opp_arb_str)
                #data_log_to_file(opp_arb_str)

                data_collect_message1 = "Número de ciclo de recopilación de datos: "+str(k) +'\n'
                data_collect_message1 += "Par de divisas: "+str(list_of_sym)+"\n"
                #data_log_to_file(data_collect_message1)

                if opp_arb_third > 100.000:
                    arb_2_msg = "Posibilidad de arbitraje\n"
                    #print(arb_2_msg)
                    #data_log_to_file(arb_2_msg)
                    arb_profit = opp_arb_third - 100.000
                    arb_profit_fees = fee_percentage
                    arb_profit_adjust = arb_profit - arb_profit_fees

                    arb_1_msg = "Beneficio potencial (porcentaje): "+str(arb_profit)+"%\n\n"
                    arb_1_msg += "Tarifas potenciales (porcentaje): "+str(arb_profit_fees)+"%\n\n"
                    arb_1_msg += "Beneficio ajustado (porcentaje): "+str(arb_profit_adjust)+"%\n\n"
                    #print(arb_1_msg)
                    #data_log_to_file(arb_1_msg)


                    #Calcular la cantidad de beneficio
                    #Realizar pedido
                    if arb_profit_adjust > 0.3:

                        has_order1 = client.get_open_orders(symbol=list_of_sym[0])
                        has_order2 = client.get_open_orders(symbol=list_of_sym[1])
                        has_order3 = client.get_open_orders(symbol=list_of_sym[2])

                        if not has_order2 and not has_order3:
                            place_order_msg = "REALIZANDO OPERACIÓN\n\n"
                            print(place_order_msg)
                            #data_log_to_file(place_order_msg)


                            list_of_precision = [
                                ['0.00000001', 8],
                                ['0.00000010', 7],
                                ['0.00000100', 6],
                                ['0.00001000', 5],
                                ['0.00010000', 4],
                                ['0.00100000', 3],
                                ['0.01000000', 2],
                                ['0.10000000', 1],
                                ['1.00000000', 0]
                                ]

                            precision1 = 0
                            ceroes1 = 0
                            precision2 = 0
                            ceroes2 = 0
                            precision3 = 0
                            ceroes3 = 0

                            #Primera Venta de BTC a BTC
                            #Recoger precision
                            info1 = client.get_symbol_info(list_of_sym[0])
                            filters1 = info1["filters"][2]["stepSize"]
                            price_filters1 = info1["filters"][0]["minPrice"]
                            for value in list_of_precision:
                                if value[0] == filters1:
                                    precision1 = value[1]
                                if value[0] == price_filters1:
                                    ceroes1 = value[1]
                                    
                            usdt_asset = client.get_asset_balance("USDT")
                            usdt_balance = float(usdt_asset["free"])

                            if usdt_balance > 80:
                                quantity_btc = (usdt_balance/price_1)*0.97
                                quantity_btc_rounded = str(round_decimals_down(quantity_btc, precision1))

                                order_btc_usdt = client.order_market_buy(
                                    symbol="BTCUSDT",
                                    quantity=quantity_btc_rounded
                                )                                    

                            balance1 = client.get_asset_balance(asset='BTC')
                            quantity1 = (float(balance1['free']))*0.98
                            quantity_1 = str(round_decimals_down(quantity1, precision1))
                            #quantity_1 = "0.006"
                            #price1_forced = price_1 * 0.9995
                            price1_rounded = float(round(price_1, ceroes1))
                            
                            
                            order_1 = client.create_order(
                                symbol=list_of_sym[0],
                                side=SIDE_SELL,
                                type=ORDER_TYPE_LIMIT,
                                timeInForce=TIME_IN_FORCE_GTC,
                                quantity=quantity_1,
                                price=('{:.8f}'.format(price1_rounded))
                            )
                            
                            media_1 = (float(quantity_1)*float(price1_rounded)) #Cantidad de USDT
                            first_order = "Primera operación realizada.\n"
                            print(first_order)
                            #data_log_to_file(first_order)   

                            #Bucle hasta que se realice la venta:

                            while True:
                                if not has_order1:
                                    break
                                else:
                                    waiting1 = "Esperando a la compra"
                                    #data_log_to_file(waiting1)
                                time.sleep(1.5)               
                            
                            #Segunda compra
                            #Recoger precision
                            info2 = client.get_symbol_info(list_of_sym[1])
                            filters2 = info2["filters"][2]["stepSize"]
                            price_filters2 = info2["filters"][0]["minPrice"]
                            for value in list_of_precision:
                                if value[0] == filters2:
                                    precision2 = value[1]
                                if value[0] == price_filters2:
                                    ceroes2 = value[1]

                            balance2 = client.get_asset_balance(asset='USDT')
                            quantity2 = (float(balance2['free']))/(price_2)*0.97
                            #balance2 = 0.25*price_1
                            #quantity2 = (media_1/price_2)*0.99
                            quantity_2 = str(round_decimals_down(quantity2, precision2))
                            symb2 = list_of_sym[1]
                            symb2form = symb2[0:-4]
                            #price2_forced = price_2 * 1.001
                            price2_rounded = float(round(price_2, ceroes2))
                            

                            order_2 = client.create_order(
                                symbol=list_of_sym[1],
                                side=SIDE_BUY,
                                type=ORDER_TYPE_LIMIT,
                                timeInForce=TIME_IN_FORCE_GTC,
                                quantity=quantity_2,
                                price=('{:.8f}'.format(price2_rounded))
                            )
                            
                            second_order = "Segunda operación realizada. \n"
                            print(second_order)
                            #data_log_to_file(second_order)

                            #Bucle hasta que se realice la venta:
                            while True:
                                has_order2 = client.get_open_orders(symbol=list_of_sym[1])
                                if not has_order2:
                                    break
                                else:
                                    waiting1 = "Esperando a la compra"
                                    #data_log_to_file(waiting1)
                                time.sleep(1.5) 
                            
                            #Venta y última operación
                            #Recoger precision
                            info3 = client.get_symbol_info(list_of_sym[2])
                            filters3 = info3["filters"][2]["stepSize"]
                            price_filters3 = info3["filters"][0]["minPrice"]
                            for value in list_of_precision:
                                if value[0] == filters3:
                                    precision3 = value[1]
                                if value[0] == price_filters3:
                                    ceroes3 = value[1]

                            #print(symb2form)
                            balance3 = client.get_asset_balance(asset=symb2form)
                            quantity3 = (float(balance3['free']))
                            quantity_3 = str(round_decimals_down(quantity3, precision3))
                            #price3_forced = price_3 * 0.999
                            price3_rounded = float(round(price_3, ceroes3))
                            """
                            order_3 = client.order_market_sell(
                                symbol=list_of_sym[2],
                                quantity=quantity_3
                            )
                            """
                            
                            order_3 = client.create_order(
                                symbol=list_of_sym[2],
                                side=SIDE_SELL,
                                type=ORDER_TYPE_LIMIT,
                                timeInForce=TIME_IN_FORCE_GTC,
                                quantity=quantity_3,
                                price=('{:.8f}'.format(price3_rounded))
                            )
                            
                            third_order = "Operación de venta realizada.\n"
                            print(third_order)
                            #data_log_to_file(third_order)

                            #Bucle hasta que se realice la venta:

                            while True:
                                has_order3 = client.get_open_orders(symbol=list_of_sym[2])
                                if not has_order3:
                                    break
                                else:
                                    waiting1 = "Esperando a la compra"
                                    #data_log_to_file(waiting1)
                                time.sleep(1.5) 
                            
                            
                            third_order += "EL BOT HA COMPRADO! \n\n"
                            time.sleep(2)
                            


                            #Mandar dust a BNB
                            dust1 = client.transfer_dust(asset="USDT")
                            dust = client.transfer_dust(asset=symb2form)
                            

                            dust1()
                            dust()
                        




                
def make_patch_spines_invisible(ax):
    ax.set_frame_on(True)
    ax.patch.set_visible(False)
    for sp in ax.spines.values():
        sp.set_visible(False)


if __name__ == "__main__":
    run()