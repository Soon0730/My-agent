import  streamlit as st

home = st.Page("app.py",title="Home") #landing page
page_1 = st.Page("page_1.py", title="Intro") #hero section
page_2 = st.Page("page_2.py", title="Services") #services section
page_3 = st.Page("page_3.py", title="Login") #login section

pages = st.navigation([home, page_1, page_2, page_3], position="top")

pages.run()


st.title("My Streamlit App")    

# st.write("Welcome to my Streamlit application!") 

# st.markdown("This is a **simple example** of a Streamlit app.")

# st.text_input("Enter your name:", key="name_input")

# st.button("Submit", on_click=lambda: st.write(f"Hello, {st.session_state.name_input}!"))

# st.divider()  # 👈 Draws a horizontal rule


# st.slider("Select a number:", min_value=0, max_value=100, key="number_slider")

# st.divider()  # 👈 Draws a horizontal rule


# st.checkbox("Check this box", key="checkbox")

# st.divider()  # 👈 Draws a horizontal rule

# st.badge("This is a badge example.")

# st.badge("Another badge example.", color="green")

# st.badge("Yet another badge example.", color="blue")

# st.divider()  # 👈 Draws a horizontal rul

# st.text_area("Enter some text:", key="text_area")   

# st.divider

# st.button("Clear Text Area", on_click=lambda: st.session_state.update({"text_area": ""}))

# st.divider()  # 👈 Draws a horizontal rul

# st.selectbox("Choose an option:", options=["Option 1", "Option 2", "Option 3"], key="selectbox")


