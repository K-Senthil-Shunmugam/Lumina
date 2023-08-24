import streamlit as st
import openai
import pymongo

# Set up OpenAI API key
openai.api_key = st.secrets["API_KEY"]

# Set up MongoDB connection
client = pymongo.MongoClient(st.secrets["CONNECTION_STRING"])  
db = client["Lumina"]
collection = db["student"]

# Initialize conversation
conversation = []

# Streamlit app
def main():
    # Fetch domains from MongoDB
    domains = [doc["_id"] for doc in collection.find({}, {"_id": 1})]

    # Sidebar panel with dropdowns
    selected_domain = st.sidebar.selectbox("Select a Domain:", domains)

    # Fetch subcategories based on selected domain
    subcategories_data = collection.find_one({"_id": selected_domain})
    if subcategories_data:
        subcategories = [subcat["name"] for subcat in subcategories_data.get("subcategories", [])]

        selected_subcategory = st.sidebar.selectbox("Select a Subcategory:", subcategories)

        # Fetch job roles based on selected subcategory
        job_roles_data = [subcat for subcat in subcategories_data.get("subcategories", []) if subcat["name"] == selected_subcategory]
        if job_roles_data:
            job_roles = job_roles_data[0].get("job_positions", [])

            selected_job_role = st.sidebar.selectbox("Select a Job Role:", job_roles)

            submitted = st.sidebar.button("Recommend")

            if submitted:
                # Store user selections in conversation
              
                
                conversation.append({"role": "system", "content": f"You are a leader in {selected_subcategory} providing recommendations to a new individual who is a aspirant for the {selected_subcategory}."})
                conversation.append({"role": "user", "content": f"I am currently interested in learning advanced skillsets in {selected_job_role} in {selected_subcategory} under the domain of {selected_domain}. Please provide recommendations on advance skillset , technical toolkits : list the skillsets and toolkits only in the form of a table ."})

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

    # Sidebar chat input
    st.sidebar.subheader("Chat with Lumina:")
    user_input = st.sidebar.text_input("You:", "")

    if user_input:
        # Add user input to the conversation
        conversation.append({"role": "user", "content": user_input})

        # Continue the conversation with OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversation,
            max_tokens=1000  # Adjust the max tokens as needed
        )

        # Extract and display the AI's response
        ai_response = response['choices'][0]['message']['content']
        st.subheader("Lumina's Response:")
        st.write("Lumina: " + ai_response)

if __name__ == "__main__":
    main()
