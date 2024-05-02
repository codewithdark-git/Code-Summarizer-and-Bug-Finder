import streamlit as st
import google.generativeai as genai
import os

# Set up GenAI with your Google API key
GOOGLE_API_KEY = os.getenv("gemini_api")
genai.configure(api_key=GOOGLE_API_KEY)

# Function to summarize code and find bugs
def summarize_and_find_bugs(code):
    try:
        model = genai.GenerativeModel("gemini-1.0-pro")
        response = model.generate_content(code)
        bot_response = response.candidates[0].content.parts[0].text
        return bot_response
    except Exception as e:
        return f"Error: {str(e)}"

# Page layout for introduction, usage, and developer information
# Page layout for introduction, usage, and developer information
def intro_page():
    st.title("Welcome to Code Summarizer and Bug Finder")
    st.write("This app allows you to summarize code and find bugs using AI.")

    # Anchor for "How to Use" section
    st.markdown("<a name='how-to-use'></a>", unsafe_allow_html=True)
    st.header("How to Use")
    st.write(
        "To summarize code, simply enter your code in the text area under 'Summarize Code' and click the 'Summarize' button. The app will generate a summary for you.")
    st.write(
        "To find bugs in code, enter your code in the text area under 'Find Bugs' and click the 'Find Bugs' button. The app will identify any potential bugs and suggest improvements.")

    # Anchor for "Developer" section
    # Anchor for "Developer" section
    st.markdown("<a name='developer'></a>", unsafe_allow_html=True)
    st.header("Developer")
    st.write("This app was developed by [DarkCoder](/).")
    st.write("For inquiries, you can reach out to [codewithdark90@gmail.com](mailto:codewithdark90@gmail.com).")

    # Additional links under "Developer" section
    st.write("Connect with the developer:")
    st.markdown(""" [GitHub](https://github.com/codewithdark-git) || [LinkedIn](https://www.linkedin.com/in/codewithdark) || [Facebook](https://www.facebook.com/codewithdark.fb)""")

    # Style the developer section
    st.markdown(
        """
        <style>
        .developer-info {
            background-color: #f0f0f0;
            padding: 10px;
            border-radius: 5px;
            margin-top: 20px;
        }
        .developer-links {
            margin-top: 10px;
        }
        .developer-links a {
            margin-right: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


# Page layout for code summarization and bug finding functionality
def functionality_page():
    st.title("Code Summarizer and Bug Finder")
    st.header("Summarize Code")
    user_input_summarize = st.text_area("Enter your code here to summarize:")
    if st.button("Summarize"):
        with st.spinner('Summarizing...'):
            summary_result = summarize_and_find_bugs(f"Summarize the given code: {user_input_summarize}")
        st.subheader("Summary:")
        st.write(summary_result)

    st.header("Find Bugs")
    user_input_bugs = st.text_area("Enter your code here to find bugs:")
    if st.button("Find Bugs"):
        with st.spinner('Finding bugs...'):
            bugs_result = summarize_and_find_bugs(f"Find bugs in the provided code: {user_input_bugs}")
        st.subheader("Bugs Found:")
        st.markdown(bugs_result)

# Main function to switch between pages
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Introduction", "Functionality"])

    if page == "Introduction":
        intro_page()
    elif page == "Functionality":
        functionality_page()

if __name__ == "__main__":
    main()
