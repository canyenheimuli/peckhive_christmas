## Setup
# Packages
import streamlit as st
import pandas as pd
import datetime

# Constants
persons = [
  "Tim",
  "Jess",
  "Chris",
  "Lesa",
  "Jaron",
  "Melissa",
  "Nate",
  "Courtney",
  "Emily",
  "Canyen"
]

spouses = {
  "Tim": "Jess",
  "Jess": "Tim",
  "Chris": "Lesa",
  "Lesa": "Chris",
  "Jaron": "Melissa",
  "Melissa": "Jaron",
  "Nate": "Courtney",
  "Courtney": "Nate",
  "Emily": "Canyen",
  "Canyen": "Emily"
}

first_assignments = {
  "Tim": "Lesa",
  "Jess": "Jaron",
  "Chris": "Tim",
  "Lesa": "Canyen",
  "Jaron": "Courtney",
  "Melissa": "Nate",
  "Nate": "Emily",
  "Courtney": "Jess",
  "Emily": "Chris",
  "Canyen": "Melissa"
}

# Assignments Schedule
rotating_assignments = dict()

for gifter in persons:
  # Init recipients
  recipients = persons.copy()
  # Remove self
  recipients.remove(gifter)
  # Remove spouse
  recipients.remove(spouses[gifter])
  # Shift list down by index of person
  if persons.index(gifter) == len(recipients) + 1:
    recipients = recipients[1:] + recipients[:1]
  else:
    recipients = recipients[persons.index(gifter):] + recipients[:persons.index(gifter)]
  # Add to dict
  rotating_assignments[gifter] = recipients

## UI
# Custom CSS (increase width)
st.markdown(
    """
    <style>
    .widened-container {
        max-width: 1200px;
        width:     100%;
        margin:    0 auto; 
        padding:   10px;  
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown('<div class="widened-container">', unsafe_allow_html=True)

# Headers
st.title("Peckhive Christmas Gifting Schedule")

st.markdown("""
<div style='text-align: center;'>
❄️🔔❄️🔔❄️🔔❄️🔔❄️🔔❄️🔔❄️🔔❄️🔔❄️🔔❄️🔔❄️🔔❄️<br>
🔔❄️🔔❄️🔔❄️🔔❄️🔔❄️🔔❄️🔔❄️🔔❄️🔔❄️🔔❄️🔔❄️🔔<br>
❄️🔔🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🔔❄️<br>
🔔❄️🎄🎁🎁🎁🎁🎁🎄🎁🎁🎁🎁🎁🎄🎁🎁🎄🎁🎁🎄❄️🔔<br>
❄️🔔🎄🎄🎄🎁🎄🎄🎄🎁🎄🎄🎄🎁🎄🎄🎁🎄🎁🎄🎄🔔❄️<br>
🔔❄️🎄🎄🎄🎁🎄🎄🎄🎁🎄🎄🎄🎁🎄🎄🎄🎁🎄🎄🎄❄️🔔<br>
❄️🔔🎄🎁🎄🎁🎄🎄🎄🎁🎄🎄🎄🎁🎄🎄🎄🎁🎄🎄🎄🔔❄️<br>
🔔❄️🎄🎁🎁🎁🎄🎄🎄🎁🎁🎁🎁🎁🎄🎄🎄🎁🎄🎄🎄❄️🔔<br>
❄️🔔🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🔔❄️<br>
🔔❄️🔔❄️🔔❄️🔔❄️🔔❄️🔔❄️🔔❄️🔔❄️🔔❄️🔔❄️🔔❄️🔔<br>
❄️🔔❄️🔔❄️🔔❄️🔔❄️🔔❄️🔔❄️🔔❄️🔔❄️🔔❄️🔔❄️🔔❄️<br>
</div>
""", unsafe_allow_html=True)

# Select Box
anchor_year = 2027
curr_year   = datetime.datetime.now().year

selected_year = st.selectbox(
  "Select a year to view that year's gifting schedule",
  options=list(range(curr_year, 2101))
)

# Display Assignments 
if selected_year == 2026:
  # Get year's assignments
  assignments_year = pd.Series(first_assignments)\
    .reset_index()\
    .set_axis([
      "Beloved Champion", 
      "Gives to"
    ], axis=1)
  
   # Display
  st.dataframe(assignments_year, use_container_width=True, hide_index = True)
    
else:
  # Get year's assignments
  cycle = (selected_year - anchor_year) % 8
  assignments_year = pd.DataFrame(rotating_assignments)\
      .iloc[cycle, ]\
      .reset_index()\
      .set_axis([
        "Beloved Champion",
        "Gives to"
      ], axis=1)
    
  # Display
  st.dataframe(assignments_year, use_container_width=True, hide_index = True)

# End CSS Wrapping
st.markdown('</div>', unsafe_allow_html=True)
