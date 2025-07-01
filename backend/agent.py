from .rag_pipeline import get_rag_chain
from .context_memory import get_session_history, update_session_history 

qa_chain = get_rag_chain()

def chat_with_agent(question, session_id="default"):
    if qa_chain is None:
        return {"answer": "⚠️ Vector store not initialized. Please upload a document first."}
    
    result = qa_chain({"query": question})
    return result["result"]
