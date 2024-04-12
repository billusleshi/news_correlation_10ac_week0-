import matplotlib.pyplot as plt
import seaborn as sns

# Distribution of article_id
plt.figure(figsize=(8, 6))
sns.histplot(data_df['article_id'], bins=20, kde=True)
plt.title('Distribution of article_id')
plt.xlabel('Article ID')
plt.ylabel('Frequency')
plt.show()
# Scatter plot between article_id and GlobalRank
plt.figure(figsize=(8, 6))
sns.scatterplot(x='article_id', y='GlobalRank', data=data_df.merge(traffic_df, how='left', on='Domain'))
plt.title('Scatter plot between article_id and GlobalRank')
plt.xlabel('Article ID')
plt.ylabel('Global Rank')
plt.show()
# Check for missing values
print("\nMissing values in data dataframe:\n", data_df.isnull().sum())
# Example: Group by website domain and count the number of news articles
article_count_by_domain = data_df.groupby('source_name').size().reset_index(name='article_count')
print("\nArticle count by domain:\n", article_count_by_domain)
