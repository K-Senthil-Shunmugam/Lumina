import streamlit as st
import openai
import pymongo

# Set up OpenAI API key
openai.api_key = st.secrets["API_KEY"]

# Set up MongoDB connection
client = pymongo.MongoClient("mongodb+srv://nullbyte:nullbyte@lumina.mkc3wga.mongodb.net")  
db = client["Lumina"]  # Replace with your actual database name
collection = db["startup"]  

# Streamlit app
def main():
    # Fetch domains from MongoDB
    domains = [doc["_id"] for doc in collection.find({}, {"_id": 1})]

    # Sidebar panel with dropdowns
    selected_domain = st.sidebar.selectbox("Select a Domain:", domains)

    # Fetch subcategories based on selected domain
    subcategories_data = collection.find_one({"_id": selected_domain})
    if subcategories_data:
        subcategories = subcategories_data.get("subcategories", [])

        selected_subcategory = st.sidebar.selectbox("Select a Subcategory:", subcategories)
        submitted = st.sidebar.button("Recommend")

        if submitted:
            # Store user selections in conversation
            conversation = [
                {"role": "system", "content": f"You are a great leader having awesome in depth knowledge in {selected_subcategory} such that you provide valuable insights , advance ideas and unique recommendations and creative ideas for startup aspirants and proper investment of money for investors  relating advance technologies inside it, make it point by point ."},
                {"role": "user", "content": f"Please provide me valuable insights and advance and unique recommendations on {selected_subcategory} under the domain {selected_domain} , provide valuable insights , advance ideas and unique recommendations and creative ideas for startup aspirants and proper investment of money for investors relating advance technologies inside it , make it  point by point . "}
            ]

            # Make an API call to OpenAI for recommendations
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=conversation,
                max_tokens=1000  # Adjust the max tokens as needed
            )

            # Extract and display the AI's response
            ai_response = response['choices'][0]['message']['content']
            st.subheader("Lumina's Recommendations:")
            st.write(ai_response)

if __name__ == "__main__":
    main()
