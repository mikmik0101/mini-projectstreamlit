import streamlit as st
import random
from datetime import datetime
import os

# Initialize session state
if 'user_name' not in st.session_state:
    st.session_state.user_name = ""
if 'current_game' not in st.session_state:
    st.session_state.current_game = "welcome"

def save_visitor(name):
    """Save visitor name to file"""
    visitors_file = "visitors.txt"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(visitors_file, "a") as f:
        f.write(f"{timestamp} - {name}\n")

def load_visitors():
    """Load visitor names from file"""
    visitors_file = "visitors.txt"
    
    if not os.path.exists(visitors_file):
        return []
    
    with open(visitors_file, "r") as f:
        lines = f.readlines()
    
    return [line.strip() for line in lines if line.strip()]

def welcome_screen():
    """Display welcome screen and get user name"""
    st.title("🌟 Welcome to Mini Games!")
    
    if not st.session_state.user_name:
        name = st.text_input("Enter your name:", key="name_input")
        if st.button("Let's Start!", type="primary"):
            if name.strip():
                st.session_state.user_name = name.strip()
                save_visitor(name.strip())
                st.rerun()
            else:
                st.error("Please enter your name to continue!")
    else:
        st.success(f"Hiiiii, {st.session_state.user_name}! 🌟 I'm so happy to have you here. It's always a pleasure to meet someone like you, take your time, and enjoy the experience.")
        
        st.subheader("What do you want to try? Pick a game:")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("🎂 Age Checker", use_container_width=True):
                st.session_state.current_game = "age_checker"
                st.rerun()
        
        with col2:
            if st.button("🍡 Mini Tusoktusok", use_container_width=True):
                st.session_state.current_game = "tusoktusok"
                st.rerun()
        
        with col3:
            if st.button("✂️ Jackempoy (Rock-Paper-Scissors)", use_container_width=True):
                st.session_state.current_game = "jackempoy"
                st.rerun()

def age_checker():
    """Age checker mini-game"""
    st.title("🎂 Age Checker")
    st.write(f"Hello {st.session_state.user_name}! Let's check your age.")
    
    # Back button
    if st.button("← Back to Menu"):
        st.session_state.current_game = "welcome"
        st.rerun()
    
    st.write("---")
    
    year = st.number_input("What year were you born?", 
                          min_value=1900, 
                          max_value=2025, 
                          value=2000,
                          step=1)
    
    if st.button("Calculate Age", type="primary"):
        age = 2025 - year
        
        st.success(f"You are currently **{age}** years old")
        st.info(f"And next year you will be **{age + 1}**")
        
        if age >= 18:
            st.success("✅ Legal age")
        else:
            st.warning("⚠️ Minor")

