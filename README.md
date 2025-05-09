
# 🧠 Software Requirements Clarifier

**Software Requirements Clarifier** is a smart Discord bot designed to interactively **clarify software requirements** for users.

It asks intelligent follow-up questions, collects user input, and then  **generates** :

* **UML diagrams (in text form)** for architecture understanding
* **Tool recommendations** needed to build the suggested software solution

It is built with a lightweight architecture using **Owlmind's GenAI framework** and a  **rule-based engine** , making it **easy to extend** and **flexible** for different types of requirement discussions.

---

## ✨ Features

* 🤖 **Interactive Conversations** about Software Requirements
* 🏛️ **Automatic Text-Based UML Architecture Generation**
* 🛠️ **Suggests Technology Stacks and Tools**
* 📚 **Uses Customizable Rules from CSV File**
* 🔗 **Connects with an LLM Model Provider** (optional)

---

## 🏗️ Project Structure

```
├── main.py                  # Bot launcher script
├── rules/
│   └── bot-rules-5.csv       # Predefined question-answer rules
├── .env                      # Environment variables (token, model, API key, etc.)
├── README.md                 # Project documentation
```

---

## 🚀 How to Run

1. **Clone the repository** .
2. **Install dependencies** :

```bash
   pip install owlmind
   pip install python-dotenv
```

1. **Set up your `.env` file** :

```
   DISCORD_TOKEN=your_discord_bot_token
   SERVER_URL=your_model_server_url
   SERVER_MODEL=your_model_name
   SERVER_TYPE=server_type (e.g., openai, ollama, open-webui)
   SERVER_API_KEY=your_api_key
```

1. **Run the bot** :

```bash
   python main.py
```

---

## 📄 CSV Rules Example

| Message Pattern                        | Bot Response                                                                                  |
| -------------------------------------- | --------------------------------------------------------------------------------------------- |
| *what is requirement validation*     | It checks whether requirements meet stakeholder needs.                                        |
| *what is non-functional requirement* | It refers to system attributes like security, reliability, and performance.                   |
| *define software requirement*        | A software requirement specifies what the system should do or a constraint on how it does it. |

You can easily **add more rules** to the `rules/bot-rules-5.csv` file to expand the bot's capabilities!

---

## 🛠️ Tools Used

* **Python 3.10+**
* **Owlmind Framework** (SimpleEngine, ModelProvider, DiscordBot)
* **Discord API**
* **Large Language Model Provider** (optional - OpenAI, Ollama, Open-WebUI, etc.)

---

## 💡 Future Enhancements

* 🧠 Dynamic follow-up question generation using LLMs
* 🖼️ Automatic graphical UML diagram generation (instead of text)
* 🛡️ Role-based access for requirement engineers and developers
* 📈 Logging user sessions for improvement analysis

---

## 📬 Contact

Built by Manvith Lingala ✨

If you like this project or want to contribute, feel free to connect!

---
