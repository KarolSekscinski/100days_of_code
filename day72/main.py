import pandas as pd
df = pd.read_csv("salaries_by_college_major.csv")

df.head()

df.shape

df.columns

df.isna()
df.tail()
clean_df = df.dropna()
clean_df.tail()

clean_df['Starting Median Salary'].max()
clean_df['Starting Median Salary'].idxmax()
clean_df['Undergraduate Major'].loc[43]
clean_df['Undergraduate Major'][43]
clean_df.loc[43]

clean_df['Mid-Career Median Salary'].max()
clean_df['Mid-Career Median Salary'].idxmax()
clean_df.loc[8]

clean_df['Starting Median Salary'].idxmin()
clean_df.loc[49]

clean_df['Mid-Career Median Salary'].min()
clean_df['Mid-Career Median Salary'].idxmax()
clean_df.loc[8]

spread_col = clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']
clean_df.insert(1, 'Spread', spread_col)
clean_df.head()

low_risk = clean_df.sort_values('Spread', ascending=False)
low_risk[['Undergraduate Major', 'Spread']].head()

highest_pot = clean_df.sort_values('Mid-Career 90th Percentile Salary', ascending=False)
highest_pot.head()

highest_spread = clean_df.sort_values('Mid-Career Median Salary', ascending=False)
highest_spread[['Undergraduate Major', 'Mid-Career Median Salary']].head()

clean_df.groupby('Group').count()

pd.options.display.float_format = '{:,.2f}'.format
clean_df.groupby('Group').mean()
