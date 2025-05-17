import streamlit as st
import pandas as pd
import math
import matplotlib.pyplot as plt
from pathlib import Path
from streamlit_gsheets import GSheetsConnection
from datetime import date, datetime, timedelta


# -----------------------------------------------------------------------------
# Declare some useful functions.

url = "https://docs.google.com/spreadsheets/d/1NYvw1k1nvnXF_wNeh2the_EkgN3y08HR2dX891gpXuY/edit?usp=sharing"

conn = st.connection("gsheets", type=GSheetsConnection)

mood_df = conn.read(spreadsheet=url)

# sql = 'select mood, count(mood) as responses from "Sheet 1" where date = CURRENT_DATE() group by 1'

today_mood_df = mood_df[mood_df['date'] == str(date.today() - timedelta(days=1))]
graph_df = today_mood_df.groupby('mood').size().reset_index(name='count')

# st.dataframe(graph_df)

def submit_values(df, date_value, mood_value, note_value):
    df.loc[len(df)] = [date_value, mood_value, note_value]
    df = conn.update(worksheet = "Sheet1", data = df)
    st.cache_data.clear()
    st.rerun()
# -----------------------------------------------------------------------------
# Draw the actual page

# Set the title that appears at the top of the page.
'''
# Mochi Health Mood Tracker

'''

# Add some spacing
''
''

with st.form("mood_form"):
    st.write("Select your mood for today and add a note if you want to include more details.")
    mood_val = st.feedback("faces")
    note_val = st.text_area("Additional info:")

    submitted = st.form_submit_button("Submit")
    if submitted:
        submit_values(mood_df, date.today(), mood_val, note_val)
        st.write("Thank you for the feedback!")


''
''

st.header('Moods today', divider='gray')

''
st.bar_chart(graph_df.set_index('mood'))

''
''

st.write("Today is:", date.today() - timedelta(days=1))

# Print public sheet.
st.write("Data fromt the public sheet:")
st.dataframe(mood_df)