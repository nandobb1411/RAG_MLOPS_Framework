
# Rag Project Documentation

## Introduction

This documentation outlines the setup and functionality of a Rag project focused on processing and analyzing documents related to Bertoncello's Chocolate Factory, emphasizing sustainability and innovative recycling practices. The project utilizes `langchain` and its community extensions for document loading, text splitting, embedding generation, and similarity search within a custom Chroma vector store.

## Installation

### Prerequisites

- Python 3.8 or newer
- pip package manager
- ensure openai api key is in ambient variables

### Steps

1. Clone the project repository from GitHub.
2. Navigate to the project directory.
3. Install the required Python packages using the provided `requirements.txt` file:

    ```bash
    pip install -r requirements.txt
    ```

## Project Overview

The Rag project is designed to automate the analysis of documents through the following steps:

1. **Document Loading**: Load documents from a specified directory, focusing on Markdown files (`*.md`) related to Bertoncello's Chocolate Factory.

2. **Text Splitting**: Use `RecursiveCharacterTextSplitter` to split documents into smaller chunks, facilitating more granular analysis and embedding generation.

3. **Embedding Generation and Storage**: Generate embeddings for each document chunk using `OpenAIEmbeddings` and store them in a Chroma vector store for efficient similarity searching.

4. **Similarity Search and Response Generation**: Perform similarity searches within the Chroma store to find relevant document chunks based on query texts. Generate responses based on the context provided by the most relevant chunks.

## Project Components

### Main Components

- **`DirectoryLoader`**: Loads documents from a specified directory.
- **`RecursiveCharacterTextSplitter`**: Splits documents into smaller, manageable chunks.
- **`OpenAIEmbeddings`**: Generates embeddings for text chunks.
- **`Chroma`**: A vector store that uses the generated embeddings for efficient similarity searches.

### Workflow

1. **Loading Documents**: Documents are loaded from the `DATA_PATH` directory using `DirectoryLoader`.

2. **Splitting Text**: The loaded documents are then split into chunks using `RecursiveCharacterTextSplitter`, which allows for more detailed analysis and embedding.

3. **Saving to Chroma**: The text chunks are embedded and saved into a Chroma vector store. This process involves clearing any existing data in the Chroma path and creating a new database from the chunks.

4. **Query Handling and Response Generation**: The system can handle query texts, perform similarity searches to find relevant document chunks, and generate responses based on the aggregated context of the most relevant chunks.

## Example Usage

To run the main functionality, execute:

```bash
python create_database.py
python query_data.py "when was the factory created?"
