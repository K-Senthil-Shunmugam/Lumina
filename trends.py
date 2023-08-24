# Import necessary libraries
import streamlit as st
import requests

# Function to fetch news articles from the News API
def get_news(keyword, api_key):
    base_url = "https://newsapi.org/v2/everything"
    params = {
        "q": keyword,
        "apiKey": api_key
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    return data.get("articles", [])

# List of recommended keywords
keywords = [
    "Digital Transformation",
    "Fintech Innovation",
    "Cybersecurity Jobs",
    "Blockchain Integration",
    "Artificial Intelligence (AI) Economy",
    "Data Analytics Growth",
    "Cloud Computing Expansion",
    "Tech Startups",
    "Remote Work Opportunities",
    "E-commerce Boom",
    "Financial Inclusion",
    "Mobile Banking",
    "Payment Solutions",
    "Regulatory Compliance",
    "Tech Talent Demand",
    "Automation Impact",
    "Cryptocurrency Adoption",
    "Machine Learning Jobs",
    "Big Data Management",
    "API Development",
    "Financial Technology Trends",
    "Insurtech Advancements",
    "AI-Powered Trading",
    "Economic Resilience",
    "Data Privacy Compliance",
    "Digital Payment Systems",
    "Tech Skills Gap",
    "Mobile App Development",
    "Digital Lending",
    "Economic Recovery Strategies",
    "Wealth Management Technology",
    "Financial Data Security",
    "Tech Education Initiatives",
    "Sustainable Finance",
    "Financial Sector Growth",
    "AI in Customer Service",
    "Tech Investment Opportunities",
    "Remote Cybersecurity Jobs",
    "Digital Marketing Expansion",
    "Financial Regulatory Changes",
    "Tech Policy Development",
    "Cloud Services Expansion",
    "Mobile Payment Solutions",
    "Financial Services Innovation",
    "Tech Ecosystem Development",
    "Robotic Process Automation (RPA)",
    "Financial Incentives",
    "AI Ethics",
    "Data Science Careers",
    "Tech and Finance Partnerships"
]

# Streamlit application
def main():
    
    
    # Get the user's News API key
    api_key = "0c117ea1bf874910bf39d09e5097d7d1"
    
    # Sidebar with dropdown menu
    selected_keyword = st.sidebar.selectbox("Select a keyword for trend search:", keywords)
    
    # Check if a keyword is selected
    if selected_keyword:
        st.title("Trends for '{}'".format(selected_keyword))
        
        # Fetch news articles using the API
        if api_key:
            news_articles = get_news(selected_keyword, api_key)
            if news_articles:
                for article in news_articles:
                    st.write("-" * 20)
                    st.subheader("Title\: "+ article["title"])
                    st.write("Description:", article["description"])
                    st.write("Source:", article["source"]["name"])
                    st.write("URL:", article["url"])
                    
            else:
                st.warning("No news articles found for the selected keyword.")
        else:
            st.warning("Please enter your News API key in the code.")
    
# Run the Streamlit app
if __name__ == "__main__":
    main()