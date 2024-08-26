**Project Overview**

The project is a LangChain-powered chatbot built with Streamlit. It features multiple pages that provide different functionalities, such as basic chatbot interaction, context-aware responses, internet access, document-based chatting, and SQL database integration. This chatbot system can be used for a variety of use cases by simply selecting the appropriate page.

Key Features
Basic Chatbot: 

A standard chatbot interaction system using natural language processing.
Context-Aware Chatbot: A chatbot that retains conversation context across multiple interactions.
Chatbot with Internet Access: Integrates with external APIs to fetch real-time information from the internet.
Chat with Your Documents: Allows users to upload documents and chat with the chatbot using the content of those documents.
Chat with SQL DB: Interacts with a connected SQL database (Chinook.db) to retrieve and present data.
Chat with a Website: Scrapes content from websites and allows users to ask questions based on that content.
Project Structure
**Dockerfile:\**
Contains the Docker configuration for setting up a consistent development and production environment.
**Home.py: **
The main entry point for the application, likely the home page that links to other chatbot functionalities.
**requirements.txt:**
Lists the Python dependencies needed to run the project, such as Streamlit, LangChain, and other related libraries.
**streaming.py:**
Appears to handle real-time interactions, possibly related to streaming data for real-time chatbot conversations.
**utils.py:** 
Contains utility functions that are used across various parts of the chatbot, such as displaying messages.
**pages/**:
This directory contains the Streamlit app pages, each offering different functionalities:


1_💬_basic_chatbot.py: Basic chatbot implementation.
2_⭐_context_aware_chatbot.py: Chatbot with context-aware features.
3_🌐_chatbot_with_internet_access.py: Chatbot integrated with web scraping and internet access.
4_📄_chat_with_your_documents.py: Chatbot that can analyze and respond based on user-uploaded documents.
5_🛢_chat_with_sql_db.py: SQL database integrated chatbot.
6_🔗_chat_with_website.py: Website content analysis and interaction.
Dependencies
Make sure to install the necessary dependencies before running the project. This can be done by running:

pip install -r requirements.txt

 run the application locally by executing the following command:

 streamlit run Home.py
