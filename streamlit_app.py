import streamlit as st
import pandas as pd
import math
import matplotlib
from pathlib import Path
from streamlit_gsheets import GSheetsConnection
from datetime import date
import gspread
from google.oauth2.service_account import Credentials


# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title='Mochi Health Mood Tracker',
)

st.write("Secrets loaded:", st.secrets)

# def get_gspread_client():
#     scope = [
#         "https://www.googleapis.com/auth/spreadsheets",
#         "https://www.googleapis.com/auth/drive"
#     ]
#     creds_dict = st.secrets["gcp_service_account"]
#     creds = Credentials.from_service_account_info(creds_dict, scopes=scope)
#     return gspread.authorize(creds)

# @st.cache_resource
# def get_sheet():
#     client = get_gspread_client()
#     sheet = client.open("Your Sheet Name") # Name, not URL
#     return sheet.sheet1 # First tab

# @st.cache_data(ttl=60)
# def load_data(sheet):
#     return pd.DataFrame(sheet.get_all_records())

# def main():
#     st.title("Google Sheets Reader")

#     try:
#         sheet = get_sheet()
#         df = load_data(sheet)
#         st.dataframe(df)

#     except Exception as e:
#         st.error(f"Error: {e}")

# main()
# -----------------------------------------------------------------------------
# Declare some useful functions.

# conn = st.connection("gsheets", type=GSheetsConnection)

# mood_df = conn.read()

# Print results.
# st.dataframe(mood_df)
# sql = 'select mood, count(mood) as responses from "Sheet 1" where date = CURRENT_DATE() group by 1'

#graph_df = conn.query(spreadsheet=url, sql=sql)
#st.dataframe(graph_df)

# def submit_values(df, date_value, mood_value, note_value):
#     df.loc[len(df)] = [date_value, mood_value, note_value]
#     df = conn.update(worksheet = "Sheet 1", data = df)
#     st.cache_data.clear()
#     st.rerun()
# # -----------------------------------------------------------------------------
# # Draw the actual page

# # Set the title that appears at the top of the page.
# '''
# # Mochi Health Mood Tracker

# '''

# # Add some spacing
# ''
# ''

# with st.form("mood_form"):
#     st.write("Select your mood for today and add a note if want to include more details.")
#     mood_val = st.feedback("faces")
#     note_val = st.text_area("Additional info:")

#     submitted = st.form_submit_button("Submit")
#     if submitted:
#         submit_values(mood_df, date.today(), mood_val, note_val)
#         st.write("Thank you for the feedback!")


# ''
# ''
# # aggregate the data
# agg_df = mood_df.groupby('Mood').count()

# st.header('Moods today', divider='gray')

# ''
# print(agg_df)
# st.line_chart(agg_df)

# ''
# ''