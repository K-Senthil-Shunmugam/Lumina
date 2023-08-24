import streamlit as st

# Define a main function to encapsulate the Streamlit app
def main():
    # Title with improved font styling
    st.title("Welcome to **LUMINA** (AI-Assisted Chatbot)")
    
    # Sub-header with improved font styling
    st.markdown("#### Please review the following information to gain insight into Lumina's usage and functionalities.")

    # Main content with improved font styling
    st.markdown("Are you a student, a job seeker, an investor, or a CEO/Owner/Entrepreneur? Our AI-assisted chatbot is here to empower you with tailored guidance and support, aligning your unique goals with the latest advancements in technology and business. Discover how our chatbot can be your trusted companion:")

    # Sub-header for Students with improved font styling
    st.write("-" * 20)
    st.markdown("#### For Students / Job Seekers / Current Working Professionals:")
    st.markdown("**Unlock Your Academic Journey**")
    st.markdown("Are you unsure about your field of study? Our chatbot helps students navigate their educational path. Select your area of interest, and receive recommendations on toolkits, advanced skill sets, and trending technologies to integrate into your chosen field of study. Stay ahead of the curve with personalized guidance.")


    # Sub-header for Investors and Startup Aspirants with improved font styling
    st.write("-" * 20)
    st.markdown("#### For Investors and Startup Aspirants:")
    st.markdown("**Navigate the Business Landscape**")
    st.markdown("Investors and aspiring entrepreneurs, discover your path to success. Select your field of interest or industry, and our chatbot will provide expert advice and pathways. Receive recommendations on investment opportunities, project ideas, and emerging domains. Make informed decisions and explore new avenues for growth.")

    # Sub-header for CEOs/Owners/Entrepreneurs with improved font styling
    st.write("-" * 20)
    st.markdown("#### For CEOs/Owners/Entrepreneurs:")
    st.markdown("**Elevate Your Business**")
    st.markdown("CEOs, owners, and entrepreneurs, take control of your company's growth. Analyze your company's stock market data and economic performance by entering your ticker symbols. Our chatbot conducts in-depth time series data analysis and exploratory data analysis. Gain valuable insights and receive future-focused recommendations to drive your company's success.")

# Call the main function to run the Streamlit app
if __name__ == '__main__':
    main()