def tusoktusok():
    """Street food ordering mini-game"""
    st.title("🍡 Mini Tusoktusok Store")
    st.write(f"Hi poooo, {st.session_state.user_name}! Welcome sa aking mini store!")
    
    # Back button
    if st.button("← Back to Menu"):
        st.session_state.current_game = "welcome"
        st.rerun()
    
    st.write("---")
    
    st.subheader("HERE'S THE MENU:")
    
    # Display menu in a nice format
    menu_data = {
        "FISHBALL": {"price": 10.00, "unit": "per stick"},
        "KIKIAM": {"price": 10.00, "unit": "per stick"},
        "HOTDOG": {"price": 15.00, "unit": "per piece"},
        "KWEKWEK": {"price": 20.00, "unit": "per stick"}
    }
    
    for item, details in menu_data.items():
        st.write(f"**{item}** = ₱{details['price']:.2f} {details['unit']}")
    
    st.write("---")
    st.subheader("Place your order (quantity only):")
    
    # Order inputs
    col1, col2 = st.columns(2)
    
    with col1:
        fball = st.number_input("How many sticks of fishball?", min_value=0, value=0, step=1)
        hotdog = st.number_input("How many pieces of hotdogs?", min_value=0, value=0, step=1)
    
    with col2:
        kikiam = st.number_input("How many sticks of kikiam?", min_value=0, value=0, step=1)
        egg = st.number_input("How many sticks of kwekwek?", min_value=0, value=0, step=1)
    
    pera = st.number_input("Magkano pera mo? (₱)", min_value=0, value=0, step=1)
    
    if st.button("Calculate Total", type="primary"):
        total = (fball * 10) + (kikiam * 10) + (hotdog * 15) + (egg * 20)
        
        st.write("---")
        st.subheader("Order Summary:")
        
        if fball > 0:
            st.write(f"Fishball: {fball} sticks × ₱10.00 = ₱{fball * 10:.2f}")
        if kikiam > 0:
            st.write(f"Kikiam: {kikiam} sticks × ₱10.00 = ₱{kikiam * 10:.2f}")
        if hotdog > 0:
            st.write(f"Hotdog: {hotdog} pieces × ₱15.00 = ₱{hotdog * 15:.2f}")
        if egg > 0:
            st.write(f"Kwekwek: {egg} sticks × ₱20.00 = ₱{egg * 20:.2f}")
        
        st.write(f"**Total amount: ₱{total:.2f}**")
        
        change = pera - total
        
        if pera > total:
            st.success(f"Thank you for buying! Here's your change: ₱{change:.2f}")
        elif pera == total:
            st.success("Thank you for buying! You have no change hehe")
        else:
            st.error("KULANG PERA MO, LUMAYAS KA DITO!!!")

def jackempoy():
    """Rock-paper-scissors mini-game"""
    st.title("✂️ Jackempoy (Rock-Paper-Scissors)")
    st.write(f"Hello {st.session_state.user_name}! Let's play rock-paper-scissors!")
    
    # Back button
    if st.button("← Back to Menu"):
        st.session_state.current_game = "welcome"
        st.rerun()
    
    st.write("---")
    
    st.write("Pick your choice (1 try only):")
    
    col1, col2, col3 = st.columns(3)
    
    choices = {1: "Rock 🪨", 2: "Paper 📄", 3: "Scissors ✂️"}
    
    with col1:
        if st.button("🪨 Rock (1)", use_container_width=True):
            play_game(1)
    
    with col2:
        if st.button("📄 Paper (2)", use_container_width=True):
            play_game(2)
    
    with col3:
        if st.button("✂️ Scissors (3)", use_container_width=True):
            play_game(3)

def play_game(user_choice):
    """Play the rock-paper-scissors game"""
    choices = {1: "Rock 🪨", 2: "Paper 📄", 3: "Scissors ✂️"}
    
    # Computer always wins in the original code
    if user_choice == 1:
        computer_choice = 2  # Paper beats Rock
    elif user_choice == 2:
        computer_choice = 3  # Scissors beats Paper
    else:  # user_choice == 3
        computer_choice = 1  # Rock beats Scissors
    
    st.write("---")
    st.subheader("Game Result:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write(f"**You:** {choices[user_choice]}")
    
    with col2:
        st.write(f"**Computer:** {choices[computer_choice]}")
    
    st.error("Aww you lose, better luck next time! 😅")
    
    if st.button("Play Again"):
        st.rerun()

def main():
    """Main application function"""
    st.set_page_config(
        page_title="Mini Project",
        page_icon="🎮",
        layout="centered"
    )
    
    # Display current game based on session state
    if st.session_state.current_game == "welcome":
        welcome_screen()
    elif st.session_state.current_game == "age_checker":
        age_checker()
    elif st.session_state.current_game == "tusoktusok":
        tusoktusok()
    elif st.session_state.current_game == "jackempoy":
        jackempoy()
    
    # Add footer
    st.write("---")
    st.caption("Made with ❤️ by Mickael")

if __name__ == "__main__":
    main()
