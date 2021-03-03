import pandas as pd
import os

def main():
    
    df = pd.read_csv((os.path.join('/opt/ml/processing/input','part-00000-be25f590-e7b0-4e7c-b2c5-411437906e5e-c000.csv')))
    df.event_datetime = pd.to_datetime(df.event_datetime, infer_datetime_format=True)
    df.to_csv((os.path.join('opt/ml/processing/output','ouput.csv')),index=False,header=True)
    
if __name__ == '__main__':
    main()