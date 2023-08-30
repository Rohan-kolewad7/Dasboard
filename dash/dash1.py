import streamlit as st
import plotly.express as px
import pandas as pd
import os

st.set_page_config(page_title="Atal Dashboard", page_icon=":bar_chart:", layout="wide")

st.title(":bar_chart: Atal CSV Data Analysis")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)

fl = st.file_uploader(":file_folder: Upload a file", type=(["csv", "txt", "xlsx", "xls"]))
if fl is not None:
    filename = fl.name
    st.write(filename)
    df = pd.read_csv(fl, encoding="ISO-8859-1")
else:
    os.chdir("Atal_Jal_Area.csv")  # Replace with your directory path
    df = pd.read_csv("Atal_Jal_Area.csv", encoding="ISO-8859-1")

col1, col2 = st.columns((2))

# Sidebar filters
st.sidebar.header("Filters")

# State filter
selected_states = st.sidebar.multiselect("Select States", df["State_Name"].unique())

# Filter data based on selected states
if selected_states:
    filtered_df = df[df["State_Name"].isin(selected_states)]
else:
    filtered_df = df.copy()

# Display filtered data
st.subheader("Filtered Data")
st.dataframe(filtered_df)

# Summary table
st.subheader("Summary Table")
summary_table = filtered_df.groupby("State_Name")["District_Name"].nunique()
st.write(summary_table)
#-----------------------------Defaut------------------------------------
# Create a treemap of all states
data = pd.DataFrame({'States': df['State_Name'].unique()})
fig = px.treemap(data, path=['States'], title="Unique States")
st.plotly_chart(fig, use_container_width=True)



# Create a pie chart for state-wise distribution
st.subheader("State-wise Distribution")
state_count = filtered_df["State_Name"].value_counts()
fig = px.pie(state_count, names=state_count.index, values=state_count.values, title="State-wise Distribution")
st.plotly_chart(fig, use_container_width=True)

#------------------------------------------------------------------
# Create a treemap of unique districts in the selected state
if selected_states:
    selected_state = selected_states[0]

    # Group the data by 'State_Name' and collect unique district names
    unique_districts_by_state = filtered_df.groupby('State_Name')['District_Name'].unique()

    # Check if the entered state exists in the dataset
    if selected_state in unique_districts_by_state.index:
        # Get the unique district names for the selected state
        unique_districts = unique_districts_by_state[selected_state]

        # Create a treemap using Plotly Express
        data = pd.DataFrame({'Districts': unique_districts})
        fig = px.treemap(data, path=['Districts'], title=f'Unique Districts in {selected_state}')
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.write("State not found.")

# Download filtered data
csv_data = filtered_df.to_csv(index=False).encode("utf-8")
st.download_button("Download Filtered Data", data=csv_data, file_name="filtered_data.csv", mime="text/csv")


