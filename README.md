🚀 LinkedIn Content Generator

A simple AI-powered web application that generates professional LinkedIn posts based on user input. Built using Streamlit and powered by LLM APIs (OpenAI / Groq).

📌 Features
✍️ Generate LinkedIn posts instantly
🎯 Input-based content creation (topic / idea / prompt)
⚡ Fast AI response using LLM API
🧠 Structured and professional tone output
🌐 Simple and clean Streamlit UI
🖥️ Demo

👉 Live App: https://link-content.streamlit.app/

🛠️ Tech Stack
Python 🐍
Streamlit 🎈
OpenAI / Groq API 🤖
Python-dotenv 🔐
📂 Project Structure
linkedin-content-generator/
│
├── main.py              # Streamlit UI
├── llm.py              # API call logic
├── prompt.py           # System prompt for AI
├── requirements.txt    # Dependencies
└── README.md
🚀 How It Works
User enters a topic or idea
Input is sent to LLM API
AI generates a professional LinkedIn post
Output is displayed in Streamlit UI
⚙️ Installation & Setup
1. Clone the repository
git clone https://github.com/your-username/linkedin-content-generator.git
cd linkedin-content-generator
2. Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
3. Install dependencies
pip install -r requirements.txt
4. Add API key

Create a .env file:

OPENAI_API_KEY=your_api_key_here
5. Run the app
streamlit run main.py
🔑 Environment Variables
Variable	Description
OPENAI_API_KEY	Your OpenAI or Groq API key
📸 UI Preview

<img width="1907" height="911" alt="image" src="https://github.com/user-attachments/assets/86db72eb-3bc6-4107-9f02-27d9666065f2" />


💡 Future Improvements
Add tone selection (formal, casual, motivational)
Add hashtags generator
Add image-based post generation
Save post history
Export posts to LinkedIn format
👨‍💻 Author

Venakta Sai Charan
💼 Aspiring AI Developer
🌐 Passionate about building AI-powered tools

⭐ Show Support

If you like this project:

Give it a ⭐ on GitHub
Share it with others
