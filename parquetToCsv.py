# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 17:19:12 2024

@author: Luis1
"""
 
import pandas as pd

parquet_file_order = "/Users/Luis1/Projetos/Detection/datasets/parquet/btc_orderbook_df.parquet"
parquet_file_trade = "/Users/Luis1/Projetos/Detection/datasets/parquet/btc_trades_df.parquet"

dfo = pd.read_parquet(parquet_file_order)
dft = pd.read_parquet(parquet_file_trade)

csv_output_order = "/Users/Luis1/Projetos/Detection/datasets/csv/btc_orderbook_df.csv"
dft.to_csv(csv_output_order, index= False)
csv_output_trade = "/Users/Luis1/Projetos/Detection/datasets/csv/btc_trades_df.csv"
dft.to_csv(csv_output_trade, index= False)