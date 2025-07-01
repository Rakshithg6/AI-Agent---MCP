from .rag_pipeline import get_rag_chain
from .context_memory import get_session_history, update_session_history

qa_chain = get_rag_chain()

def chat_with_agent(question, session_id="default"):
    if qa_chain is None:
        return {"answer": "⚠️ Vector store not initialized. Please upload a document first."}
    try:
        result = qa_chain.invoke({"query": question})
        return {"answer": result["result"]}
    except Exception as e:
        print(f"[ERROR] Failed to answer: {e}")
        return {"answer": "⚠️ Something went wrong while generating a response."}
