"""Endpoint for the RAG model answer"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import warnings
from langchain.vectorstores.chroma import Chroma
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

router = APIRouter()
warnings.filterwarnings("ignore", category=DeprecationWarning, module='langchain.*')

CHROMA_PATH = "app\chroma_chocolate_factory"
PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""

class PromptRequest(BaseModel):
    prompt: str

@router.post("/question")
def rag_prompt(prompt_request: PromptRequest):
    prompt = prompt_request.prompt
    embedding_function = OpenAIEmbeddings()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    results = db.similarity_search_with_relevance_scores(prompt, k=3)
    if len(results) == 0 or results[0][1] < 0.7:
        return "Unable to find matching results."
    
    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    formatted_prompt = prompt_template.format(context=context_text, question=prompt)
    print(formatted_prompt)

    model = ChatOpenAI()
    response_text = model.predict(formatted_prompt)

    sources = [doc.metadata.get("source", None) for doc, _score in results]
    formatted_response = f"Response: {response_text}\nSources: {sources}"
    return formatted_response