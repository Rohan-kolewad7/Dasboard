import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import seaborn as sns


st.title("Water in India: A Dashboard of Information")

rainfall_state_url = 'https://raw.githubusercontent.com/Rohan-kolewad7/Dasboard/main/dash/Daily_Rainfall_data_from_IMD_and_NRSC_2018_2023_Cleaned.csv'
cleaned_url = 'https://raw.githubusercontent.com/Rohan-kolewad7/Dasboard/main/dash/Daily_Sub-basin-wise_Rainfall_data_from_IMD_and_NRSC_2018_2023_Cleaned.csv'
surface_url = 'https://raw.githubusercontent.com/Rohan-kolewad7/Dasboard/main/dash/SW_CPCP_and_CWC_Cleaned.csv'
reservoirs_url = 'https://raw.githubusercontent.com/Rohan-kolewad7/Dasboard/main/dash/Daily_data_of_reservoir_level_of_CWC_Agency_2000_2023.csv'

# Load CSV data into DataFrames
df_rainfall_state = pd.read_csv(rainfall_state_url)
df_rainfall_state['Date'] = pd.to_datetime(df_rainfall_state['Date'])

df_cleaned = pd.read_csv(cleaned_url)
df_cleaned['Date'] = pd.to_datetime(df_cleaned['Date'])

df_surface = pd.read_csv(surface_url)
df_reservoirs = pd.read_csv(reservoirs_url)

# # Load your CSV data into a DataFrame
# df_rainfall_state = pd.read_csv('Daily_Rainfall_data_from_IMD_and_NRSC_2018_2023_Cleaned.csv')

# # Convert the 'Date' column to datetime format
# df_rainfall_state['Date'] = pd.to_datetime(df_rainfall_state['Date'])


# # Load your CSV data into a DataFrame
# df_cleaned = pd.read_csv('Daily_Sub-basin-wise_Rainfall_data_from_IMD_and_NRSC_2018_2023_Cleaned.csv')

# # Convert the 'Date' column to datetime format
# df_cleaned['Date'] = pd.to_datetime(df_cleaned['Date'])


# # Load your CSV data into a DataFrame
# df_surface = pd.read_csv('SW_CPCP_and_CWC_Cleaned.csv')


# # Load your dataset into a DataFrame
# df_reservoirs = pd.read_csv('Daily_data_of_reservoir_level_of_CWC_Agency_2000_2023.csv')

# # Convert the 'Date' column to datetime format
# df_reservoirs['Date'] = pd.to_datetime(df_reservoirs['Date'])



# Set up the sidebar
st.sidebar.title('Water Category')

# User selects a category using a selectbox
selected_category1 = st.sidebar.selectbox("Select Category", ["Select an option", "Rainfall of States", "Rainfall of Sub-basin", "Surface Water Quality", "Reservoir Water Level"])

