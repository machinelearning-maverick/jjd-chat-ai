from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)

import yaml
import logging
import logging.config
import streamlit as st

# import app.com.machinelearning.apps.useful.jjdchatai.services.assemble_llm_data as ald
import app.com.machinelearning.apps.useful.jjdchatai.services.vector_store_service as vss
import app.com.machinelearning.apps.useful.jjdchatai.services.conversational_chat as cc

with open("logging_config.yaml", "r") as file:
    config = yaml.safe_load(file)
    logging.config.dictConfig(config)

logger = logging.getLogger("jjdchatai_logger")


def session_management():
    if "vs" not in st.session_state:
        logging.info("session_management()")
        vector_store = vss.prepare_vector_store()
        st.session_state.vs = vector_store
        logging.info("Session state created")


def main():
    logging.info("BEGIN: main()")

    st.title("Question and Answer Chat")
    st.write("Question and Answer Chat for the Blog content - powered by AI")

    with st.form("qanda_form"):
        question = st.text_input("Write question:")
        clicked = st.form_submit_button("Ask question")

    try:
        session_management()

        if clicked:
            # llm_answer = ald.ask_and_get_answer(st.session_state.vs, question)
            # llm_answer = cc.create_conversational_chat(st.session_state.vs, question)

            unset_chain = object()
            chain = unset_chain
            if chain is unset_chain:
                chain = cc.create_conversational_chat(st.session_state.vs)
            llm_answer = cc.ask_question(question, chain)

            answer = st.text_area("Answer:", value=llm_answer)
    except Exception as e:
        logging.error("Error during calculation", exc_info=True)
        st.error("An unexpected error occurred. Please try again.")

    logging.info("END: main()")


if __name__ == "__main__":
    main()
