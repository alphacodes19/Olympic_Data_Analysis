import pandas as pd


def preprocess(df, region_df):
    # filtering for Summer Olympics only
    df = df[df['Season'] == 'Summer']
    df = df.merge(region_df, on="NOC", how='left')
    # dropping duplicates
    df.drop_duplicates(inplace=True)
    df = pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)
    return df
