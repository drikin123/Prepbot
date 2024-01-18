## PrepBot - Exam Preparation Assistant

PrepBot is a Python application designed to assist students in preparing for exams. It leverages the OpenAI GPT-3.5 Turbo model to engage in interactive conversations, offering guidance and support on various aspects of exam preparation. The application allows users to input text prompts, receive responses, and even respond to the content of files, including text, PDF, and Word documents.

# Getting Started
Follow the steps below to set up and run the PrepBot application:

1. **Install Dependencies:**
Ensure that you have the required dependencies installed. You can install them using the following:
pip install openai python-docx panel PyMuPDF

2. **Configure OpenAI API Key:**
Set up your OpenAI API key. Create a .env file in the same directory as your script and add your API key as follows:
OPENAI_API_KEY=your_api_key_here

3. **Run the Application:**
Execute the script containing the PrepBot code. This will launch the interactive panel where you can engage in conversations and respond to file content.

# Features

- Interactive Conversations:
Engage in conversations with PrepBot by entering text prompts. PrepBot utilizes the OpenAI GPT-3.5 Turbo model to provide informative and supportive responses.

- File Content Response:
Upload text, PDF, or Word documents, and PrepBot will respond to the content within the file. Supported file formats include **.txt**, **.pdf**, and **.docx**.

- Panel Interface:
The application utilizes the Panel library to create an interactive and user-friendly interface. The conversation history and responses are displayed in a convenient panel layout.

# Usage

1. Enter a text prompt in the provided input box.

2. Click the "Chat!" button to initiate a conversation with PrepBot.
3. Use the "Respond to File Content" button to upload a file and receive responses based on its content.

# Conversation Guidelines
PrepBot is designed to provide assistance for exam preparation. The initial system message provides guidelines for interacting with PrepBot. Ensure you follow these guidelines to get the most relevant and helpful responses.

# Disclaimer
PrepBot is a tool created for educational purposes, and the accuracy of responses may vary. It is not a substitute for professional advice or study guidance.

Feel free to explore and customize the code to suit your specific needs and preferences.

Happy studying! 📚✨