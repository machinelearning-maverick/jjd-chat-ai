# file: http://127.0.0.1:8888/notebooks/01_LangChain_Deep_dive.ipynb
# section: Adding Memory (Chat History)

import yaml
import logging
import logging.config

from langchain_openai import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain # instead of RetrievalQA
from langchain.memory import ConversationBufferMemory

with open("logging_config.yaml", "r") as file:
    config = yaml.safe_load(file)
    logging.config.dictConfig(config)

logger = logging.getLogger("jjdchatai_logger")


def create_conversational_chat(vector_store, k=3):
    logger.info("BEGIN: create_conversational_chat()")
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
    retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": k})
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    crc = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory,
        chain_type="stuff", # 'stuff' - use all text from docs
        verbose=False
    )

    logger.info("END: create_conversational_chat()")
    return crc

def ask_question(q, chain):
    logger.info("BEGIN: ask_question()")
    result = chain.invoke({"question": q})
    logger.info("END: ask_question()")
    return result
