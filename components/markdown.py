"""
Markdown sections for the Learn tab
"""

from dash import dcc

learn_markdown = dcc.Markdown(
    """
    Welcome to the Dallas Cost of Living Dashboard🤠
    
    This is a tool that will help you explore changes in the cost of living across various categories such as: 
    
    ## Play
    
    This is the tab where users can explore how different aspects of life in Dallas affect the overall of living. 
    
    It offers interactive tools like dropdown menu that allow you to examine avg costs in different categories, such as: 
    
    - Housing
    - Childcare
    - Groceries
    - Dining Out
    - Utilities
    - Transportation
    
    (all updated quarterly)
    
    Use the "Play" tab to filter and explore trends, and use the "Results" tab to view the visualizations.
    
    You can use these controls to explore two key visualizations: 
    
        Bar Chart: Cost Breakdown
        This chart shows the individual components that make up the selected expense category. For example, choosing "Groceries" reveals the prices of milk, bread, cheese, fruits, veggies, and more - all sourced from real cost-of-living data. 
        
        Line Chart: Housing Price Trends:
        This charts helps visualize how housing affordability has changed over time in Dallas. You can compare 2 different data sources:
        - Traditional Housing Price Index data
            - measure of how home value change over time. It doesn't show actual dollar prices of houses, instead it shows how much prices have increased of decreased compared to a starting point.
            - index is based on 100 in a baseline year (2005) - approx $149,100
            - an index of 150 means home prices have increased by 50% since 2005 - approx $223,650
            - an index of 250 means home prices have decreased by 150% since 2005 - approx $372,750
        - Median Household Income (from FRED)
        
        WHY only housing and income trends for capital expenses? 
        
            Due to dataset constraints and the interest of creating a focused narrative, this dashboard emphasizes housing as the primary capital expense. Future versions could include transportation or education indices as additional capital expenses over time. 
        
        These insights help show the gap between wages and expenses - a key part in understanding affordability in urban areas such as the great Dallas. 
        
        Why this matters: 
        This tab serves mostly as educational. It helps you:
            - Understand the building blocks of monthly living expenses.
            - Reflect on how income stacks up against essential needs. 
            
    ## Results 
    
    The results tab gives yall a summarized view of the read costs of living in Dallas today. This page focuses on current, tangible data to help users understand what essential cateogries like housing, groceries, childcare, and more might cost them on a monthly basis. 
                
    ## Would You Survive in Dallas?
    
     It is a interactive game that puts you in the shoes of a Dallas resident navigating the real cost of living. 
    
    Using the most recent median household income for Dallas County (2023), this tool challenges you to build a realistic monthly budget. You'll make choices in key expense categories like groceries, dining out, transportation, ect. - and see if you'd have enough money left over after... of if you'd be in the red. 
    
    At the end, you'll get a breakdown of your total monthly expenses, how they compare to the median income, and whether you'd made it comfortably, just barely, or not at all. 
    
    It is a lighthearted way to explore serious realities behind affordability in Dallas - all based on real data! 
    
    Below are more in depth information about the each of the options: 
    
         Grocery Options
        
        - Basic Staples: A minimal grocery load including milk, bread, eggs, and rice. Not much variety, but enough to get by. 
        - Protein-Packed: Focused on meat, cheese, and protein, a more nutritious, but pricier. 
        - Full Grocery Mix: A well-rounded basket with meats, dairy grains, fruits, and veggies. More realistic, more expensive. 
        
         Dining Out Options
        
        - Cheap: One McDonald's meal a month. Think tight budgeting and almost no eating out. 
        - Moderate: Two fast food meals, several coffees, and a bear. Reflects occasional treats.
        - Expensive: A nicer dinner, some drinks, and coffee shop trips - a more social, comfortable lifestyle. 
        
         Transportation Options
        
        - Public Transit Pass: The most affordable option if you rely on buses or trains. 
        - Gasoline Only: For those with a car but minimal expenses outside of fuel. 
        - Car Ownership: Includes gas, basic insurance, and maintenance - the true cost of driving. 
    
         Childcare Options
        
        - None:  If you don't have kids or have free care 
        - Home-Based: Based on Dallas averages for home daycare for infants/toddlers 
        - Center-Based: Slightly higher cost - for center based infant/toddler care. 
        
         Housing Options
        
        - Shared Roomate Situation: Half the cost of a 1-bedroom apartment outside the city center
        - 1BR Outside City: A full apartment at more affordable rates than downtown
        - 1BR In City Center: Higher rent, but central location.
    
    Ready to test your survival skills? Head to the Survival tab & give it a try!
    """


)

data_sources = dcc.Markdown(
    """
    ***Data Sources:***
    - Home Price Index: [FRED] (https://www.https://fred.stlouisfed.org/)
    - Cost of Living: Numbeo 
    - Childcare Costs: Compiled static dataset for 2024 Dallas (center/home-based)
    """
)