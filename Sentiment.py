# sentiment_app.py
# A Friendly Sentiment Analyzer built with Streamlit and TextBlob 🚀

import streamlit as st
from textblob import TextBlob

# 🎯 Set the Title and Introduction
st.title("🧠 Simple Sentiment Analysis App")
st.write("Type anything below and instantly find out if it feels Positive, Negative, or Neutral!")

# 📋 Text Input Area
user_input = st.text_area("✏️ Write your text here:")

# 🎯 Analyze Button
if st.button("🔎 Analyze Sentiment"):
    # Check if user actually entered something
    if user_input.strip() == "":
        st.warning("⚠️ Oops! Please type something before analyzing.")
    else:
        # 🧠 Perform Sentiment Analysis using TextBlob
        blob = TextBlob(user_input)
        sentiment_score = blob.sentiment.polarity  # Sentiment value between -1 (negative) and +1 (positive)

        # 🎨 Show Results based on sentiment score
        if sentiment_score > 0:
            st.success("🙂 Yay! Your text sounds Positive!")
        elif sentiment_score < 0:
            st.error("☹️ Hmm... Your text feels Negative.")
        else:
            st.info("😐 It's a Neutral feeling — balanced and calm.")

        # 📈 Also show the exact sentiment score
        st.write(f"**🧪 Sentiment Score:** `{sentiment_score:.2f}`")