import streamlit as st
from PIL import Image

st.set_page_config(page_title="MLN | Dashboard", layout="wide", initial_sidebar_state="expanded")

st.markdown("<u>Dashboard & Data ▪ Dashboard</u>", unsafe_allow_html=True)

# # # Dashboard header elements
col1, col2, col3 = st.columns([3,2,1])
with col1:
    st.markdown("# **Dashboard**")
    st.write("KPI's & Statistics for Packaging Line Controlling")
with col2:
    st.write("")
with col3:
    options = ["SLAM-ALL", "SLAM01", "SLAM02", "SLAM03", "SLAM04", "SLAM05", "SLAM06", "SLAM07", "SLAM08", "....."]
    default_index = 0
    option = st.selectbox(
        label="**Select Packaging Line Station** \n\n(*SLAM-STATION*)",
        options=options,
        index=default_index
    )

st.write("")

# # # KPI Section
with st.container():
    col1, col2, col3, col4, col5, col6, col7 = st.columns([1, 1, 1, 1, 1, 1, 1])
    with col1:
        st.write("")
        st.subheader("KPI's:")
        st.write("Controlling")
    with col2:
        # between 0.8 and 2.4 | 2.38 Threshold
        # eventuell berechnen Durchschnitt letzte 3 Pakete mit dem ... ?

        conv_spd = 2.37
        conv_spd_threshold = 2.38

        if conv_spd > 2.38:
            status = f"🔴 high risk"
        elif conv_spd > 2.36:
            status = f"🟡 medium risk"
        else:
            status = f"🟢 no risk"

        st.markdown("<u>**Conveyer speed**</u>", unsafe_allow_html=True)
        st.subheader(f"{conv_spd} m/s")
        st.write(status)
    with col3:
        st.markdown("<u>**Print Head 1**</u>", unsafe_allow_html=True)
        st.subheader("99.5 %")
        f"🟢 OK"
    with col4:
        st.markdown("<u>**Print Head 2**</u>", unsafe_allow_html=True)
        st.subheader("98.7 %")
        f"🟢 OK"
    with col5:
        st.markdown("<u>**Kickout Rate**</u>", unsafe_allow_html=True)
        st.subheader("21.2 %")
        f"🟢 OK"
    with col6:
        st.markdown("<u>**Defect-Rate**</u>", unsafe_allow_html=True)
        st.subheader("4.0 %")
        f"🟢 OK"
    with col7:
        st.markdown("<u>**Conveyor-Stops**</u>", unsafe_allow_html=True)
        st.subheader("5")
        f"🟢 OK"

st.write("")
col1, col2 = st.columns([1,6])
with col1:
    st.write("**Recommendation for action:**")
with col2:
    st.write("The conveyer speed could be problematic, please check")
st.write("**NOTE:** *Action items will be displayed by priority starting with highest. After resolve please make sure to reset the error log on machine control panel !*")
st.divider()

st.markdown(
    "### <span style='color:red; text-decoration:underline; font-weight:bold;'>Page is under construction !</span>",
    unsafe_allow_html=True)