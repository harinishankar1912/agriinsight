import streamlit as st
import pandas as pd

st.title("🌾 AgriInsight – Agriculture & Climate Q&A")

rain = pd.read_csv("rainfall_data.csv")
crop = pd.read_csv("crop_production.csv")

question = st.text_input("Ask your question:")
if st.button("Get Answer"):
    if "rainfall" in question.lower():
        st.subheader("Average Rainfall Comparison")
        avg = rain.groupby("State")["Rainfall"].mean().reset_index()
        st.dataframe(avg)
        st.caption("Source: IMD dataset (data.gov.in)")
    elif "crop" in question.lower():
        st.subheader("Top Crops by Production")
        top = crop.groupby("Crop")["Production"].sum().reset_index().sort_values(by="Production", ascending=False).head(5)
        st.dataframe(top)
        st.caption("Source: Ministry of Agriculture (data.gov.in)")
    else:
        st.write("Please ask about rainfall or crop production.")
