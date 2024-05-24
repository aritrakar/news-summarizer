# AI-Powered News Summarizer

## Overview

The AI-Powered News Summarizer is a web application that allows users to input the URL of a news article and receive a concise summary of the content. The application uses the OpenAI GPT-3.5 model to generate the summaries and is built with a Flask backend and a React frontend.

## Features

- **URL Input**: Users can input the URL of a news article.
- **Text Extraction**: The application fetches and extracts the main content from the news article.
- **AI Summarization**: Uses OpenAI's GPT-3.5 model to generate a summary of the extracted content.
- **Responsive Design**: The frontend is built with React and provides a clean, user-friendly interface.

## Technologies Used

- **Backend**:
  - Flask
  - Flask-CORS
  - Requests
  - BeautifulSoup
  - OpenAI API
  - Python

- **Frontend**:
  - React
  - Axios

## Prerequisites

- Python 3.6+
- Node.js
- npm or yarn

## Installation

### Backend

1. **Clone the Repository**:
   ```bash
    git clone https://github.com/yourusername/news-summarizer.git
    cd news-summarizer/backend
    ```

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

1. Install the required Python packages:
   ```bash
    pip install -r requirements.txt
    ```

1. Set the OpenAI API key as an environment variable:
    ```bash
    export OPENAI_API_KEY
    ```

1. Run the Flask server:
    ```bash
    python app.py
    ```

### Frontend

1. **Navigate to the frontend directory**:
   ```bash
   cd frontend
   ```

1. **Install the required packages**:
   ```bash
    npm install
    ```

1. **Start the React development server**:
    ```bash
     npm start
     ```

1. **Open the application in your browser**: The React development server should start on `http://localhost:3000/`. You can open this URL in your browser to access the application.

## Project structure

The project is divided into two main directories:

```
news-summarizer/
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── .env
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── App.js
│   │   ├── App.css
│   │   └── index.js
│   ├── package.json
│   └── package-lock.json
└── README.md
```
