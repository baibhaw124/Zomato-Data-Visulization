import pandas as pd
from ydata_profiling import ProfileReport  # Corrected import

df = pd.read_csv('zomato.csv')
profile = ProfileReport(df, title="Zomato Data Report")
profile.to_file("zomato.html")