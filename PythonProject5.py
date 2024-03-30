#Menggunakan __init__
import pandas as pd

class MarketingDataETL :
  def __init__(self, file):
    self.file = file
    self.df = None

  def Extract(self) :
    self.df = pd.read_csv(self.file, sep=';')
    return self.df
  def Transform(self) :
    self.df['purchase_date'] = pd.to_datetime(self.df['purchase_date'])
    self.df_cleaned = self.df.dropna()
    return self.df_cleaned
  def Store(self):
    self.df_cleaned.to_csv('marketing_data_new.csv', index=False)

etl = MarketingDataETL('marketing_data.csv')
etl.Extract()
etl.Transform()
etl.Store()

#ini mewariskan dari class yang menggunakan __INIT__
class TargetedMarketingETL(MarketingDataETL) :
  def Segment_customer(self):
    df_pengeluaran_total = self.df_cleaned.groupby('customer_id')['amount_spent'].sum().reset_index()
    df_kategori_produk = self.df_cleaned.groupby('customer_id')['product_category'].apply(list).reset_index()
    result = pd.merge(df_kategori_produk, df_pengeluaran_total, on="customer_id")
    return result
  def Transform(self):
    super().Transform()
    df_cleaned_average = self.df_cleaned.groupby('customer_id')['amount_spent'].mean()
    result = pd.merge(self.df_cleaned, df_cleaned_average, on="customer_id", suffixes=('', '_avg'))
    return result
target_ETL = TargetedMarketingETL('marketing_data.csv')
target_ETL.Extract()
target_ETL.Transform()
result = target_ETL.Transform()
print("data frame hasil pengelompokan :")
result