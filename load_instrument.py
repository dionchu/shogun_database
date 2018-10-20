from shogun_database.future_root_factory import FutureRootFactory

columns =[
        'symbol_id',
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

def write_future(factory,root_symbol):
        root_chain_df = factory.make_root_chain(root_symbol)
        root_info_dict = factory.retrieve_root_info(root_symbol)

        pd.concat([pd.DataFrame.from_dict(root_info),root_chain_df],axis=1).fillna(method='ffill')
        #create ticker table by month or quarter
        #filter for those that are listed to get contract months
        #apply date rules and create dict
        #append dict to root info and create pandas
        #take symbol list and map to thomson symbol list
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

    _kwargnames = frozenset({
        'root_symbol',
        'instrument_name',
        'instrument_country_id',
        'asset_class_id',
        'settle_start',
        'settle_end',
        'settle_method',
        'settle_timezone',
        'final_settle_start',
        'final_settle_end',
        'final_settle_method',
        'final_settle_timezone',
        'last_trade_time'
#        'first_traded',
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
        'delivery_month',
        'delivery_year',
    })
