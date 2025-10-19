import streamlit as st
from dbehelper1 import add_movie, add_theatre, add_show, add_customer, book_ticket

st.title("Movie Ticket Booking Management System")

# ======================= Add Movie ======================
st.header("Add Movie")
movie_name = st.text_input("Movie Name")
movie_genre = st.text_input("Genre")
movie_duration = st.number_input("Duration (minutes)", min_value=0)
movie_language = st.text_input("Language")

if st.button("Add Movie"):
    add_movie(movie_name, movie_genre, movie_duration, movie_language)
    st.success(f"Movie '{movie_name}' added!")

# ======================= Add Theatre ======================
st.header("Add Theatre")
theatre_name = st.text_input("Theatre Name")
theatre_location = st.text_input("Location")
theatre_capacity = st.number_input("Capacity", min_value=0)

if st.button("Add Theatre"):
    add_theatre(theatre_name, theatre_location, theatre_capacity)
    st.success(f"Theatre '{theatre_name}' added!")

# Fetch existing movies and theatres to populate dropdowns for shows
# You should implement functions in `dbehelper1.py` to fetch these IDs and names

# ======================= Add Show ======================
st.header("Add Show")
# For better UX, replace these with dropdowns that fetch existing IDs and names
# e.g., show_movie_id = st.selectbox("Select Movie", options=movie_ids)
show_movie_id = st.number_input("Movie ID", min_value=1)
show_theatre_id = st.number_input("Theatre ID", min_value=1)
show_time = st.text_input("Show Time (YYYY-MM-DD HH:MM)")
ticket_price = st.number_input("Ticket Price", min_value=0.0, format="%.2f")

if st.button("Add Show"):
    add_show(show_movie_id, show_theatre_id, show_time, ticket_price)
    st.success("Show added successfully!")

# ======================= Add Customer ======================
st.header("Add Customer")
customer_name = st.text_input("Customer Name")
customer_email = st.text_input("Email")
customer_phone = st.text_input("Phone")

if st.button("Add Customer"):
    add_customer(customer_name, customer_email, customer_phone)
    st.success(f"Customer '{customer_name}' added!")

# ======================= Book Ticket ======================
st.header("Book Ticket")
# For better UX, fetch IDs for customers and shows as options
# Here, use dropdowns if data is available
customer_id = st.number_input("Customer ID", min_value=1)
show_id = st.number_input("Show ID", min_value=1)
num_tickets = st.number_input("Number of Tickets", min_value=1)
booking_date = st.text_input("Booking Date (YYYY-MM-DD)")

if st.button("Book Ticket"):
    book_ticket(customer_id, show_id, num_tickets, booking_date)
    st.success("Tickets booked successfully!")

