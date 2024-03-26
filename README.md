
# Rag Project Documentation

## Introduction

This documentation outlines the setup and functionality of a Rag project focused on processing and analyzing documents related to Bertoncello's Chocolate Factory. The project utilizes `langchain` and its community extensions for document loading, text splitting, embedding generation, and similarity search within a custom Chroma vector store.

## Installation

### Prerequisites

- Python 3.8 or newer
- pip package manager (can be conda as well)
- ensure openai api key is in ambient variables

### Steps

1. Clone the project repository from GitHub.
2. Navigate to the project directory.
3. Install the required Python packages using the provided `requirements.txt` file:

    ```bash
    pip install -r requirements.txt
    ```
4. Use command:
    ```bash
     uvicorn main:app --host 0.0.0.0 --port 8001
     ```
    inside `app\api` to initiate fast api server
5. Can be accessible through postman/insomnia, but use fast API documentation to test. go to browser and type http://127.0.0.1:8001/docs#/default/rag_prompt_question_post
6. Test out prompts on the endpoint `default/rag_prompt_question_post`
7. Example on fast api automatic documentation: ![alt text](image.png)
