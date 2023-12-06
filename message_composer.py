import pandas as pd

filename = r'D:\Documents\Finance News.xlsx'

df = pd.read_excel(filename)
df_sorted = df.sort_values(by='Rank')
top_5_stories = df_sorted.head(5)
remaining_stories = df_sorted.iloc[5:]
top_5_output = "\n".join(
    [f"\n{row['Headline']}\n{row['Summary']}\n{row['Link']}\n" for i, (_, row) in enumerate(top_5_stories.iterrows())]
)
remaining_output = "\n".join(
    [f"\nRank {row['Rank']}: {row['Headline']}\n" for _, row in remaining_stories.iterrows()]
)
final_output = f"Good day, here are the top 5 ranking stories from Business Inquirer today, based on your interest:\n{top_5_output}\n\nHere are the other stories:\n{remaining_output}\n\nAttached is the Excel file containing all data for further reading."

# Print or save the final output
print(final_output)