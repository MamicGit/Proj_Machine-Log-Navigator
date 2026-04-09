import streamlit as st

st.set_page_config(page_title="MLN | Bugreport", layout="wide", initial_sidebar_state="expanded")

st.markdown("<u>Support ▪ Bug</u>", unsafe_allow_html=True)
st.markdown("# **Bugreport**")
st.write("Submit a ticket to report website issues, data problems or errors")

col1, col2 = st.columns([2, 2])

with col1:
    in_form = st.container()
    with in_form:
        st.subheader("Ticket")
        with st.form("form_dummy"):
            options = ["- click here - select the most appropriate category -", "Problem with Website", "Error on Dashboard", "Data issue"]
            default_index = 0
            option = st.selectbox(
                label="*Select Category:*",
                options=options,
                index=default_index
            ),
            tt_descr = st.text_area("*Describe the Problem:*")
            submitted  = st.form_submit_button()

st.divider()

if submitted:
    st.markdown("**NOTE:** :red[The ticket content will not be sent in this version, as specific internal company ticket processes must be configured here!]")
    st.write(f"**Category:** {option[0]}")
    st.write("**Description:** ", tt_descr)
