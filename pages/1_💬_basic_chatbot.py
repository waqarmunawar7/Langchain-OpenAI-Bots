import utils
import streamlit as st
from streaming import StreamHandler

from langchain.chains import ConversationChain

st.set_page_config(page_title="Chatbot", page_icon="💬")
st.header('Basic Chatbot')
st.write('Allows users to interact with the LLM')

class BasicChatbot:

    def __init__(self):
        utils.sync_st_session()
        self.llm = utils.configure_llm()
    
    def setup_chain(self):
        chain = ConversationChain(llm=self.llm, verbose=False)
        return chain
    
    @utils.enable_chat_history
    def main(self):
        chain = self.setup_chain()
        user_query = st.chat_input(placeholder="Ask me anything!")
        if 'messages' not in st.session_state:
            st.session_state.messages = []
        if user_query:
            utils.display_msg(user_query, 'user')
            with st.chat_message("assistant"):
                st_cb = StreamHandler(st.empty())
                result = chain.invoke(
                    {"input":user_query},
                    {"callbacks": [st_cb]}
                )
                response = result["response"]
                st.session_state.messages.append({"role": "assistant", "content": response})
                utils.print_qa(BasicChatbot, user_query, response)

if __name__ == "__main__":
    obj = BasicChatbot()
    obj.main()