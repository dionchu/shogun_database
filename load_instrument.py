import numpy as np
import pandas as pd
import eikon as ek
ek.set_app_key('48f17fdf21184b0ca9c4ea8913a840a92b338918')
from shogun_database.future_root_factory import FutureRootFactory

columns =[
        'exchange_symbol',
        'root_symbol',
        'instrument_name',
        'instrument_country_id',
        'underlying_name',
        'underlying_asset_class_id',
        'settle_start',
        'settle_end',
        'settle_method',
        'settle_timezone',
        'final_settle_start',
        'final_settle_end',
        'final_settle_method',
        'final_settle_timezone',
        'last_trade_time'
        'quote_currency_id',
        'multiplier',
        'tick_size',
        'start_date',
        'end_date',
        'first_trade',
        'last_trade',
        'first_position',
        'last_position',
        'first_notice_date',
        'last_notice_date',
        'first_delivery_date',
        'last_delivery_date',
        'settlement_date',
        'volume_switch_date',
        'open_interest_switch_date',
        'auto_close_date',
        'parent_calendar_id',
        'child_calendar_id'
        'average_pricing',
        'deliverable',
        'delivery_month',
        'delivery_year',
]

future_instrument_df = pd.DataFrame(columns = columns)

def write_future(factory,root_symbol):
        """
        write new future instruments to table.
        """
        # Construct futures instruments data
        root_chain_df = factory.make_root_chain(root_symbol)
        root_info_dict = factory.retrieve_root_info(root_symbol)

        # Combine futures instrument information and calculated dates
        root_info_and_chain = pd.concat([pd.DataFrame.from_dict(root_info_dict),root_chain_df],axis=1).fillna(method='ffill')

        # inner join with future_instrument_df to enforce column structure
        df_insert = pd.concat([future_instrument_df,root_info_and_chain], join = "inner")

        # Extract platform ticker symbols
        root_chain_dict = root_chain_df.set_index('platform_symbol').to_dict()
        platform_symbol_list = list(root_chain_dict['exchange_symbol'].keys())

        data_df = pd.DataFrame()
        for platform_symbol in platform_symbol_list:
            print(platform_symbol)
            exchange_symbol = root_chain_dict['exchange_symbol'][platform_symbol]
            start = root_chain_dict['first_trade'][platform_symbol].strftime("%Y-%m-%d")
            end = root_chain_dict['last_trade'][platform_symbol].strftime("%Y-%m-%d")
            tmp_ohlcv = ek.get_timeseries(platform_symbol,["open","high","low","close","volume"],start_date=start, end_date=end)
            tmp_ohlcv.insert(0,'exchange_symbol',exchange_symbol)
            e = ek.get_data(platform_symbol, ['TR.OPENINTEREST.Date', 'TR.OPENINTEREST'], {'SDate':start,'EDate':end})
            tmp_oi = pd.DataFrame({'open_interest': e[0]['Open Interest'].values}, index = pd.to_datetime(e[0]['Date'].values))
            tmp = pd.merge(tmp_ohlcv,tmp_oi,left_index=True,right_index=True)
            data_df = data_df.append(tmp)

        data_df.columns = ['exchange_symbol','open','high','low','close','volume','open_interest']
        data_df.to_csv('./shogun_database/_InstrumentData.csv')
        return data_df
        #run through loop to get data for all, keeping in mind 5 year limit to history
        #write or append to csv
        #this concludes the write + load function

        #update function
        #one for us, one for eu, one for asia, or separated by exchange close times
        #generate currently listed contracts
        #check against thomson
        #dump into today update list
        #run through list download and append latest data to df
        #check to see that we are getting data that we expect to get

        #read first and last date for each symbol in isntrument table
        #insert those dates into instrument table
        #write missing to dashboard or log or email for daily check

        #create continuous futures from the data daily
        #dump this into a csv file, either locally or ftp to blackbox
        #read the data in R and save to RData file in compatible format

        #setup account for each client
        #have algorithm run incrementally, day by day
        #have algorithm spit out orders with equity and vol info to file or shiny

        #have R trade on real prices rather than continuous prices
        #track roll dates

        #migrate all R code into python and integrate

        #track pnl and have program set up to take actual fills against benchmark

        #clean up code and start testing new strategies
