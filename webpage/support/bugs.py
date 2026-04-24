import streamlit as st

st.set_page_config(page_title="MLN | Bugreport", layout="wide", initial_sidebar_state="expanded")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # 3 lines Headers of page + dropdowns right side
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
st.markdown("<u>Support ▪ Bug</u>", unsafe_allow_html=True)
st.markdown("# **Bugreport**")
st.write("Submit a ticket to report website issues, data problems or errors")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # creation of ticket system - using 2 columns just for design purposes (smaller ticket-panel)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
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
            if submitted and tt_descr.strip() == "":
                st.markdown(":red[**Note:** Description missing, field cannot be left blank!]")

st.divider()

# showing ticket content after submit
if submitted and tt_descr.strip() != "":
    st.markdown("**NOTE:** :red[In this version, ticket content will not be sent because a company’s internal ticket procedures must be configured first!]")
    st.write(f"**Category:** {option[0]}")
    st.write("**Description:** ", tt_descr)
