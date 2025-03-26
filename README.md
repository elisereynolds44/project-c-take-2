## Dallas Cost of Living Dashboard 
Elise Reynolds - CS 150 Community Action Computing 

## Why Dallas? 

Dallas is not only my hometown, but also a city that has seen rapid economic growth and change over time. By analyzing this region, I hoped to gain insight into how affordability has shifted, and how wage growth compares to increasing costs of essentials. I also wanted to share this with classmates who may be unfamiliar with the area but interested in the realities of life in a major US city as COOL as Dallas Texas. 

## About this Project: 

This dashboard explores the cost of living in Dallas, Texas through an interactive and accessible tool designed for individuals and families looking to understand the financial landscape of this vibrant city. Inspired by my own personal connection to Dallas - I was born and raised here (as you already know from me saying it 100x times by now) - and more recently, by becoming a first-time aunt, over spring break, this project was a way to reflect on what life might look like for my brother as he navigates parenthood, budgeting, and adult responsibilties.

While the dashboard is backed by real data & structured analysis, it is also designed to tell stories - stories like his. It will allow users to see how expenses like groceries, transportation, housing, and childcare add up and compare them to income trends over time. 

## Datasets used: 

I selected 3 datasets for this project: 

    1. Median Household Income (2005-2023)
        - Source: https://fred.stlouisfed.org/series/MHITX48113A052NCEN
        - Dataset liscence: Public use
        - CSV File: medianhouseholdincome.csv
        - year-by-year income data for Dallas County, offering a picture of how household earnings have changed over time. 
    2. Global Cost of Living Dataset
        - Source: https://www.kaggle.com/datasets/mvieira101/global-cost-of-living
        - Dataset liscence:Public use
        - CSV File: cost-of-living.csv
        - Covers detailed cost estimates for daily expenses like groceries, rent, dining out, and more in major ciites worldwide, including Dallas (the one I used obvi)
    3. Housing Price Index (2005-2023)
        - Source: https://trerc.tamu.edu/data/home-price-index/?data-MSA=Dallas-Fort+Worth-Arlington
        - Dataset liscence: Public use
        - CSV File: housing_index.csv
        - This dataset reflects how home prices in Dallas have changed using an index where 2005 = 100. A value in 250 in 2023, for example, would mean home prices are 2.5x higher than they were in 2005.  

## SwD & Dashboard: 

I used several principles from Storytelling with Data and the Big Book of Dashboards including: 
    - clear tab nav to support exploratory analysis
    - minimalist design that highlights data rather than decorations 
    - interactive through dropdowns and user choices
    - thoughtful labeling and color choices 

## Dashboard Features: 

    - Learn Tab: provides educational context, data explanations, and a background info for users unfamiliar with some of the topics 
    - Play Tab: allows users to interactively select expense categories and visualize cost breakdowns. 
        - Dropdown to select expense category 
        - Bar chart visualizes the breakdown of costs within the category 
        - Line chart switches between Median Household Income and Housing Price index over time 
    - Results Tab: Summarizes data tables and displays line charts of income or housing price index over time.
        - Full data table for selected categories costs. 
    - Would You Survive? Tab: a personal favorite, this interactive, game-style features lets users choose monthly lifestyle options (groceries, housing, ect.) and calculates whether they would survive on the average Dallas income. This helps turn abstract numbers into personal decisions. 
        - Choose options for groceries, dining, transportationn, childcare, and housing
        - Click "calculate budget survival" to see if you are overspending or making it 
        - Get a detailed breakdown of your monthly expenses and remaining income    
        - includes a reset/play again button to experiement with different scenariors 

## Example Scenarios: 
1. "Could I afford to live alone in Dallas?"
   - selecting "solo housing", "moderate dining" and "car ownership" shows how fast costs add up and how slim your buffer might be on an average income. 
2. "Have incomes changed since 2005?"
   - the line chart tracks income growth over time - and lets users compare it to inflation and rising expenses. 
3. "What would it take to save for a child?"
   - Selecting childcare options in the game tab reveals how significantly they impact monthly finances, especailly  when combined with transportation and housing. 


## Things I learned along the way: 
- Plotly Line and Scatter Plots 
  - https://stackoverflow.com/questions/72744801/specifying-linetype-in-scatter-plots-of-plotly
  - https://plotly.com/python/line-and-scatter/
  - helped me get a better grasp with these scatter line dot graphs 
- Multi-file Dash App Structure 
  - wasn't super familiar with how this would work but I love the idea of a multi-file strucuture and I will never tearn back
- html.Br() and html.Hr()
  - Br - line break, creates a single line break 
  - Hr - horizontal rule, line across page to visually divide sections 


## Close statements: 
Okay, so — technically, the assignment called for multiple capital expenses and time-series data across the board. And I get that. But after diving into the data that actually exists (and is freely available), I had to make some intentional decisions to balance scope, clarity, and what's actually useful for someone exploring the cost of living in Dallas.

Why I Focused on Just one Capital Expense: 
I chose Housing as the sole capital expense to track over time, and I stand by that decision. Housing is hands down the most significant, consistent cost most people face, especially in a city like Dallas. It's not just a single purchase — it's a monthly reality. And more importantly, I was able to find a strong time-series dataset through the Federal Reserve that gave me real, reliable insight into how housing prices have shifted since 2005.

Sure, I could have thrown in some miscellaneous other capital expenses (like cars or major appliances), but I’d argue that doing so without solid data would have made the dashboard feel more cluttered than insightful. I’d rather do one capital expense well than five half-baked.

Why My Cost of Living Isn't Over Time:
This was probably the biggest challenge. The cost of living dataset I found — which is rich, diverse, and really detailed — only gives a snapshot of one point in time. That’s not ideal if we’re talking about change over time, but I saw it as a creative opportunity rather than a limitation.

Instead of forcing a trend line where there wasn’t one, I used that data to build my favorite part of the whole dashboard: the "Would You Survive?" interactive game tab. If I can’t show change over time for things like groceries, childcare, and transportation, I can at least let users experience the impact of those costs right now, based on real, recent data. That feels like a much more engaging and relevant way to highlight how those costs affect people today — especially someone like my brother, who just had a baby and is staring down these exact choices.

Final Thoughts: 
I approached this project with real people in mind. I wanted it to be personal, local, and usable — not just a technical checklist. So while I didn’t include multiple capital expenses or have all my datasets in time-series format, I did design a dashboard that lets users explore income, housing trends, and real-life spending decisions with clarity and impact.

And honestly? I think that’s the whole point.

Also, if you are curious I have included some photos of my nephew in my project! His name is Theodore!!!!!

## Feedback Exchange 

To make the budget simulation more realistic for different household types, I expanded the housing options in the "Would You Survive" game tab:
- Added 2 new housing choices for families: 
  - 3 BR Outside City Center (Family Option)
  - 3 BR In City Center (Family Option)
- Updated the logic to properly handle these new dropdown values and get the corresponding price data
    
Also, to better reflect the cost of groceries for a typical 3-person household, I revised the logic i the "Would You Survive" tab: 
- Added quantity multipliers to each grocery item in the budget simulation to more accurately simulate what a 3-person family might consume in a month. 
- updated all grocery option mappings (basic, protein, full) to include both the item name and an estimated monthly quantity.
- Adjusted the calculation logic from a simple sum() to a weighted total using item quantity x unit price