# Perform actions based on the selected option
if selected_category1 != "Select an option":
    st.title('Rainfall Analysis of States')

    if selected_category1 == "Rainfall of States":
        st.write("You selected: Rainfall of States")

        # Bar plot of average rainfall across all years for each month.
        st.subheader('Average Rainfall Across Months')
        monthly_avg_rainfall = df_rainfall_state.groupby(df_rainfall_state['Date'].dt.month)['Avg_rainfall'].mean()
        fig, ax = plt.subplots()
        monthly_avg_rainfall.plot(kind='bar', ax=ax)
        plt.xlabel('Month')
        plt.ylabel('Average Rainfall')
        plt.title('Average Rainfall Over Months')
        plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
        st.pyplot(fig)



        # Bar plot of average rainfall across all years.
        st.subheader('Average Rainfall Across Years')
        df_rainfall_state['Year'] = df_rainfall_state['Date'].dt.year
        yearly_avg_rainfall = df_rainfall_state.groupby('Year')['Avg_rainfall'].mean()
        fig, ax = plt.subplots()
        yearly_avg_rainfall.plot(kind='bar', ax=ax)
        plt.xlabel('Year')
        plt.ylabel('Average Rainfall')
        plt.title('Average Rainfall Over Years')
        plt.xticks(rotation=90)
        st.pyplot(fig)



        # Line plot to compare the data collected by different agencies over time.
        st.subheader('Average Rainfall Comparison for Selected Agencies')
        df_rainfall_state['Year'] = df_rainfall_state['Date'].dt.year
        selected_agencies = ['IMD GRID MODEL', 'NRSC VIC MODEL']
        filtered_df = df_rainfall_state[df_rainfall_state['Agency_name'].isin(selected_agencies)]
        agency_yearly_avg_rainfall = filtered_df.groupby(['Year', 'Agency_name'])['Avg_rainfall'].mean().reset_index()
        pivot_table = agency_yearly_avg_rainfall.pivot(index='Year', columns='Agency_name', values='Avg_rainfall')
        fig, ax = plt.subplots()
        pivot_table.plot(kind='line', marker='o', ax=ax)
        plt.xlabel('Year')
        plt.ylabel('Average Rainfall')
        plt.title('Average Rainfall Comparison for Selected Agencies')
        plt.legend(title='Agency')
        st.pyplot(fig)



        # Plot monthly average rainfall over the years using Plotly
        st.subheader('Monthly Average Rainfall Over Years (Plotly)')
        df_rainfall_state['Date'] = pd.to_datetime(df_rainfall_state['Date'])
        monthly_avg_rainfall = df_cleaned.groupby(df_rainfall_state['Date'].dt.to_period('M'))['Avg_rainfall'].mean().reset_index()
        monthly_avg_rainfall['Date'] = monthly_avg_rainfall['Date'].astype(str)
        fig = px.bar(monthly_avg_rainfall, x='Date', y='Avg_rainfall', title='Monthly Average Rainfall')
        fig.update_traces(marker_color='blue')
        high_rainfall_threshold = 50
        high_rainfall_df = monthly_avg_rainfall[monthly_avg_rainfall['Avg_rainfall'] >= high_rainfall_threshold]
        scatter_fig = px.scatter(high_rainfall_df, x='Date', y='Avg_rainfall', text='Avg_rainfall', color_discrete_sequence=['red'])
        fig.add_trace(scatter_fig.data[0])
        fig.update_layout(xaxis_title='Date', yaxis_title='Average Rainfall', legend_title='Events')
        st.plotly_chart(fig)



        # Bar plot of average rainfall comparison between states.
        st.subheader('Average Rainfall Comparison between States')
        state_avg_rainfall = df_rainfall_state.groupby('State')['Avg_rainfall'].mean().reset_index()
        state_avg_rainfall = state_avg_rainfall.sort_values(by='Avg_rainfall', ascending=False)
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(state_avg_rainfall['State'], state_avg_rainfall['Avg_rainfall'], color='blue')
        plt.xticks(rotation=90)
        plt.xlabel('State')
        plt.ylabel('Average Rainfall')
        plt.title('Average Rainfall Comparison between States')
        plt.tight_layout()
        st.pyplot(fig)



        # Line plot of average rainfall across year.
        st.subheader('Average Rainfall Across Years')
        yearly_avg_rainfall = df_rainfall_state.groupby(df_rainfall_state['Date'].dt.year)['Avg_rainfall'].mean()
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(yearly_avg_rainfall.index, yearly_avg_rainfall.values, marker='o', color='blue')
        plt.xlabel('Year')
        plt.ylabel('Average Rainfall')
        plt.title('Average Rainfall Across Years')
        plt.grid(True)
        plt.tight_layout()
        st.pyplot(fig)



        # User inputs state name and sees all the districts with their average rainfall.
        st.subheader("Select a State to See Average Rainfall of Districts")
        # User input for state (make it case-insensitive)
        user_state = st.selectbox("Select a state:", df_rainfall_state['State'].unique(), key="user_state")

        if st.button("Show District Average Rainfall", key="show_district_avg_rainfall"):
            # Filter the DataFrame based on the user's input state
            filtered_df = df_rainfall_state[df_rainfall_state['State'].str.lower() == user_state.lower()]

            if filtered_df.empty:
                st.write("No data found for the given state.")
            else:
                # Calculate the mean of average rainfall per district
                district_avg_rainfall = filtered_df.groupby('District')['Avg_rainfall'].mean().reset_index()

                # Create a bar plot with highlighted mean of average rainfall
                fig = px.bar(district_avg_rainfall, x='Avg_rainfall', y='District', orientation='h',
                             title=f'Average Rainfall by District in {user_state.capitalize()}',
                             labels={'Avg_rainfall': 'Average Rainfall', 'District': 'District'})

                # Highlight mean of average rainfall with a different color
                mean_rainfall = district_avg_rainfall['Avg_rainfall'].mean()
                fig.add_vline(x=mean_rainfall, line_dash="dash", line_color="red",
                              annotation_text=f'Mean: {mean_rainfall:.2f}', annotation_position="top right")

                # Color code bars based on the average rainfall (customize color here)
                fig.update_traces(marker_color='skyblue', textposition='outside')

                # Customize layout
                fig.update_layout(xaxis_title='Average Rainfall', yaxis_title='Districts',
                                  legend_title='Average Rainfall', yaxis={'categoryorder':'total ascending'},
                                  height=800, width=1100)  # Change the size of the plot here

                # Show the plot
                st.plotly_chart(fig)



        # User inputs state name and sees mean, min, and max rainfall of districts.
        st.subheader("Select a State to See Rainfall Statistics of Districts")
        # User input for state (make it case-insensitive)
        user_state_stats = st.selectbox("Select a state:", df_rainfall_state['State'].unique(), key="user_state_stats")

        if st.button("Show District Rainfall Statistics", key="show_district_rainfall_stats"):
            # Filter the DataFrame based on the user's input state for statistics
            filtered_stats_df = df_rainfall_state[df_rainfall_state['State'].str.lower() == user_state_stats.lower()]

            if filtered_stats_df.empty:
                st.write("No data found for the given state.")
            else:
                # Calculate the mean, max, and min of average rainfall per district
                district_stats = filtered_stats_df.groupby('District')['Avg_rainfall'].agg(['mean', 'max', 'min']).reset_index()

                # Create a bar plot with mean, max, and min of average rainfall
                fig = px.bar(district_stats, x='District', y=['mean', 'max', 'min'],
                             title=f'Rainfall Statistics by District in {user_state_stats.capitalize()}',
                             labels={'value': 'Rainfall', 'District': 'District'},
                             color_discrete_map={'mean': 'yellow', 'max': 'skyblue', 'min': 'red'})

                # Customize layout
                fig.update_layout(xaxis_title='Districts', yaxis_title='Rainfall',
                                  legend_title='Statistics', barmode='group', xaxis_tickangle=-90,
                                  height=600, width=1000)  # Change size of the plot here

                # Show the plot
                st.plotly_chart(fig)



        # User inputs state name and sees mean, min and max rainfall over the years.
        st.subheader("Select a State to See Rainfall Statistics Over the Years")
        # User input for state (make it case-insensitive)
        user_state = st.selectbox("Select a state:", df_rainfall_state['State'].unique(), key="user_state_years")

        if st.button("Show Rainfall Statistics Over the Years", key="show_state_rainfall_stats"):
            # Filter the DataFrame based on the user's input state
            filtered_df = df_rainfall_state[df_rainfall_state['State'].str.lower() == user_state.lower()]

            if filtered_df.empty:
                st.write("No data found for the given state.")
            else:
                # Calculate the mean, max, and min of average rainfall for the entire state for each year
                state_stats = filtered_df.groupby(['Year'])['Avg_rainfall'].agg(['mean', 'max', 'min']).reset_index()

                # Create a line plot for each year with mean, max, and min of average rainfall for the state
                fig = px.line(state_stats, x='Year', y=['mean', 'max', 'min'],
                              title=f'Rainfall Statistics for {user_state.capitalize()} (Each Year)',
                              labels={'value': 'Rainfall', 'Year': 'Year'},
                              color_discrete_map={'mean': 'blue', 'max': 'green', 'min': 'red'})

                # Customize line shape (make it thicker)
                fig.update_traces(line=dict(width=5.0))

                # Customize layout
                fig.update_layout(xaxis_title='Year', yaxis_title='Rainfall',
                                  legend_title='Statistics', barmode='group',
                                  height=600, width=800)  # Change size of the plot here

                # Show the plot
                st.plotly_chart(fig)



        # User inputs district name to see the average, max, and min of rainfall for the district over the years.
        st.subheader("Select a District to See Rainfall Statistics Over the Years")
        # User input for district (make it case-insensitive)
        user_district = st.selectbox("Select a district:", df_rainfall_state['District'].unique(), key="user_district_years")

        if st.button("Show Rainfall Statistics for District Over the Years", key="show_district_rainfall_statsssss"):
            # Filter the DataFrame based on the user's input district
            filtered_df = df_rainfall_state[df_rainfall_state['District'].str.lower() == user_district.lower()]

            if filtered_df.empty:
                st.write("No data found for the given district.")
            else:
                # Get the unique state name for the district
                state_name = filtered_df['State'].iloc[0]

                # Calculate the average, max, and min of average rainfall for the district over the years
                district_stats = filtered_df.groupby('Year')['Avg_rainfall'].agg(['mean', 'max', 'min']).reset_index()

                # Create a line plot for average, max, and min of average rainfall for the district over the years
                fig = px.line(district_stats, x='Year', y=['mean', 'max', 'min'],
                              title=f'Rainfall Statistics for {user_district.capitalize()} District ({state_name.capitalize()}) (Over the Years)',
                              labels={'value': 'Rainfall', 'Year': 'Year'},
                              color_discrete_map={'mean': 'blue', 'max': 'green', 'min': 'red'})

                # Customize line shape (make it thicker)
                fig.update_traces(line=dict(width=5.0))

                # Add annotation to highlight state name
                fig.add_annotation(text=state_name.capitalize(),
                                   xref='paper', yref='paper',
                                   x=0.95, y=0.9,
                                   showarrow=False,
                                   font=dict(size=12, color='darkblue'))

                # Customize layout
                fig.update_layout(xaxis_title='Year', yaxis_title='Rainfall',
                                  legend_title='Statistics',
                                  height=600, width=800)  # Change size of the plot here

                # Show the plot
                st.plotly_chart(fig)



        # User inputs year and sees average rainfall of all states across that year.
        st.subheader("Select a Year to See Average Rainfall Across States")
        # User input for year (between 2018 and 2023)
        user_year = st.selectbox("Select a year:", range(2018, 2024), key="user_year_states")

        if st.button("Show Average Rainfall Across States", key="show_avg_rainfall_states"):
            # Filter the DataFrame based on the user's input year
            filtered_df = df_rainfall_state[df_rainfall_state['Year'] == user_year]

            if filtered_df.empty:
                st.write(f"No data found for the year {user_year}.")
            else:
                # Calculate the mean rainfall for each state for the specified year
                state_avg_rainfall = filtered_df.groupby('State')['Avg_rainfall'].mean().reset_index()

                # Create a bar plot for mean rainfall of all states for the specified year
                fig = px.bar(state_avg_rainfall, x='State', y='Avg_rainfall',
                             title=f'Average Rainfall Across States in {user_year}',
                             labels={'Avg_rainfall': 'Average Rainfall', 'State': 'State'})

                # Customize layout
                fig.update_layout(xaxis_title='State', yaxis_title='Average Rainfall',
                                  legend_title='Average Rainfall',
                                  xaxis={'categoryorder': 'total descending'},
                                  height=600, width=1100)  # Change size of the plot here

                # Show the plot
                st.plotly_chart(fig)



    elif selected_category1 == "Rainfall of Sub-basin":
        st.write("You selected: Rainfall of States")

        # Bar plot of average rainfall across all years for each month.
        st.subheader('Average Rainfall Across Months')
        monthly_avg_rainfall = df_cleaned.groupby(df_cleaned['Date'].dt.month)['Avg_rainfall'].mean()
        fig, ax = plt.subplots()
        monthly_avg_rainfall.plot(kind='bar', ax=ax)
        plt.xlabel('Month')
        plt.ylabel('Average Rainfall')
        plt.title('Average Rainfall Over Months')
        plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
        st.pyplot(fig)


        # Bar plot of average rainfall across all years.
        st.subheader('Average Rainfall Across Years')
        df_cleaned['Year'] = df_cleaned['Date'].dt.year
        yearly_avg_rainfall = df_cleaned.groupby('Year')['Avg_rainfall'].mean()
        fig, ax = plt.subplots()
        yearly_avg_rainfall.plot(kind='bar', ax=ax)
        plt.xlabel('Year')
        plt.ylabel('Average Rainfall')
        plt.title('Average Rainfall Over Years')
        plt.xticks(rotation=90)
        st.pyplot(fig)


        # Line plot to compare the data collected by different agencies over time.
        st.subheader('Average Rainfall Comparison for Selected Agencies')
        df_cleaned['Year'] = df_cleaned['Date'].dt.year
        selected_agencies = ['IMD GRID MODEL', 'NRSC VIC MODEL']
        filtered_df = df_cleaned[df_cleaned['Agency_name'].isin(selected_agencies)]
        agency_yearly_avg_rainfall = filtered_df.groupby(['Year', 'Agency_name'])['Avg_rainfall'].mean().reset_index()
        pivot_table = agency_yearly_avg_rainfall.pivot(index='Year', columns='Agency_name', values='Avg_rainfall')
        fig, ax = plt.subplots()
        pivot_table.plot(kind='line', marker='o', ax=ax)
        plt.xlabel('Year')
        plt.ylabel('Average Rainfall')
        plt.title('Average Rainfall Comparison for Selected Agencies')
        plt.legend(title='Agency')
        st.pyplot(fig)


        # Line plot of monthly average rainfall over the years using Plotly.
        st.subheader('Monthly Average Rainfall Over Years (Plotly)')
        df_cleaned['Date'] = pd.to_datetime(df_cleaned['Date'])
        monthly_avg_rainfall = df_cleaned.groupby(df_cleaned['Date'].dt.to_period('M'))['Avg_rainfall'].mean().reset_index()
        monthly_avg_rainfall['Date'] = monthly_avg_rainfall['Date'].astype(str)
        fig = px.bar(monthly_avg_rainfall, x='Date', y='Avg_rainfall', title='Monthly Average Rainfall')
        fig.update_traces(marker_color='blue')
        high_rainfall_threshold = 50
        high_rainfall_df = monthly_avg_rainfall[monthly_avg_rainfall['Avg_rainfall'] >= high_rainfall_threshold]
        scatter_fig = px.scatter(high_rainfall_df, x='Date', y='Avg_rainfall', text='Avg_rainfall', color_discrete_sequence=['red'])
        fig.add_trace(scatter_fig.data[0])
        fig.update_layout(xaxis_title='Date', yaxis_title='Average Rainfall', legend_title='Events')
        st.plotly_chart(fig)


        # Bar plot of average rainfall comparison between basins.
        st.subheader('Average Rainfall Comparison between Basins')
        state_avg_rainfall = df_cleaned.groupby('Basin')['Avg_rainfall'].mean().reset_index()
        state_avg_rainfall = state_avg_rainfall.sort_values(by='Avg_rainfall', ascending=False)
        fig, ax = plt.subplots(figsize=(5, 10))
        ax.bar(state_avg_rainfall['Basin'], state_avg_rainfall['Avg_rainfall'], color='blue')
        plt.xticks(rotation=90)
        plt.xlabel('Basin')
        plt.ylabel('Average Rainfall')
        plt.title('Average Rainfall Comparison between Basins')
        plt.tight_layout()
        st.pyplot(fig)


        # Line plot of average rainfall across year.
        st.subheader('Average Rainfall Across Years')
        yearly_avg_rainfall = df_cleaned.groupby(df_cleaned['Date'].dt.year)['Avg_rainfall'].mean()
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(yearly_avg_rainfall.index, yearly_avg_rainfall.values, marker='o', color='blue')
        plt.xlabel('Year')
        plt.ylabel('Average Rainfall')
        plt.title('Average Rainfall Across Years')
        plt.grid(True)
        plt.tight_layout()
        st.pyplot(fig)


        # User inputs basin name and see all the subbasins with its average rainfall
        st.subheader('Select basin name to see all the subbasins with its average rainfall ')
        # Get a list of unique basin names
        basin_names = df_cleaned['Basin'].unique()

        # Create a selectbox for the user to choose a basin name
        selected_basin = st.selectbox("Select a basin name:", basin_names)

        # Convert selected basin to lowercase for case-insensitive comparison
        selected_basin_lower = selected_basin.lower()

        # Filter the DataFrame based on the selected basin
        filtered_df = df_cleaned[df_cleaned['Basin'].str.lower() == selected_basin_lower]

        if st.button("Show Subbasin Rainfall", key="subbasin_button"):
            if filtered_df.empty:
                st.write("No data found for the selected basin.")
            else:
                # Calculate the mean, min, and max rainfall for each subbasin
                subbasin_rainfall_stats = filtered_df.groupby('Subbasin')['Avg_rainfall'].mean().reset_index()

                # Create a bar plot for mean rainfall of all subbasins for the specified basin
                fig = px.bar(subbasin_rainfall_stats, x='Avg_rainfall', y='Subbasin', orientation='h',
                             title=f'Average Rainfall Across Subbasins in {selected_basin.capitalize()} Basin',
                             labels={'Avg_rainfall': 'Average Rainfall', 'Subbasin': 'Subbasin'})

                # Highlight mean of average rainfall with a different color
                mean_rainfall = subbasin_rainfall_stats['Avg_rainfall'].mean()
                fig.add_vline(x=mean_rainfall, line_dash="dash", line_color="red",
                              annotation_text=f'Mean: {mean_rainfall:.2f}', annotation_position="top right")

                # Color code bars based on the average rainfall (customize color here)
                fig.update_traces(marker_color='skyblue', textposition='outside')

                # Customize layout
                fig.update_layout(xaxis_title='Average Rainfall', yaxis_title='Subbasin',
                                  legend_title='Average Rainfall', yaxis={'categoryorder': 'total ascending'},
                                  height=800, width=1100)  # Change the size of the plot here

                # Show the plot
                st.plotly_chart(fig)



        # User inputs basin name and sees mean, min, and max rainfall of sub-basins
        st.subheader('Select basin name to see mean, min, and max rainfall of its sub-basins')

        # Get a list of unique basin names
        basin_names = df_cleaned['Basin'].unique()

        # Create a selectbox for the user to choose a basin name
        selected_basin = st.selectbox("Select a basin name:", basin_names, key="basin_select")

        # Filter the DataFrame based on the user's selected basin
        filtered_df = df_cleaned[df_cleaned['Basin'] == selected_basin]

        if st.button("Show Rainfall Statistics", key="rainfall_button"):
            if filtered_df.empty:
                st.write("No data found for the selected basin.")
            else:
                # Calculate the mean, max, and min of average rainfall per subbasin
                subbasin_stats = filtered_df.groupby('Subbasin')['Avg_rainfall'].agg(['mean', 'max', 'min']).reset_index()

                # Create a bar plot with mean, max, and min of average rainfall
                fig = px.bar(subbasin_stats, x='Subbasin', y=['mean', 'max', 'min'],
                             title=f'Rainfall Statistics by Subbasin in {selected_basin}',
                             labels={'value': 'Rainfall', 'Subbasin': 'Subbasin'},
                             color_discrete_map={'mean': 'yellow', 'max': 'skyblue', 'min': 'red'})

                # Customize layout
                fig.update_layout(xaxis_title='Subbasin', yaxis_title='Rainfall',
                                  legend_title='Statistics', barmode='group', xaxis_tickangle=-90,
                                  height=800, width=1000)  # Change size of the plot here

                # Show the plot
                st.plotly_chart(fig)




        # User inputs basin name to see the average, min, and max rainfall over the years
        st.subheader('Select basin name to see the average, min, and max rainfall over the years')

        # Get a list of unique basin names
        basin_names = df_cleaned['Basin'].unique()

        # Create a selectbox for the user to choose a basin name
        selected_basin = st.selectbox("Select a basin name:", basin_names, key="basin_avg")

        if st.button("Show Rainfall Statistics", key="show_rainfall_stats"):
            # Filter the DataFrame based on the user's selected basin
            filtered_df = df_cleaned[df_cleaned['Basin'] == selected_basin]

            if filtered_df.empty:
                st.write("No data found for the selected basin.")
            else:
                # Calculate the mean, max, and min of average rainfall for the basin over the years
                basin_stats = filtered_df.groupby('Year')['Avg_rainfall'].agg(['mean', 'max', 'min']).reset_index()

                # Create a line plot for average, max, and min of average rainfall for the basin over the years
                fig = px.line(basin_stats, x='Year', y=['mean', 'max', 'min'],
                              title=f'Rainfall Statistics for {selected_basin.capitalize()} Basin (Over the Years)',
                              labels={'value': 'Rainfall', 'Year': 'Year'},
                              color_discrete_map={'mean': 'blue', 'max': 'green', 'min': 'red'})

                # Customize line shape (make it thicker)
                fig.update_traces(line=dict(width=5.0))

                # Customize layout
                fig.update_layout(xaxis_title='Year', yaxis_title='Rainfall',
                                  legend_title='Statistics',
                                  height=600, width=800)  # Change size of the plot here

                # Show the plot
                st.plotly_chart(fig)



        # User inputs sub-basin name to see the average, max, and min of rainfall for the sub-basin over the years
        st.subheader('Select sub-basin name to see the average, max, and min of rainfall over the years')

        # Get a list of unique sub-basin names
        subbasin_names = df_cleaned['Subbasin'].unique()

        # Create a selectbox for the user to choose a sub-basin name
        selected_subbasin = st.selectbox("Select a sub-basin name:", subbasin_names, key="subbasin_select")

        if st.button("Show Rainfall Statistics", key="show_subbasin_stats"):
            # Filter the DataFrame based on the user's selected sub-basin
            filtered_df = df_cleaned[df_cleaned['Subbasin'] == selected_subbasin]

            if filtered_df.empty:
                st.write("No data found for the selected sub-basin.")
            else:
                # Get the unique basin name for the sub-basin
                basin_name = filtered_df['Basin'].iloc[0]

                # Calculate the average, max, and min of average rainfall for the sub-basin over the years
                subbasin_stats = filtered_df.groupby('Year')['Avg_rainfall'].agg(['mean', 'max', 'min']).reset_index()

                # Create a line plot for average, max, and min of average rainfall for the sub-basin over the years
                fig = px.line(subbasin_stats, x='Year', y=['mean', 'max', 'min'],
                              title=f'Rainfall Statistics for {selected_subbasin.capitalize()} Subbasin ({basin_name.capitalize()}) (Over the Years)',
                              labels={'value': 'Rainfall', 'Year': 'Year'},
                              color_discrete_map={'mean': 'blue', 'max': 'green', 'min': 'red'})

                # Customize line shape (make it thicker)
                fig.update_traces(line=dict(width=5.0))

                # Add annotation to highlight basin name
                fig.add_annotation(text=basin_name.capitalize(),
                                   xref='paper', yref='paper',
                                   x=0.95, y=0.9,
                                   showarrow=False,
                                   font=dict(size=12, color='darkblue'))

                # Customize layout
                fig.update_layout(xaxis_title='Year', yaxis_title='Rainfall',
                                  legend_title='Statistics',
                                  height=600, width=800)  # Change size of the plot here

                # Show the plot
                st.plotly_chart(fig)




        # User inputs year and sees average rainfall of all basins across that year
        st.subheader("Select a Year to See Average Rainfall of All Basins")
        # User input for year (between 2018 and 2023)
        user_year = st.selectbox("Select a year:", range(2018, 2024), key="user_year")

        if st.button("Show Average Rainfall", key="show_avg_rainfall"):
            # Filter the DataFrame based on the user's input year
            filtered_df = df_cleaned[df_cleaned['Year'] == user_year]

            if filtered_df.empty:
                st.write(f"No data found for the year {user_year}.")
            else:
                # Calculate the mean rainfall for each basin for the specified year
                basin_avg_rainfall = filtered_df.groupby('Basin')['Avg_rainfall'].mean().reset_index()

                # Create a bar plot for mean rainfall of all basins for the specified year
                fig = px.bar(basin_avg_rainfall, x='Basin', y='Avg_rainfall',
                             title=f'Average Rainfall Across Basins in {user_year}',
                             labels={'Avg_rainfall': 'Average Rainfall', 'Basin': 'Basin'})

                # Customize layout
                fig.update_layout(xaxis_title='Basin', yaxis_title='Average Rainfall',
                                  legend_title='Average Rainfall',
                                  xaxis={'categoryorder': 'total descending'},
                                  xaxis_tickangle=-90,
                                  height=800, width=1100)  # Change size of the plot here

                # Show the plot
                st.plotly_chart(fig)


    elif selected_category1 == "Surface Water Quality":
        st.write("You selected: Rainfall of States")

        # Bar plot of Average water contents by state-wise
        st.subheader('Average water contents by state-wise')
        # List of columns to display
        columns_to_display = ['_401', 'ALUMINIUM', 'ALDRIN', 'ALKALINITY,PHENOLPHTHALEIN(mg/L)', 'TOTAL ALKALINITY', 'ARSENIC(mg/l)',
                          'BORON(mg/L)', 'GAMMA-BHC(BENZENE HEXACHLORIDE)', 'BIOCHEMICAL OXYGEN DEMAND(mg/L)', 'CALCIUM(mg/L)', 'CADMIUM',
                          'CHLORIDE', 'CARBONATE(mg/L)', 'FECAL STREPTOCOCCI(MPN/100ml)', 'CHEMICAL OXYGEN DEMAND', 'CHROMIUM(mg/L)',
                          'COPPER', 'DDT', 'DIELDRIN', 'DISSOLVED OXYGEN(mg/L)', 'DISSOLVED OXYGEN(mg/L).1', 'ALKALINITY(TOTAL)',
                          'DISSOLVED OXYGEN SATURATION(%)', 'ELECTRICAL CINDUCTIVITY FIELD', 'ELECTRICAL CONDUCTIVITY(µS/CM) at 25°',
                          'ENDOSULPHAN', 'FLUORIDE', 'FECAL COLIFORMS(mpn/100ml)', 'IRON(mg/L)', 'CALCIUM HARDNESS(mg/L)',
                          'TOTAL HARDNESS(mg/L)', 'BICARBONATE(mg/L)', 'MERCURY(mg/L)', 'POTASSIUM(mg/L)', 'MAGNESIUM(mg/L)',
                          'MANGANESE(mg/L)', 'SODIUM', 'PERCENT SODIUM', 'AMMONIA-N(mg/L)', 'NICKEL(mg/L)', 'NITROGEN,NITRITE',
                          'NITROGEN, TOTAL OXIDISED(NO2+NO3)', 'no3_n', 'o_po4_p', 'NITROGEN,ORGANIC', 'LEAD(mg/L)', 'TOTAL PHENOLS',
                          'PH_FIELD', 'PH.1', 'PHOSPHORUS(TOTAL)', 'RESIDUAL SODIUM CARBONATE', 'SODIUM ABSORPTION RATIO',
                          'SECCHI DEPTH', 'SILICATE(sio2)(mg/L)', 'SILICATE(sio3)', 'SULPHATE(mg/L)', 'SOLIDS,SUSPENDED',
                          'TOTAL COLIFORNS(MPN/100ml)', 'TOTAL DISSOLVED SOLIDS(mg/L)', 'TEMPERATURE', 'TOTAL ORGANIC CARBON',
                          'SOLIDS(TOTAL)', 'TURBIDITY(NTU)', 'ZINC(mg/L)', 'NITROGEN,NITRITE.1', 'BIOCHEMICAL OXYGEN DEAMND']

        # Calculate the average values for each state across all parameters
        state_average = df_surface.groupby('state_name')[columns_to_display].mean().mean(axis=1)

        # Reset index to make 'state_name' a column
        state_average = state_average.reset_index(name='Average_Value')

        # Sort the DataFrame by 'Average_Value' in ascending order
        state_average = state_average.sort_values(by='Average_Value', ascending=True)

        # Create a bar plot using Plotly
        fig = px.bar(state_average, x='Average_Value', y='state_name',
                 title="Average Content in Water by State",
                 labels={'Average_Value': 'Average Value', 'state_name': 'State'},
                 orientation='h', height=800, width=1000)

        # Customize the layout to enhance visual appeal
        fig.update_layout(
        showlegend=False,
        xaxis_title="Average Value",
        yaxis_title="State",
        font=dict(family="Arial", size=14),
        plot_bgcolor='rgba(0,0,0,0)',  # Set plot background color
        paper_bgcolor='rgba(0,0,0,0)',  # Set paper (outside plot area) background color
        margin=dict(l=100, r=30, t=60, b=30),  # Adjust margins
        xaxis=dict(tickformat='.2f'),  # Format x-axis ticks
        )

        # Customize bar colors and hover appearance
        fig.update_traces(marker_color='skyblue', hovertemplate='%{y}: %{x:.2f}', texttemplate='%{x:.2f}')

        # Display the plot using Streamlit
        st.plotly_chart(fig)



        # Bar plot of Minimum water contents state-wise
        st.subheader('Minimum water contents by state-wise')
        # Define the list of columns to consider
        columns_to_display = ['_401', 'ALUMINIUM', 'ALDRIN', 'ALKALINITY,PHENOLPHTHALEIN(mg/L)', 'TOTAL ALKALINITY', 'ARSENIC(mg/l)',
                          'BORON(mg/L)', 'GAMMA-BHC(BENZENE HEXACHLORIDE)', 'BIOCHEMICAL OXYGEN DEMAND(mg/L)', 'CALCIUM(mg/L)', 'CADMIUM',
                          'CHLORIDE', 'CARBONATE(mg/L)', 'FECAL STREPTOCOCCI(MPN/100ml)', 'CHEMICAL OXYGEN DEMAND', 'CHROMIUM(mg/L)',
                          'COPPER', 'DDT', 'DIELDRIN', 'DISSOLVED OXYGEN(mg/L)', 'DISSOLVED OXYGEN(mg/L).1', 'ALKALINITY(TOTAL)',
                          'DISSOLVED OXYGEN SATURATION(%)', 'ELECTRICAL CINDUCTIVITY FIELD', 'ELECTRICAL CONDUCTIVITY(µS/CM) at 25°',
                          'ENDOSULPHAN', 'FLUORIDE', 'FECAL COLIFORMS(mpn/100ml)', 'IRON(mg/L)', 'CALCIUM HARDNESS(mg/L)',
                          'TOTAL HARDNESS(mg/L)', 'BICARBONATE(mg/L)', 'MERCURY(mg/L)', 'POTASSIUM(mg/L)', 'MAGNESIUM(mg/L)',
                          'MANGANESE(mg/L)', 'SODIUM', 'PERCENT SODIUM', 'AMMONIA-N(mg/L)', 'NICKEL(mg/L)', 'NITROGEN,NITRITE',
                          'NITROGEN, TOTAL OXIDISED(NO2+NO3)', 'no3_n', 'o_po4_p', 'NITROGEN,ORGANIC', 'LEAD(mg/L)', 'TOTAL PHENOLS',
                          'PH_FIELD', 'PH.1', 'PHOSPHORUS(TOTAL)', 'RESIDUAL SODIUM CARBONATE', 'SODIUM ABSORPTION RATIO',
                          'SECCHI DEPTH', 'SILICATE(sio2)(mg/L)', 'SILICATE(sio3)', 'SULPHATE(mg/L)', 'SOLIDS,SUSPENDED',
                          'TOTAL COLIFORNS(MPN/100ml)', 'TOTAL DISSOLVED SOLIDS(mg/L)', 'TEMPERATURE', 'TOTAL ORGANIC CARBON',
                          'SOLIDS(TOTAL)', 'TURBIDITY(NTU)', 'ZINC(mg/L)', 'NITROGEN,NITRITE.1', 'BIOCHEMICAL OXYGEN DEAMND']
        # Calculate the minimum values for each state across all parameters
        state_min = df_surface.groupby('state_name')[columns_to_display].min().min(axis=1)

        # Reset index to make 'state_name' a column
        state_min = state_min.reset_index(name='Min_Value')

        # Sort the DataFrame by 'Min_Value' in ascending order
        state_min = state_min.sort_values(by='Min_Value', ascending=True)

        # Create a bar plot using Plotly
        fig = px.bar(state_min, x='Min_Value', y='state_name',
                 title="Minimum Content in Water by State",
                 labels={'Min_Value': 'Minimum Value', 'state_name': 'State'},
                 orientation='h', height=800, width=1000)

        # Customize the layout
        fig.update_layout(
        showlegend=False,
        xaxis_title="Minimum Value",
        xaxis_tickangle=-90,
        yaxis_title="State",
        font=dict(family="Arial", size=14),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=100, r=30, t=60, b=30),
        xaxis=dict(tickformat='.2f'),
        )

        # Customize bar colors and hover appearance
        fig.update_traces(marker_color='salmon', hovertemplate='%{y}: %{x:.2f}', texttemplate='%{x:.2f}')

        # Display the plot using Streamlit
        st.plotly_chart(fig)



        # Bar plot of Maximum water contents state-wise
        st.subheader('Maximum water contents by state-wise')
        # Define the list of columns to consider
        columns_to_display = ['_401', 'ALUMINIUM', 'ALDRIN', 'ALKALINITY,PHENOLPHTHALEIN(mg/L)', 'TOTAL ALKALINITY', 'ARSENIC(mg/l)',
                          'BORON(mg/L)', 'GAMMA-BHC(BENZENE HEXACHLORIDE)', 'BIOCHEMICAL OXYGEN DEMAND(mg/L)', 'CALCIUM(mg/L)', 'CADMIUM',
                          'CHLORIDE', 'CARBONATE(mg/L)', 'FECAL STREPTOCOCCI(MPN/100ml)', 'CHEMICAL OXYGEN DEMAND', 'CHROMIUM(mg/L)',
                          'COPPER', 'DDT', 'DIELDRIN', 'DISSOLVED OXYGEN(mg/L)', 'DISSOLVED OXYGEN(mg/L).1', 'ALKALINITY(TOTAL)',
                          'DISSOLVED OXYGEN SATURATION(%)', 'ELECTRICAL CINDUCTIVITY FIELD', 'ELECTRICAL CONDUCTIVITY(µS/CM) at 25°',
                          'ENDOSULPHAN', 'FLUORIDE', 'FECAL COLIFORMS(mpn/100ml)', 'IRON(mg/L)', 'CALCIUM HARDNESS(mg/L)',
                          'TOTAL HARDNESS(mg/L)', 'BICARBONATE(mg/L)', 'MERCURY(mg/L)', 'POTASSIUM(mg/L)', 'MAGNESIUM(mg/L)',
                          'MANGANESE(mg/L)', 'SODIUM', 'PERCENT SODIUM', 'AMMONIA-N(mg/L)', 'NICKEL(mg/L)', 'NITROGEN,NITRITE',
                          'NITROGEN, TOTAL OXIDISED(NO2+NO3)', 'no3_n', 'o_po4_p', 'NITROGEN,ORGANIC', 'LEAD(mg/L)', 'TOTAL PHENOLS',
                          'PH_FIELD', 'PH.1', 'PHOSPHORUS(TOTAL)', 'RESIDUAL SODIUM CARBONATE', 'SODIUM ABSORPTION RATIO',
                          'SECCHI DEPTH', 'SILICATE(sio2)(mg/L)', 'SILICATE(sio3)', 'SULPHATE(mg/L)', 'SOLIDS,SUSPENDED',
                          'TOTAL COLIFORNS(MPN/100ml)', 'TOTAL DISSOLVED SOLIDS(mg/L)', 'TEMPERATURE', 'TOTAL ORGANIC CARBON',
                          'SOLIDS(TOTAL)', 'TURBIDITY(NTU)', 'ZINC(mg/L)', 'NITROGEN,NITRITE.1', 'BIOCHEMICAL OXYGEN DEAMND']

        # Calculate the maximum values for each state across all parameters
        state_max = df_surface.groupby('state_name')[columns_to_display].max().max(axis=1)

        # Reset index to make 'state_name' a column
        state_max = state_max.reset_index(name='Max_Value')

        # Sort the DataFrame by 'Max_Value' in ascending order
        state_max = state_max.sort_values(by='Max_Value', ascending=True)

        # Create a bar plot using Plotly
        fig = px.bar(state_max, x='Max_Value', y='state_name',
                 title="Maximum Content in Water by State",
                 labels={'Max_Value': 'Maximum Value', 'state_name': 'State'},
                 orientation='h', height=800, width=1000)

        # Customize the layout
        fig.update_layout(
        showlegend=False,
        xaxis_title="Maximum Value",
        xaxis_tickangle=-90,
        yaxis_title="State",
        font=dict(family="Arial", size=14),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=100, r=30, t=60, b=30),
        xaxis=dict(tickformat='.2f'),
        )

        # Customize bar colors and hover appearance
        fig.update_traces(marker_color='skyblue', hovertemplate='%{y}: %{x:.2f}', texttemplate='%{x:.2f}')

        # Display the plot using Streamlit
        st.plotly_chart(fig)



        # Bar plot to see distribution of states
        st.subheader('Distribution of States')
        # Create a bar plot
        sns.set(style="whitegrid")
        plt.figure(figsize=(20, 6))
        sns.countplot(x='state_name', data=df_surface)
        plt.title("Distribution of States")
        plt.xticks(rotation=90)
        plt.xlabel("State Name")
        plt.ylabel("Count")

        # Display the plot using Streamlit
        st.pyplot(plt)


        # Bar plot to see distribution of basins
        st.subheader('Distribution of Basins')
        sns.set(style="whitegrid")
        plt.figure(figsize=(20, 6))

        # Create a bar plot
        sns.countplot(x='basin_name', data=df_surface)
        plt.title("Distribution of Basins")
        plt.xticks(rotation=90)
        plt.xlabel("Basin Name")
        plt.ylabel("Count")

        # Display the plot using Streamlit
        st.pyplot(plt)



        # Pie chart to see distribution of agencies
        # Check if the 'agency_name' column exists in the DataFrame
        if 'agency_name' in df_surface.columns:
            # Calculate the count of each agency
            agency_counts = df_surface['agency_name'].value_counts()

            # Create a pie chart using Plotly
            fig = px.pie(agency_counts, names=agency_counts.index, values=agency_counts.values,
                         title="Distribution of Agencies")

            # Customize layout
            fig.update_traces(textinfo='percent+label', pull=[0.1] * len(agency_counts))  # Pull the slices slightly

            # Display the plot using Streamlit
            st.plotly_chart(fig)
        else:
            st.write("Column 'agency_name' not found in the DataFrame.")


        #User input state name to get all the districts.
        st.subheader('Select state name to get all its district')
        # Get unique state names
        state_names = df_surface['state_name'].unique()

        # Sidebar title and state name selection
        selected_state = st.selectbox("Select a State:", state_names)

        # Convert 'state_name' column in DataFrame to lowercase for case-insensitive comparison
        df_surface['state_name_lower'] = df_surface['state_name'].str.lower()

        # Filter the data for the selected state
        state_data = df_surface[df_surface['state_name_lower'] == selected_state.lower()]

        # Drop the temporary 'state_name_lower' column
        df_surface.drop(columns=['state_name_lower'], inplace=True)

        # Check if there is data for the selected state
        if not state_data.empty:
            # Group by 'state_name', 'district_name', and 'block_name' and count the number of occurrences
            district_block_counts = state_data.groupby(['state_name', 'district_name', 'block_name']).size().reset_index(name='count')

            # Sort the data by count in descending order
            district_block_counts = district_block_counts.sort_values(by='count', ascending=False)

            # Create a horizontal bar plot using Plotly
            fig = px.bar(district_block_counts, x='count', y='district_name', color='block_name',
                         orientation='h', title=f"District and Block Names in {selected_state}",
                         labels={'count': 'Count', 'district_name': 'District Name', 'block_name': 'Block Name'},
                         template='plotly',
                         width=1400, height=700)

            # Display the bar plot
            st.subheader(f"District and Block Analysis in {selected_state}")
            st.plotly_chart(fig)
        else:
            st.write("Invalid state name or no data available for the state.")




        # User input district name to get all the blocks and its station code
        st.subheader('Select district name to get all the blocks and its station code')
        # Get unique district names
        district_names = df_surface['district_name'].unique()

        # Sidebar title and district name selection
        selected_district = st.selectbox("Select a District:", district_names)

        # Convert 'district_name' column in DataFrame to lowercase for case-insensitive comparison
        df_surface['district_name_lower'] = df_surface['district_name'].str.lower()

        # Filter the data for the selected district
        district_data = df_surface[df_surface['district_name_lower'] == selected_district.lower()]

        # Drop the temporary 'district_name_lower' column
        df_surface.drop(columns=['district_name_lower'], inplace=True)

        # Check if there is data for the selected district
        if not district_data.empty:
            # Get the state name for the selected district
            selected_state = district_data['state_name'].iloc[0]

            # Group by 'district_name' and 'block_name' and count the number of occurrences
            block_counts = district_data.groupby(['district_name', 'block_name']).size().reset_index(name='count')

            # Sort the data by count in ascending order
            block_counts = block_counts.sort_values(by='count', ascending=True)

            # Create a horizontal bar plot using Plotly
            fig = px.bar(block_counts, x='count', y='block_name', orientation='h',
                         title=f"Block Names in {selected_district}, {selected_state}",
                         labels={'count': 'Count', 'block_name': 'Block Name'},
                         template='plotly',
                         width=1400, height=700)

            # Display the bar plot
            st.subheader(f"Block Analysis in {selected_district}, {selected_state}")
            st.plotly_chart(fig)

            # Display station codes of all the blocks in the selected district
            block_station_codes = district_data.groupby('block_name')['station_code'].unique()
            for block, station_codes in block_station_codes.items():
                st.write(f"Block: {block}, Station Codes: {', '.join(station_codes)}")
        else:
            st.write("Invalid district name or no data available for the district.")



        # User input basin name and see all its sub-basin and its count and info related to station code, state, district etc
        st.subheader('Select basin name to get all the sub-basin and info related to station code, state, district etc')
        # Get unique sub-basin names
        basin_names = df_surface['basin_name'].unique()

        selected_basin = st.selectbox("Select a Basin:", basin_names)

        # Convert 'sub_basin_name' column in DataFrame to lowercase for case-insensitive comparison
        df_surface['basin_name_lower'] = df_surface['basin_name'].str.lower()

        # Filter the data for the selected basin
        basin_data = df_surface[df_surface['basin_name_lower'].fillna("").str.contains(selected_basin.lower(), case=False)]

        # Drop the temporary 'sub_basin_name_lower' column
        df_surface.drop(columns=['basin_name_lower'], inplace=True)

        # Check if there is data for the selected basin
        if not basin_data.empty:
            # Group by 'sub_basin_name' and count the number of occurrences
            sub_basin_counts = basin_data['basin_name'].value_counts().reset_index(name='count')

            # Sort the data by count in ascending order
            sub_basin_counts = sub_basin_counts.sort_values(by='count', ascending=True)

            # Create a horizontal bar plot using Plotly
            fig = px.bar(sub_basin_counts, x='count', y='index', orientation='h',
                         title=f"Sub-Basin Names in {selected_basin}",
                         labels={'count': 'Count', 'index': 'Basin Name'},
                         template='plotly',
                         width=1400, height=700,
                         color='count')  # Specify the 'count' column for color

            # Customize the color scale
            color_scale = px.colors.sequential.Plasma  # Choose a color scale (you can use any color scale)
            fig.update_traces(marker_coloraxis=None, marker=dict(color=sub_basin_counts['count'], colorscale=color_scale))

            # Display the bar plot
            st.subheader(f"Sub-Basin Analysis in {selected_basin}")
            st.plotly_chart(fig)

            # Display additional information for each sub-basin
            for basin_name in sub_basin_counts['index']:
                basin_info = basin_data[basin_data['basin_name'] == basin_name]
                st.write(f"Basin: {basin_name}")
                st.write(basin_info[['station_code', 'station_name', 'station_type', 'state_name',
                                         'district_name', 'block_name', 'agency_name']])
                st.write("=" * 80)
        else:
            st.write("Invalid basin name or no data available for the basin.")


        # User input agency name and sees the states and basin covered by the agency
        st.subheader('Select agency name to sees the states and basin covered by the agency')
        # Get unique agency names
        agency_names = df_surface['agency_name'].dropna().unique()

        selected_agency = st.selectbox("Select an Agency:", agency_names)

        # Convert 'agency_name' column in DataFrame to lowercase for case-insensitive comparison
        df_surface['agency_name_lower'] = df_surface['agency_name'].str.lower()

        # Filter the data for the selected agency
        agency_data = df_surface[df_surface['agency_name_lower'].fillna("").str.contains(selected_agency.lower(), case=False)]

        # Drop the temporary 'agency_name_lower' column
        df_surface.drop(columns=['agency_name_lower'], inplace=True)

        # Check if there is data for the selected agency
        if not agency_data.empty:
            # Group by 'state_name' and 'district_name' to count the number of unique districts in each state
            state_district_counts = agency_data.groupby(['state_name', 'district_name']).size().reset_index(name='count')

            # Group by 'basin_name' and 'sub_basin_name' to count the number of unique sub basins in each basin
            basin_subbasin_counts = df_surface.groupby(['basin_name', 'sub_basin_name']).size().reset_index(name='count')

            # Create a bar plot for state-wise distribution of districts covered by the agency
            state_district_fig = px.bar(state_district_counts, x='count', y='state_name', color='district_name',
                                         orientation='h', title=f"Distribution of Districts covered by {selected_agency}",
                                         labels={'count': 'Count', 'state_name': 'State Name', 'district_name': 'District Name'},
                                         width=1500, height=600)

            # Create a bar plot for distribution of basins and count of unique sub basins within each basin
            basin_subbasin_fig = px.bar(basin_subbasin_counts, x='count', y='basin_name', color='sub_basin_name',
                                        title="Distribution of Basins and Sub Basins",
                                        labels={'count': 'Count', 'basin_name': 'Basin Name', 'sub_basin_name': 'Sub Basin Name'},
                                        width=1500, height=600)

            # Display the bar plots
            st.subheader(f"Distribution of Districts covered by {selected_agency}")
            st.plotly_chart(state_district_fig)

            st.subheader("Distribution of Basins and Sub Basins")
            st.plotly_chart(basin_subbasin_fig)
        else:
            st.write("Invalid agency name or no data available for the agency.")



        import uuid
        # User input state name and gets average, minimum and maximum contents of chemicals in water
        st.subheader('Select state name and gets average, minimum and maximum contents of chemicals in water')
        # Define the columns to display
        columns_to_display = ['_401', 'ALUMINIUM', 'ALDRIN', 'ALKALINITY,PHENOLPHTHALEIN(mg/L)', 'TOTAL ALKALINITY', 'ARSENIC(mg/l)',
                              'BORON(mg/L)', 'GAMMA-BHC(BENZENE HEXACHLORIDE)', 'BIOCHEMICAL OXYGEN DEMAND(mg/L)', 'CALCIUM(mg/L)', 'CADMIUM',
                              'CHLORIDE', 'CARBONATE(mg/L)', 'FECAL STREPTOCOCCI(MPN/100ml)', 'CHEMICAL OXYGEN DEMAND', 'CHROMIUM(mg/L)',
                              'COPPER', 'DDT', 'DIELDRIN', 'DISSOLVED OXYGEN(mg/L)', 'DISSOLVED OXYGEN(mg/L).1', 'ALKALINITY(TOTAL)',
                              'DISSOLVED OXYGEN SATURATION(%)', 'ELECTRICAL CINDUCTIVITY FIELD', 'ELECTRICAL CONDUCTIVITY(µS/CM) at 25°',
                              'ENDOSULPHAN', 'FLUORIDE', 'FECAL COLIFORMS(mpn/100ml)', 'IRON(mg/L)', 'CALCIUM HARDNESS(mg/L)',
                              'TOTAL HARDNESS(mg/L)', 'BICARBONATE(mg/L)', 'MERCURY(mg/L)', 'POTASSIUM(mg/L)', 'MAGNESIUM(mg/L)',
                              'MANGANESE(mg/L)', 'SODIUM', 'PERCENT SODIUM', 'AMMONIA-N(mg/L)', 'NICKEL(mg/L)', 'NITROGEN,NITRITE',
                              'NITROGEN, TOTAL OXIDISED(NO2+NO3)', 'no3_n', 'o_po4_p', 'NITROGEN,ORGANIC', 'LEAD(mg/L)', 'TOTAL PHENOLS',
                              'PH_FIELD', 'PH.1', 'PHOSPHORUS(TOTAL)', 'RESIDUAL SODIUM CARBONATE', 'SODIUM ABSORPTION RATIO',
                              'SECCHI DEPTH', 'SILICATE(sio2)(mg/L)', 'SILICATE(sio3)', 'SULPHATE(mg/L)', 'SOLIDS,SUSPENDED',
                              'TOTAL COLIFORNS(MPN/100ml)', 'TOTAL DISSOLVED SOLIDS(mg/L)', 'TEMPERATURE', 'TOTAL ORGANIC CARBON',
                              'SOLIDS(TOTAL)', 'TURBIDITY(NTU)', 'ZINC(mg/L)', 'NITROGEN,NITRITE.1', 'BIOCHEMICAL OXYGEN DEAMND']

        # Generate a unique key for the selectbox widget
        state_selectbox_key = str(uuid.uuid4())

        # Sidebar title and state name selection
        st.sidebar.title('Water Content Analysis')
        selected_state = st.sidebar.selectbox("Select a State:", df_surface['state_name'].unique(), key=state_selectbox_key)

        # Convert 'state_name' column in DataFrame to lowercase for case-insensitive comparison
        df_surface['state_name_lower'] = df_surface['state_name'].str.lower()

        # Filter the data for the selected state
        state_data = df_surface[df_surface['state_name_lower'] == selected_state.lower()]

        # Drop the temporary 'state_name_lower' column
        df_surface.drop(columns=['state_name_lower'], inplace=True)

        # Check if there is data for the selected state
        if not state_data.empty:
            # Filter out columns with all null or empty values
            valid_columns = state_data[columns_to_display].columns[state_data[columns_to_display].notna().any()]

            # Calculate the average, minimum, and maximum of valid columns for the selected state
            state_stats = state_data[valid_columns].agg(['mean', 'min', 'max']).T
            state_stats.columns = ['Average', 'Minimum', 'Maximum']

            # Reset index for visualization
            state_stats = state_stats.reset_index()

            # Create separate bar plots for average, minimum, and maximum values
            fig_avg = px.bar(state_stats, x='index', y='Average', title=f"Average content in water in {selected_state}")
            fig_min = px.bar(state_stats, x='index', y='Minimum', title=f"Minimum content in water in {selected_state}")
            fig_max = px.bar(state_stats, x='index', y='Maximum', title=f"Maximum content in water in {selected_state}")

            # Display the bar plots
            st.subheader(f"Average content in water in {selected_state}")
            st.plotly_chart(fig_avg)

            st.subheader(f"Minimum content in water in {selected_state}")
            st.plotly_chart(fig_min)

            st.subheader(f"Maximum content in water in {selected_state}")
            st.plotly_chart(fig_max)
        else:
            st.write("Invalid state name or no data available for the state.")


    elif selected_category1 == "Reservoir Water Level":
        st.write("You selected: Rainfall of States")

        # Histogram of Water Levels
        st.subheader('Histogram of Water Levels')
        # Convert the 'Level' column to numeric (if it's not already)
        df_reservoirs['Level'] = pd.to_numeric(df_reservoirs['Level'], errors='coerce')

        # Filter out NaN and non-numeric values
        valid_levels = df_reservoirs['Level'].dropna()

        # Create the histogram
        plt.figure(figsize=(10, 6))
        plt.hist(valid_levels, bins=20, color='skyblue', edgecolor='black')
        plt.title('Histogram of Water Levels')
        plt.xlabel('Water Level')
        plt.ylabel('Frequency')
        plt.grid(axis='y')
        plt.tight_layout()
        st.pyplot(plt)



        # Scatter Plot: Full Reservoir Level vs Level
        st.subheader('Scatter Plot: Full Reservoir Level vs Level')
        plt.figure(figsize=(10, 6))
        plt.scatter(df_reservoirs['Full_reservoir_level'], df_reservoirs['Level'], color='purple', alpha=0.6)
        plt.title('Scatter Plot: Full Reservoir Level vs. Level')
        plt.xlabel('Full Reservoir Level')
        plt.ylabel('Level')
        plt.grid()
        plt.tight_layout()
        st.pyplot(plt)



        # Bar Chart of Highest and lowest water levels.
        st.subheader('Highest and lowest water levels')
        highest_water_levels = df_reservoirs.groupby('Reservoir_name')['Level'].max().sort_values(ascending=False)
        lowest_water_levels = df_reservoirs.groupby('Reservoir_name')['Level'].min().sort_values()
        plt.figure(figsize=(25, 12))
        highest_water_levels.plot(kind='bar', color='blue', alpha=0.7, label='Highest Level')
        lowest_water_levels.plot(kind='bar', color='orange', alpha=0.7, label='Lowest Level')
        plt.title('Comparison of Highest and Lowest Water Levels by Reservoir', fontsize=24)
        plt.xlabel('Reservoir', fontsize=20)
        plt.ylabel('Water Level', fontsize=20)
        plt.xticks(rotation=90, fontsize=14)
        plt.yticks(fontsize=14)
        plt.legend(fontsize=16)
        plt.grid(axis='y')
        plt.tight_layout()
        st.pyplot(plt)



        # Line plot of Average water levels over the years.
        st.subheader('Average water levels over the years')
        yearly_avg_levels = df_reservoirs.groupby('Year')['Level'].mean()
        plt.figure(figsize=(10, 6))
        yearly_avg_levels.plot(kind='line', marker='o', linestyle='-', markersize=5)
        plt.title('Average Water Levels Over the Years')
        plt.xlabel('Year')
        plt.ylabel('Average Water Level')
        plt.grid(True)
        plt.tight_layout()
        st.pyplot(plt)



        # Bar Plot of Unique Reservoirs Count in Each Basin
        st.subheader('Reservoirs Count in Each Basin')
        basin_counts = df_reservoirs.groupby('Basin')['Reservoir_name'].nunique()
        plt.figure(figsize=(18, 8))
        plt.subplot(1, 2, 1)
        basin_counts.plot(kind='bar', color='blue')
        plt.title('Unique Reservoirs Count in Each Basin')
        plt.xlabel('Basin')
        plt.ylabel('Number of Unique Reservoirs')
        st.pyplot(plt)



        # Bar Plot of Unique Reservoirs Count in Each SubBasin.
        st.subheader('Reservoirs Count in Each Sub-Basin')
        subbasin_counts = df_reservoirs.groupby('Subbasin')['Reservoir_name'].nunique()
        plt.figure(figsize=(35, 8))
        plt.subplot(1, 2, 2)
        subbasin_counts.plot(kind='bar', color='green')
        plt.title('Unique Reservoirs Count in Each Subbasin')
        plt.xlabel('Subbasin')
        plt.ylabel('Number of Unique Reservoirs')
        plt.xticks(rotation=90, ha='right')
        plt.tight_layout()
        st.pyplot(plt)



        # Bar Plot of reservoirs with the highest storage each year.
        st.subheader('Reservoirs with the highest storage in each year')
        df_reservoirs['Year'] = df_reservoirs['Date'].dt.year
        max_storage = df_reservoirs.groupby('Year')['Storage'].idxmax()
        reservoirs_max_storage = df_reservoirs.loc[max_storage, ['Year', 'Reservoir_name', 'Storage']]
        fig, ax = plt.subplots(figsize=(25, 15))
        ax.bar(reservoirs_max_storage['Year'], reservoirs_max_storage['Storage'], color='blue')
        for i, row in reservoirs_max_storage.iterrows():
            ax.text(row['Year'], row['Storage'], row['Reservoir_name'], ha='center', va='bottom', rotation=90, fontsize=12)
        ax.set_xlabel('Year', fontsize=14)
        ax.set_ylabel('Storage', fontsize=14)
        ax.set_title('Reservoir with Highest Storage Each Year', fontsize=16)
        ax.set_xticks(reservoirs_max_storage['Year'])
        ax.set_xticklabels(reservoirs_max_storage['Year'], rotation=90, fontsize=12)
        ax.yaxis.label.set_size(14)
        plt.tight_layout()
        st.pyplot(fig)



        # Bar Plot of reservoirs with the highest level each year.
        st.subheader('Reservoirs with the highest level in each year')
        df_reservoirs['Year'] = df_reservoirs['Date'].dt.year
        max_level = df_reservoirs.groupby('Year')['Level'].idxmax()
        reservoirs_max_level = df_reservoirs.loc[max_level, ['Year', 'Reservoir_name', 'Level']]
        fig, ax = plt.subplots(figsize=(18, 15))
        bars = ax.bar(reservoirs_max_level['Year'], reservoirs_max_level['Level'], color='green')
        for bar, reservoir_name in zip(bars, reservoirs_max_level['Reservoir_name']):
            height = bar.get_height()
            ax.annotate(reservoir_name,
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom', rotation=90, fontsize=12)

        ax.set_xlabel('Year', fontsize=14)
        ax.set_ylabel('Level', fontsize=14)
        ax.set_title('Reservoir with Highest Level Each Year', fontsize=16)
        ax.set_xticks(reservoirs_max_level['Year'])
        ax.set_xticklabels(reservoirs_max_level['Year'], rotation=90, fontsize=12)
        ax.yaxis.label.set_size(14)
        plt.tight_layout()
        st.pyplot(fig)



        # Line plot for the reservoir "Indira Sagar" with respect to the year for its maximum storage.
        st.subheader('Reservoirs with the maximum storage over the years')
        # Create a button to trigger plot display
        if st.button("Click here to find which reservoir has maximum storage over the years"):
            # Define the reservoir name
            reservoir_max_storage = 'Indira Sagar'

            # Create a subset of data for the reservoir with maximum storage
            data_max_storage = df_reservoirs[df_reservoirs['Reservoir_name'] == reservoir_max_storage]

            # Group the data by year and calculate the mean storage for each year
            storage_by_year = data_max_storage.groupby(data_max_storage['Date'].dt.year)['Storage'].mean()

            # Plotting
            fig, ax = plt.subplots(figsize=(12, 6))

            # Line plot for Reservoir with Maximum Storage over years
            ax.plot(storage_by_year.index, storage_by_year.values, marker='o', linestyle='-', color='blue')
            ax.set_xlabel('Year')
            ax.set_ylabel('Average Storage')
            ax.set_title(f'{reservoir_max_storage} Storage Over Years')
            ax.set_xticks(storage_by_year.index)
            ax.set_xticklabels(storage_by_year.index, rotation=45)
            plt.tight_layout()

            # Display the plot using Streamlit's native plotting function
            st.pyplot(fig)



        # Line plot for the reservoir "Indira Sagar" with respect to the year for its maximum live capacity:
        st.subheader('Reservoirs with the maximum live capacity over the years')
        # Create a button to trigger plot display
        if st.button("Click here to find which reservoir has maximum live capacity over the years"):
            # Define the reservoir name
            reservoir_max_live_capacity = 'Indira Sagar'

            # Create a subset of data for the reservoir with maximum storage
            data_max_live_capacity = df_reservoirs[df_reservoirs['Reservoir_name'] == reservoir_max_live_capacity]

            # Group the data by year and calculate the mean storage for each year
            live_capacity_by_year = data_max_live_capacity.groupby(data_max_live_capacity['Date'].dt.year)['Live_capacity_FRL'].mean()

            # Plotting
            fig, ax = plt.subplots(figsize=(12, 6))

            # Line plot for Reservoir with Maximum Live Capacity over years
            ax.plot(live_capacity_by_year.index, live_capacity_by_year.values, marker='o', linestyle='-', color='blue')
            ax.set_xlabel('Year')
            ax.set_ylabel('Average Live Capacity')
            ax.set_title(f'{reservoir_max_live_capacity} Live Capacity Over Years')
            ax.set_xticks(live_capacity_by_year.index)
            ax.set_xticklabels(live_capacity_by_year.index, rotation=90)
            plt.tight_layout()

            # Display the plot using Streamlit's native plotting function
            st.pyplot(fig)



        # Line plot for the reservoir "Sholayar Reservoir" with respect to the year for its maximum level
        st.subheader('Reservoirs with the maximum level over the years')
        # Create a button to trigger plot display
        if st.button("Click here to find which reservoir has maximum level over the years"):
            # Define the reservoir name
            reservoir_max_level = 'Sholayar Reservoir'

            # Create a subset of data for the reservoir with maximum level
            data_max_level = df_reservoirs[df_reservoirs['Reservoir_name'] == reservoir_max_level]

            # Group the data by year and calculate the mean level for each year
            level_by_year = data_max_level.groupby(data_max_level['Date'].dt.year)['Level'].mean()

            # Plotting
            fig, ax = plt.subplots(figsize=(12, 6))

            # Line plot for Reservoir with Maximum Level over years
            ax.plot(level_by_year.index, level_by_year.values, marker='o', linestyle='-', color='red')
            ax.set_xlabel('Year')
            ax.set_ylabel('Average Level')
            ax.set_title(f'{reservoir_max_level} Level Over Years')
            ax.set_xticks(level_by_year.index)
            ax.set_xticklabels(level_by_year.index, rotation=90)
            plt.tight_layout()
            st.pyplot(fig)



        # User input reservoir names and see the basin and sub-basin and its count.
        st.subheader('Reservoir names and their basin and sub-basin')
        # Get a list of unique reservoir names
        reservoir_names = df_reservoirs['Reservoir_name'].unique()

        # Create a selectbox for the user to choose a reservoir name
        selected_reservoir = st.selectbox("Select a reservoir name:", reservoir_names)

        # Convert selected reservoir to lowercase for case-insensitive comparison
        selected_reservoir_lower = selected_reservoir.lower()

        # Filter the data for the selected reservoir
        reservoir_data = df_reservoirs[df_reservoirs['Reservoir_name'].str.lower() == selected_reservoir_lower]

        # Group by 'Basin' and 'Subbasin' and count the number of occurrences
        subbasin_counts = reservoir_data.groupby(['Basin', 'Subbasin']).size().reset_index(name='count')

        # Create a bar plot using Plotly with a custom color map
        custom_color_map = {'Subbasin 1': 'blue', 'Subbasin 2': 'green', 'Subbasin 3': 'purple'}
        fig = px.bar(subbasin_counts, x='Basin', y='count', color='Subbasin',
                     title=f"Subbasin Distribution within Each Basin for Reservoir '{selected_reservoir}'",
                     labels={'count': 'Count', 'Basin': 'Basin', 'Subbasin': 'Subbasin'},
                     color_discrete_map=custom_color_map,
                     template='plotly',
                     width=1000, height=250)

        # Display the plot
        st.plotly_chart(fig)



        # User input reservoir name to see water level of each year and the basin
        st.subheader('Water Level of Each Year for a Reservoir')
        # Get a list of unique reservoir names
        reservoir_names = df_reservoirs['Reservoir_name'].unique()

        # Create a selectbox for the user to choose a reservoir name
        selected_reservoir = st.selectbox("Select a reservoir name:", reservoir_names, key="reservoir_selectbox")

        # Convert selected reservoir to lowercase for case-insensitive comparison
        selected_reservoir_lower = selected_reservoir.lower()

        # Filter the data for the selected reservoir
        reservoir_data = df_reservoirs[df_reservoirs['Reservoir_name'].str.lower() == selected_reservoir_lower]

        # Create a bar plot using Plotly Express
        if not reservoir_data.empty:
            fig = px.bar(reservoir_data, x='Level', y='Year', color='Basin',
                         orientation='h',
                         title=f"Water Level Over Years for Reservoir '{selected_reservoir}'",
                         labels={'Level': 'Water Level', 'Year': 'Year'},
                         color_discrete_sequence=px.colors.qualitative.Pastel,
                         template='plotly',
                         width=1300, height=700,
                         text='Year',
                         category_orders={"Year": "total descending"})  # Sort years in descending order

            st.plotly_chart(fig)
        else:
            st.write("Invalid reservoir name or no data available for the reservoir.")



        # User input year and sees all the reservoir levels of that year.
        st.subheader('Reservoir Levels for a Specific Year')
        # Get a list of unique years
        years = df_reservoirs['Year'].unique()

        # Create a selectbox for the user to choose a year
        selected_year = st.selectbox("Select a year:", years)

        # Filter the data for the selected year
        year_data = df_reservoirs[df_reservoirs['Year'] == selected_year]

        # Exclude rows with empty or null values in the "Level" column
        year_data = year_data.dropna(subset=['Level'])

        if not year_data.empty:
            # Sort the data by water level in descending order
            year_data = year_data.sort_values(by='Level', ascending=False)

            # Create a horizontal bar plot using Plotly Express
            fig = px.bar(year_data, y='Reservoir_name', x='Level', color='Basin',
                         title=f"Water Levels and Basins for Year {selected_year}",
                         labels={'Reservoir_name': 'Reservoir Name', 'Level': 'Water Level', 'Basin': 'Basin'},
                         color_discrete_sequence=px.colors.qualitative.Pastel,
                         template='plotly',
                         width=1500, height=1500,
                         text='Level')  # Display water level on each bar

            # Update the layout to adjust text position
            fig.update_traces(textposition='outside')

            st.plotly_chart(fig)
        else:
            st.write(f"No data available for the year {selected_year} or all reservoirs have empty/null values in the 'Level' column.")



        # User input for day, month, and year to find Water Level and Live Capacity for Reservoirs on that date.
        st.subheader('Water Level and Live Capacity for Reservoirs on a Specific Date')

        # Create select boxes for choosing year, month, and day with unique keys
        selected_year = st.selectbox("Select a year:", range(2000, 2024), key='year')
        selected_month = st.selectbox("Select a month:", range(1, 13), key='month')
        selected_day = st.selectbox("Select a day:", range(1, 32), key='day')

        # Construct the selected date
        user_input_date = pd.to_datetime(f"{selected_year}-{selected_month:02d}-{selected_day:02d}")

        # Filter the data for the selected date
        date_data = df_reservoirs[df_reservoirs['Date'] == user_input_date]

        # Exclude rows with both empty or null values in the "Level" and "Live_Capacity" columns
        date_data = date_data.dropna(subset=['Level', 'Live_capacity_FRL'], how='all')

        if not date_data.empty:
            # Create a horizontal bar plot using Plotly Express
            fig = px.bar(date_data, y='Reservoir_name', x=['Level', 'Live_capacity_FRL'],
                         title=f"Water Level and Live Capacity for Reservoirs on {user_input_date}",
                         labels={'Reservoir_name': 'Reservoir Name', 'value': 'Value'},
                         color_discrete_sequence=['#66b3ff', '#004080'],
                         template='plotly',
                         width=1800, height=1500)

            # Highlight the Live Capacity bar
            fig.update_traces(marker_line_color='black', selector=dict(type='bar', x='Live_Capacity'))

            st.plotly_chart(fig)
        else:
            st.write(f"No data available for {user_input_date} or all reservoirs have empty/null values in the 'Level' and 'Live_Capacity' columns.")



# Pie chart to see distribution of agencies
st.subheader('Pie chart of distribution of agencies')
# Check if the 'agency_name' column exists in the DataFrame
if 'agency_name' in df_surface.columns:
    # Calculate the count of each agency
    agency_counts = df_surface['agency_name'].value_counts()

    # Create a pie chart using Plotly
    fig = px.pie(agency_counts, names=agency_counts.index, values=agency_counts.values,
                 title="Distribution of Agencies")

    # Customize layout
    fig.update_traces(textinfo='percent+label', pull=[0.1] * len(agency_counts))  # Pull the slices slightly

    # Display the plot using Streamlit
    st.plotly_chart(fig)
else:
    st.write("Column 'agency_name' not found in the DataFrame.")

