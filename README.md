# US Homelessness Analysis: State-Level Trends and Population Correlation (2007-2024)

## 📋 Project Overview

The idea for this research came to me unexpectedly. I was honing my Python Pandas skills using an outdated homelessness dataset on DataCamp and became curious about the current situation. Moving to Seattle recently, I noticed a significant number of homeless individuals, which led me to assume that Washington state might have more homeless people than New York. This project became an opportunity to validate my expectations with real-world data while simultaneously practicing my Python skills.

This project analyzes homelessness trends across US states using official data from the US Department of Housing and Urban Development (HUD) and US Census Bureau population estimates. The analysis aims to provide insights into the distribution and scale of homelessness across different states, which can inform policy decisions and resource allocation for addressing homelessness.

### Key Findings
- Identification of states with highest absolute homeless populations
- Analysis of homelessness patterns across different states and territories
- Correlation between state population size and homeless population counts

## 📊 Dataset Description

### Primary Data Sources

#### 1. HUD Point-in-Time (PIT) Estimates (2007-2024)
- **Source**: US Department of Housing and Urban Development
- **URL**: [2024 AHAR Part 1 PIT Estimates](https://www.huduser.gov/portal/datasets/ahar/2024-ahar-part-1-pit-estimates-of-homelessness-in-the-us.html)
- **File**: 2007-2024-PIT-Counts-by-State.xlsb
- **Description**: Annual Point-in-Time counts of homeless individuals across all US states and territories
- **Coverage**: All 50 states plus DC and US territories
- **Time Period**: 2007-2024

#### 2. US Census Bureau Population Estimates (2024)
- **Source**: US Census Bureau
- **Description**: Latest available population estimates for all US states and territories
- **Year**: 2024
- **Coverage**: All 50 states, DC, and major US territories (Puerto Rico, Guam, Virgin Islands, Northern Mariana Islands, American Samoa)

#### 3. USA states GeoJson
- **Source**: Kaggle
- **URL**: https://www.kaggle.com/datasets/pompelmo/usa-states-geojson/data
- **Description**: GeoJson encoding for usa states, for map plots

### Data Structure
- **Total Records**: 56 jurisdictions (50 states + DC + 5 territories)
- **Key Variables**:
  - `State`: Two-letter state/territory abbreviation
  - `Overall Homeless`: Total count of homeless individuals (2024 PIT count)
  - `Population 2024`: Total population estimate for 2024

## 🔍 Analysis Overview

### Current Analysis Completed

#### 1. Data Exploration and Cleaning
- Loaded and processed HUD XLSB file format
- Cleaned data to remove totals and non-state entries
- Filtered for valid numeric homeless population counts
- Merged homeless data with population estimates

#### 2. Top States Analysis
- **Initial Observation vs. Reality**: My partner and I initially expected New York to have the most homeless people. However, the analysis revealed that California holds the highest absolute homeless population in 2024. This was a significant and unexpected finding, clearly visualized in the bar chart of top 10 states by absolute homeless population.
- **Key Insights**:
Identified states with highest homeless populations
Clear visualization of the disparity between states
Analysis excludes national totals for accurate state-level comparison


#### 3. Population Correlation Preparation
- Merged homeless population data with 2024 Census population estimates
- Created combined dataset for correlation analysis between state population size and homeless counts
- **Homelessness Rate per 100K Population**: To gain a deeper understanding, I calculated the homelessness ratio per 100,000 people using data from official governmental websites. And what would you expect?
- **Hawaii** is ranked number one in 2024 for the density of homeless individuals.
- **New York** is in third place for the highest homelessness rate per 100K population.
- **Washington** state is also in the top 10 for homelessness rate per 100K population, confirming my initial observation about Seattle's situation.

#### 4. Sheltered vs. Unsheltered Analysis
- **An Unexpected Discrepancy**: Another unexpected finding that caught our attention was the amount of sheltered versus unsheltered people. While roughly half of the homeless population in California in 2024 was unsheltered, more than 80% of homeless individuals in New York were sheltered. This leaves New York with even fewer unsheltered people than Washington state, despite its higher absolute homeless population.


### Methodology
- **Data Processing**: Pandas for data manipulation and cleaning
- **Visualization**: Matplotlib and Seaborn for chart creation, Plotly Express for interactive maps
- **Statistical Analysis**: Descriptive statistics and data exploration

## 📈 Key Visualizations

1. **Top 10 States by Homeless Population (2024)**
2. **Top 10 States with The Highest Population**
3. **10 States with The Highest Ratio of Homeless per 100K Population**
4. **10 States with The Lowest Ratio of Homeless per 100K Population**
5. **Yearly Change in Overall Homeless Count for 10 States**
6. **Sheltered vs. Unsheltered Homeless by States With The Highest Amount of Overall Homeless in 2024**
7. **Overall Homelessness by State in 2024 (Heatmap)**
8. **Homelessness Ratio Per 100K Population by State in 2024 (Heatmap)**

![Alt text for the image](Vizualizations/US_States_Pop_2024.png)
- **General Information** on the States Population in 2024

![Alt text for the image](Vizualizations/top_10_states_homeless_2024.png)

- **Insight**: In 2024, **California and New York** have a significantly larger overall homeless population, totaling 345,103 individuals (187,084 in California and 158,019 in New York). This combined figure represents approximately **44.7% of the entire U.S. homeless population of 771,480**.
- *My initial expectation* was that New York would have the highest number of homeless people. However, the data clearly shows that California has a significantly larger absolute homeless population in 2024.

![Alt text for the image](Vizualizations/Top10_Homelessness_Rate100K.png)

- **Insight**: A significant and concerning trend emerges in **Hawaii, Washington D.C., and New York**. In 2024, **nearly 1% of the 100K population** in these areas was **experiencing homelessness**. Specifically, there are approximately 805 homeless individuals per 100,000 residents in Hawaii, 800 per 100,000 in Washington D.C., and 795 per 100,000 in New York, underscoring the severe housing challenges faced by these populations.
- *This metric reveals a different story! Hawaii is indeed Number 1 for density. New York is in 3rd place, and **Washington state** makes it into the highest 10.*
  
![Alt text for the image](Vizualizations/Bottom10_Homelessness_Rate100K.png)

- **Insight**: **Mississippi** had one of the **lowest** numbers of people experiencing homelessness per 100K population in 2024.

![Alt text for the image](Vizualizations/yearly_trend.png)

- **Insight**: **California** experienced a **notable fluctuation** in its homeless population **around 2021**. The count reportedly dropped significantly from 162K to 57K, only to rise again to 172K. This dramatic shift prompts questions about the factors at play, particularly concerning the aftermath of the COVID-19 pandemic and its impact on homelessness trends in the state.
  
![Alt text for the image](Vizualizations/Sheltered_VS_Unsheltered.png)

- Insight: While about **66% (124,000 out of 187,000) of California's** homeless population in 2024 was **unsheltered**, over **96%(152,000 out of 158,000) of New York's** homeless were **sheltered**. Interestingly, this means **New York** actually has a **lower** number of unsheltered individuals than **Washington State**, despite New York's much higher overall homeless count.

## 🛠️ Technical Implementation

### Requirements
python
pandas
matplotlib
seaborn
pyxlsb # For reading Excel Binary files
plotly # For interactive visualizations (heatmaps)

### Project Structure
```
├── data/
│   ├── raw/
│   │   └── 2007-2024-PIT-Counts-by-State.xlsb
│   └── geojson/
│       └── us_states.geojson # Assuming you've renamed/placed the geojson here
├── notebooks/
│   └── Homelessness_US_Analysis.ipynb
├── src/
│   └── analysis.py
├── visualizations/
│   ├── US_States_Pop_2024.png
│   ├── top_10_states_homeless_2024.png
│   ├── Top10_Homelessness_Rate100K.png
│   ├── Bottom10_Homelessness_Rate100K.png
│   ├── yearly_trend.png
│   ├── Sheltered_VS_Unsheltered.png
│   ├── us_homelessness_heatmap_2024.html
│   └── us_homelessness_ratio_heatmap_2024.html
├── README.md
```


## 🎯 Research Applications

This analysis can be valuable for:
- **Policy Makers**: Understanding state-level homelessness distribution
- **Non-Profit Organizations**: Resource allocation and program planning
- **Researchers**: Baseline data for homelessness studies
- **Public Health Officials**: Population health planning
- **Urban Planners**: Housing and service planning

## 🔮 Future Analysis Opportunities

1. **Demographic Breakdown**: Analyze by age, family status, and veteran status
2. **Correlation Studies**: Examine relationships with housing costs, unemployment, weather patterns
3. **Predictive Modeling**: Forecast future trends based on historical data

## 📊 Data Quality Notes

- All data sources are official government statistics
- PIT counts represent annual snapshots, typically conducted in January
- Population estimates are the most recent available from Census Bureau
- Some territories may have limited historical data availability

## 🤝 Contributing

This project welcomes contributions, particularly:
- Additional data sources (housing costs, economic indicators)
- Advanced statistical analysis
- Interactive visualizations
- Geographic mapping capabilities

## 📄 License

This project uses publicly available government data. Please cite original data sources when using this analysis.

## 📞 Contact

- Linkedin: linkedin.com/in/azhar-kudaibergen/
- Email: kuda.azhar@gmail.com
---

**Data Sources**:
- US Department of Housing and Urban Development - Annual Homeless Assessment Report
- US Census Bureau - Population Estimates Program
