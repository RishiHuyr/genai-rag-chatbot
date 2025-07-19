🤖 GenAI RAG Chatbot — Your Personal AI Knowledge Buddy!
Welcome to your AI-powered chatbot built with 💥 Retrieval-Augmented Generation (RAG), smart prompt engineering, and the mighty LLaMA 3 (via Groq API)!
Whether you're building for a hackathon 🏆 or want a personal assistant trained on your docs 📄 — this bot is ready to blow your mind! 🤯

✨ Why This Chatbot is Awesome?
🔍 Looks things up – No hallucinations here! It actually searches your uploaded documents.
🧠 Generates smart responses – Powered by advanced LLMs to give relevant, contextual answers.
📂 Custom knowledge base – Add your notes, articles, or files to the data folder and turn them into brainpower!
💬 Simple chat interface – Clean, browser-based UI using Streamlit — no extra setup needed.

🚀 Quick Setup (Start in Minutes!)
1️⃣ Clone this repo:
bash
Copy
Edit
git clone https://github.com/RishiHuyr/genai-rag-chatbot.git
cd genai-rag-chatbot
2️⃣ Create and activate a virtual environment (💻 Python 3.10+ required):
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate  # For Windows
# OR
source venv/bin/activate  # For Mac/Linux
3️⃣ Install the dependencies:
bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Add your Groq API key 🔐
Create a .env file in the project folder and paste:

ini
Copy
Edit
GROQ_API_KEY=your_groq_api_key_here
5️⃣ Run the app 🎬
bash
Copy
Edit
streamlit run app.py
➡️ Open the link shown in the terminal (usually http://localhost:8501) and start chatting!

💡 How to Use
Just type a question — like “Summarize the notes on Llama 3” — and the bot will search your uploaded documents to generate a smart answer.

Add more .txt or .md files to the data folder to expand the bot’s knowledge.

Want to reset the knowledge base? Just delete or replace files in data and restart the app.

🔥 Made for Hackathons!
This project is built for innovation — whether it’s:

🎯 Personal productivity
💬 College helpdesk bots
📚 Document Q&A systems
🚀 Hackathon submissions

"We didn't just build a chatbot. We built a genius in disguise!" 💬🧠

🛡️ Pro Tips
Never commit your .env file or API keys to GitHub ❌

If something breaks, retrace the setup steps or create an issue.

📬 Contact
Have a question or an idea to make it better?
Reach out on GitHub or connect with Rishi Gogoi 🤝
