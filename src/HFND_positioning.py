import pandas as pd
import plotly.express as px


threshold = 2  # Threshold for filtering weightings

# Load the data from url
url = "https://www.unlimitedetfs.com/wp-content/Fund_files/files/TidalETF_Services.40ZZ.A5_Holdings_HFND.csv"
df = pd.read_csv(url, delimiter=',')

print(df.head())

# Clean column names by stripping leading/trailing spaces
df.columns = df.columns.str.strip()

# Convert the 'Weightings' column to numeric after removing the '%' symbol
df['Weightings'] = df['Weightings'].str.rstrip('%').astype(float)

# Extract the first 'Date' value for the title
date_extracted = df['Date'].iloc[0]

# Sort the dataframe by 'Weightings' in descending order
df = df.sort_values(by='Weightings', ascending=False)

# Remove security names with weightings between -5% and 5%
df = df[(df['Weightings'] < -threshold) | (df['Weightings'] > threshold)]


# Create a vertical bar chart with gradient colors using Plotly
fig = px.bar(df, x='SecurityName', y='Weightings',
             title=f'Security Weightings as of {date_extracted}',
             labels={'SecurityName': 'Security Name', 'Weightings': 'Weightings (%)'},
             orientation='v', color='Weightings', color_continuous_scale='Viridis')

# Update layout for better appearance
fig.update_layout(xaxis={'categoryorder': 'total descending'}, xaxis_tickangle=90)

# Show the plot
fig.show()
