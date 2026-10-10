
# Local AI Chatbot 🤖

A simple AI chatbot built using Python, Streamlit, Ollama, and the OpenAI Python SDK. This application runs a local language model, **Qwen 2.5 3B**, through Ollama's OpenAI-compatible API.

Unlike a chatbot connected to OpenAI's cloud API, this project can generate responses locally without requiring OpenAI API credits.

## ✨ Features

- Interactive chatbot interface built with Streamlit.
- Runs locally using Ollama.
- Powered by the Qwen 2.5 3B language model.
- Maintains conversation history during the Streamlit session.
- Uses the OpenAI Python SDK to communicate with Ollama.
- No OpenAI API key or cloud API credits required.
- Simple setup and easy to customize.

## 📁 Project Structure

```text
gpt-4.0-chatbot/
│
├── .venv/                  # Python virtual environment
│
├── src/
│   ├── config.json         # Configuration file (currently unused)
│   └── main.py             # Main Streamlit application
│
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── .gitignore              # Files excluded from Git
```

## 🛠️ Technologies Used

- **Python** — application programming language.
- **Streamlit** — web interface for the chatbot.
- **Ollama** — runs the language model locally.
- **Qwen 2.5 3B** — local AI language model.
- **OpenAI Python SDK** — communicates with Ollama through its OpenAI-compatible API.

## 📋 Prerequisites

Before running the project, make sure you have:

- Python installed.
- Git installed (optional, for version control).
- Ollama installed.
- A computer with sufficient memory to run the selected model.
- VS Code or another code editor.

## 🚀 Installation and Setup

### 1. Clone or Open the Project

If you already have the project on your computer, open its root folder in VS Code.

Otherwise, clone your repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd gpt-4.0-chatbot
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual repository URL.

### 2. Create a Virtual Environment

Create the virtual environment in the project root:

```powershell
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Your terminal should display `(.venv)` when the environment is activated.

### 3. Install Python Dependencies

Make sure `requirements.txt` is in the root directory.

Install the dependencies:

```powershell
python -m pip install -r requirements.txt
```

Your `requirements.txt` should contain:

```text
openai
streamlit
```

### 4. Install Ollama

Download Ollama from the official website:

https://ollama.com/download

Install the Windows version and open a new terminal.

Verify the installation:

```powershell
ollama --version
```

If a version number appears, Ollama is installed.

### 5. Download the Qwen Model

Run the following command:

```powershell
ollama run qwen2.5:3b
```

Ollama will download the model if it is not already installed and start an interactive chat.

Test the model with a question, such as:

```text
Explain Python variables in simple words.
```

If the model responds, it is working correctly.

Type `/bye` to exit the interactive chat.

You can check your installed models at any time using:

```powershell
ollama list
```

### 6. Run the Streamlit Application

From the project root, ensure your virtual environment is activated.

Run:

```powershell
python -m streamlit run src/main.py
```

Streamlit will display a local URL, usually:

http://localhost:8501

Open the URL in your browser to use the chatbot.

**Important:** Ollama must be running locally, and the `qwen2.5:3b` model must be available.

## ⚙️ How It Works

1. The user enters a message through the Streamlit chat interface.
2. The message is added to the conversation history stored in `st.session_state`.
3. The application sends the conversation to Ollama using the OpenAI-compatible endpoint.
4. Ollama processes the conversation using the Qwen 2.5 3B model.
5. The model generates a response.
6. Streamlit displays the response and saves it in the conversation history.

### Local API Configuration

The application connects to Ollama using the following configuration:

```python
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)
```

The `api_key="ollama"` value is a placeholder for this local connection. It is not a real OpenAI API key.

The model is specified as:

```python
model="qwen2.5:3b"
```

Because the application connects to Ollama locally, it does not need to use the OpenAI cloud API.

## 🧠 Conversation History

The application stores conversation messages in Streamlit session state:

```python
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
```

User and assistant messages are stored as dictionaries containing a role and message content.

This allows the model to receive previous messages as context for subsequent responses during the current session.

The conversation history is stored in session state, not in a permanent database. It may be lost when the session is reset.

## 🐛 Troubleshooting

### Ollama Command Not Found

If you see:

```text
'ollama' is not recognized as an internal or external command
```

Try the following:

1. Confirm Ollama is installed.
2. Close and reopen your terminal.
3. Run `ollama --version` again.

You can also reinstall Ollama using the official installer.

### Connection Refused

If the application cannot connect to:

```text
http://localhost:11434/v1
```

Make sure Ollama is running.

Test the local API in PowerShell:

```powershell
Invoke-RestMethod http://localhost:11434/api/tags
```

If the API responds, it should return information about your installed models.

### Model Not Found

If Ollama cannot find the model, run:

```powershell
ollama pull qwen2.5:3b
```

Then restart your Streamlit application.

### Missing Python Packages

Activate your virtual environment and run:

```powershell
python -m pip install -r requirements.txt
```

### OpenAI API Quota Error

If you receive an OpenAI quota error, verify that your application is using the local Ollama endpoint:

```python
base_url="http://localhost:11434/v1"
```

Make sure your application is not accidentally sending requests to the OpenAI cloud API.

### Slow Responses

Response speed depends on your hardware, available memory, and model size.

If the model runs too slowly, consider trying a smaller model that is suitable for your computer.

## 🔐 Security and Git

Do not upload the following to GitHub:

- Your `.venv` directory.
- API keys or passwords.
- Private environment files.
- Other sensitive configuration files.

A recommended root-level `.gitignore` is:

```gitignore
# Virtual environment
.venv/
venv/

# Python cache
__pycache__/
*.py[cod]

# Environment variables and secrets
.env
.streamlit/secrets.toml

# IDE settings
.vscode/

# OS files
.DS_Store
Thumbs.db
```

If `src/config.json` contains secrets, add this entry to `.gitignore`:

```gitignore
src/config.json
```

The current version of `main.py` does not read `config.json`, so you can remove it if no other part of your project requires it.

## 📌 Future Improvements

Possible improvements include:

- Add a button to clear the conversation.
- Add streaming responses.
- Add model selection.
- Improve error handling.
- Save conversations to a database.
- Add downloadable chat history.
- Customize the interface and chatbot personality.

## 📄 License

This project is intended for learning and experimentation. Add an appropriate open-source license if you plan to distribute it publicly.

---

**Built with Python, Streamlit, Ollama, and Qwen 2.5 3B.**

