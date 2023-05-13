import streamlit as st


# Setup wide layout on streamlit
st.set_page_config(page_title = "QA Dashboard")



if __name__ == "__main__":
    st.header("Question-Answering Product Related IoT: ESP32")
    st.image("https://d3n0h9tb65y8q.cloudfront.net/public_assets/assets/000/001/531/original/IOT.png?1635516393")
    text_input = st.text_input("", placeholder = "Input Text Here...")
    if text_input != "":
        # TODO: Implement Question Answering Inference Here.

        st.success(
            "Result Here"
        )