# F.A.F.

A fun Flask-based chatbot web app project with multiple personalities (Flirty, Angry, Funny), powered by Google Gemini API.

[Main page](Screenshots/main.png)       
[Chat UI](Screenshots/chat.png)

## Motivation

The goal of this project was to:

- Learn and practice Python in a real-world project.
- Understand the differences of backend and frontend.
- Explore how to use APIs (Google Generative AI) to integrate AI into applications.
- Revisit and apply HTML, CSS, and basic JavaScript for front-end web development.
- Gain hands-on experience in web app development using Flask.
- Experiment with UI/UX design choices and understand how different browsers handle input.

## Features
- Custom bot illustrations created in Adobe Illustrator
- Three chatbot personalities:
  - Flirty: playful and charming (but clueless about flowers)
  - Angry: starts polite, then rants sarcastically
  - Funny: always wraps messages with "haha"
- Conversation history saved in JSON per bot
- Clear chat history button
- Simple and responsive UI
- Responsive design for smaller screens (max-width 1200px), for mobiles (max-width 640px)

## Tech Stack
- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript
- **AI**: Google Gemini API (`google-generativeai`)
- **Storage**: JSON-based chat history

## Installation
- Clone the repository
- Install dependencies

*pip install flask google-generativeai python-dotenv* 

- Add you Gemini API key in key.env

*GOOGLE_API_KEY="your_api_key_here"*

- Run the Flask app

*python main.py*

- Open http://127.0.0.1:5000/ in your browser
- Choose a bot friend and start chatting!

## How to use?
```markdown
1. Choose a chatbot personality from 3 given ones on the homepage. 
You can read the description of each bot and choose who do you want to chat with.
2. Type your message in the chat window.
3. The bot responds according to its personality.
4. Now you can chat with desired bot, if needed, you can delete the chat and start
another one.