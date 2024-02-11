import pandas as pd
import yfinance as yf


def get_stocks_yfinance(stocks):
    stocks_df = pd.DataFrame()
    for stock in stocks.keys():
        stocks_df[stock] = yf.download(stock, start="2015-01-01")["Close"]

    stocks_df = stocks_df.rename(columns=stocks)

    print("Valores nulos:")
    print(stocks_df.isnull().sum())
    stocks_df = stocks_df.dropna()
    print("Removendo valores nulos:")
    print(stocks_df.isnull().sum())

    # ? Média de dias em que as bolsas de valores para essas ações ficaram abertas ao longo dos anos da base de dados
    days = int(len(stocks_df) / len(stocks_df.index.year.unique()))

    return stocks_df, days


if __name__ == "__main__":
    stocks = {"BBAS3.SA": "Banco do Brasil", "ITSA3.SA": "TESTE"}

    print(get_stocks_yfinance(stocks))
