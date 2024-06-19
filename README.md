
# HFND Positioning Analysis

This project aims to analyze the security weightings from a specified ETF's holdings data. The primary goal is to visualize the weightings of various securities in the ETF portfolio using a bar chart with gradient colors. 

## Features
- Data cleaning and preprocessing.
- Filtering securities based on weightings.
- Visualizing the data using Plotly.

## Getting Started

### Prerequisites

To run this project, you need to have the following Python libraries installed:
- pandas
- plotly

You can install these libraries using pip:
```bash
pip install pandas plotly
```

### How to Run

1. Clone the repository or download the `HFND_positioning.py` file.
2. Ensure you have the required libraries installed.
3. Run the `HFND_positioning.py` script:
   ```bash
   python HFND_positioning.py
   ```

### Script Details

The script performs the following steps:

1. **Loading the Data:**
   - The script loads data from a specified URL (CSV file) containing the ETF's holdings.

2. **Data Cleaning:**
   - It strips any leading or trailing spaces from the column names.
   - Converts the 'Weightings' column from a string percentage to a numeric value.

3. **Data Filtering:**
   - The script sorts the dataframe by 'Weightings' in descending order.
   - Filters out securities with weightings between -2% and 2%.

4. **Visualization:**
   - A vertical bar chart is created using Plotly.
   - The chart uses a gradient color scale (Viridis) to represent the weightings.
   - The x-axis is sorted by the total descending order of the weightings.
   - The chart is titled based on the date extracted from the data.

## Example Output

The script will produce an interactive bar chart displaying the security weightings. The chart will look similar to this:

![Example Chart](example_chart.png) *Note: Add a screenshot of the generated chart here.*

## Contributions

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Data source: [Unlimited ETFs](https://www.unlimitedetfs.com/)
- Libraries: pandas, plotly

---

Feel free to customize this README further based on your specific needs and additional details of the project.
