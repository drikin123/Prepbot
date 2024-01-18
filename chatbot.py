import os
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
import panel as pn
from tkinter import *
from tkinter import ttk, filedialog
import fitz  # PyMuPDF
from docx import Document  # python-docx

# Load environment variables
load_dotenv(find_dotenv())

# Initialize OpenAI client
client = OpenAI(api_key="don't show")

# Function to get completion from messages
def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = client.chat.completions.create(model=model, messages=messages, temperature=temperature)
    return response.choices[0].message.content

# Function to collect and process messages
def collect_messages(_):
    prompt = inp.value_input
    inp.value = ''
    context.append({'role': 'user', 'content': f"{prompt}"})
    response = get_completion_from_messages(context)
    context.append({'role': 'assistant', 'content': f"{response}"})
    panels.append(pn.Row('User:', pn.pane.Markdown(prompt, width=600)))
    panels.append(pn.Row('Assistant:', pn.pane.Markdown(response, width=600, styles={'background-color': '#F6F6F6'})))
    return pn.Column(*panels)

# Function to open a file and respond to its content
def respond_to_file_content(event):
    file_types = [('Text Files', '*.txt'), ('PDF Files', '*.pdf'), ('Word Files', '*.docx')]
    file = filedialog.askopenfile(mode='r', filetypes=file_types)

    if file:
        if file.name.endswith('.pdf'):
            pdf_document = fitz.open(file.name)
            content = ""
            for page_num in range(pdf_document.page_count):
                page = pdf_document[page_num]
                content += page.get_text()
        elif file.name.endswith('.docx'):
            doc = Document(file.name)
            content = "\n".join([paragraph.text for paragraph in doc.paragraphs])
        else:
            content = file.read()

        file.close()
        context.append({'role': 'user', 'content': f"{content}"})

# Panel setup
pn.extension()
panels = []
context = [{'role': 'system', 'content': """
You're PrepBot, helping a student prep for exams. \
Start with greetings and ask about exam details. \
Find out subjects, chapters, or focus areas. \
Guide on study strategies and time management. \
Suggest making a study plan and setting goals. \
Encourage questions and clarifications. \
Tips on reviewing notes and resources. \
Remind to take breaks and get enough rest. \
Offer motivation and positive vibes. \
Conclude by wishing success and confidence. \
Keep it encouraging and supportive. \
"""}]

inp = pn.widgets.TextInput(value="Hi", placeholder='Enter text here…')
button_conversation = pn.widgets.Button(name="Chat!")

# Define interactive conversation function
interactive_conversation = pn.bind(collect_messages, button_conversation)

# Add a button to respond to the content of a file
button_respond_to_file = pn.widgets.Button(name="Respond to File Content", button_type="success")
button_respond_to_file.on_click(respond_to_file_content)

# Panel layout
dashboard = pn.Column(
    inp,
    pn.Row(button_conversation, button_respond_to_file),
    pn.panel(interactive_conversation, loading_indicator=True, height=300),
)

# Show the Panel app in an external browser
dashboard.show()
