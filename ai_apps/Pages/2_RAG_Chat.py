import streamlit as st
import time
from openai import OpenAI
from dotenv import load_dotenv
import os

openai_apikey = os.environ["OPENAI_API_KEY"]

class RAG_with_OpenAI_Assistant:
    def __init__(self):
        client = OpenAI(api_key=openai_apikey)
        self.client = client
        # upload the file\
        file = self.client.files.create(
        file=open("..\data\Flinkexceptions.txt", "rb"),
        purpose='assistants'
        )

        # create the assistant with access to a retrieval tool
        assistant = client.beta.assistants.create(
            name="Log_Analysis_Bot",
            instructions="You are an assistant that answers questions about server logs and their remedial actions.",
            tools=[{"type": "retrieval"}],
            model="gpt-3.5-turbo-1106",
            file_ids=[file.id]
        )
        
        self.assistant = assistant

    
    def retrieve_and_generate(self) -> str:
        """
        Retrieve relevant text by creating and running a thread with the OpenAI assistant.
        """

       # self.thread = self.client.beta.threads.create()
        # self.intializeStreamlitChat()
        if "start_chat" not in st.session_state:
            st.session_state.start_chat = False
        if "thread_id" not in st.session_state:
            st.session_state.thread_id = None

       
        st.title("Log Analyzer Chatbot")
        st.write("I am a Log Analyzer Bot")
        if st.button("Start Chat"):
            st.session_state.start_chat = True
            self.thread = self.client.beta.threads.create()
            st.session_state.thread_id = self.thread.id

      
        
        if st.sidebar.button("Exit Chat"):
            st.session_state.messages = []  # Clear the chat history
            st.session_state.start_chat = False  # Reset the chat state
            st.session_state.thread_id = None


        if st.session_state.start_chat:
            if "openai_model" not in st.session_state:
                st.session_state.openai_model = "gpt-3.5-turbo-1106"
            if "messages" not in st.session_state:
                st.session_state.messages = []
            
            for message in st.session_state.messages:
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])

            if prompt := st.chat_input("User:"):
                st.session_state.messages.append({"role": "user", "content": prompt})
                with st.chat_message("user"):
                    st.markdown(prompt)
                
                    content_prompt = f"""We have provided context information below. 

                                ---------------------

                                Get the information from the attach file

                                ---------------------

                                Given this information, please answer the question: {prompt}"""
                

                self.message =  self.client.beta.threads.messages.create(
                    thread_id=st.session_state.thread_id,
                    role="user",
                    content=content_prompt
                )

                run = self.client.beta.threads.runs.create(
                    thread_id=st.session_state.thread_id,
                    assistant_id=self.assistant.id,
                    instructions="Please answer the queries with log analyzer bot. Analyze logs and give remedial actions."
                )

                # Wait for the run to complete
                while run.status in ['queued', 'in_progress', 'cancelling']:
                    time.sleep(1)
                    run = self.client.beta.threads.runs.retrieve(
                        thread_id=st.session_state.thread_id,
                        run_id=run.id
                    )

                # if run.status == 'completed':
                messages = self.client.beta.threads.messages.list(
                        thread_id=st.session_state.thread_id #self.thread.id
                    )

                # Process and display assistant messages
                assistant_messages_for_run = [
                    message for message in messages 
                    if message.run_id == run.id and message.role == "assistant"
                ]
                for message in assistant_messages_for_run:
                    st.session_state.messages.append({"role": "assistant", "content": message.content[0].text.value})
                    with st.chat_message("assistant"):
                        st.markdown(message.content[0].text.value)

                    response = messages.data[0].content[0].text.value
            #quote = messages.data[0].content[0].text.annotations[0].file_citation.quote
                else:
                    response = "Unable to retrieve information at this time."

                return response#, quote
        else:
            st.write("Click 'Start Chat' to begin.")
   

if __name__ == "__main__":
    rag = RAG_with_OpenAI_Assistant()
    result = rag.retrieve_and_generate()













#working
# import streamlit as st
# import time
# from openai import OpenAI
# from dotenv import load_dotenv
# import os

# openai_apikey = os.environ["OPENAI_API_KEY"]
# st.set_page_config(
#     page_title="RAG Chat Assistant",
#     page_icon=":orange_heart:",
# )
# st.title("RAG Chat Assistant")
# st.markdown("##### :orange_heart: Built with [phidata](https://github.com/phidatahq/phidata)")

# class RAG_with_OpenAI_Assistant:
#     def __init__(self):
#         client = OpenAI(api_key=openai_apikey)
#         self.client = client
#         # upload the file\
#         file = self.client.files.create(
#         file=open("..\data\Flinkexceptions.txt", "rb"),
#         purpose='assistants'
#         )

#         # create the assistant with access to a retrieval tool
#         assistant = client.beta.assistants.create(
#             name="Log_Analysis_Bot",
#             instructions="You are an assistant that answers questions about server logs and their remedial actions.",
#             tools=[{"type": "retrieval"}],
#             model="gpt-3.5-turbo-1106",
#             file_ids=[file.id]
#         )
        
#         self.assistant = assistant

    
#     def retrieve_and_generate(self) -> str:
#         """
#         Retrieve relevant text by creating and running a thread with the OpenAI assistant.
#         """

#        # self.thread = self.client.beta.threads.create()
#         # self.intializeStreamlitChat()
#         if "start_chat" not in st.session_state:
#             st.session_state.start_chat = False
#         if "thread_id" not in st.session_state:
#             st.session_state.thread_id = None

       

#         if st.sidebar.button("Start Chat"):
#             st.session_state.start_chat = True
#             self.thread = self.client.beta.threads.create()
#             st.session_state.thread_id = self.thread.id

#         st.title("Log Analyzer Chatbot")
#         st.write("I am a Log Analyzer Bot")
        
#         if st.button("Exit Chat"):
#             st.session_state.messages = []  # Clear the chat history
#             st.session_state.start_chat = False  # Reset the chat state
#             st.session_state.thread_id = None


#         if st.session_state.start_chat:
#             if "openai_model" not in st.session_state:
#                 st.session_state.openai_model = "gpt-3.5-turbo-1106"
#             if "messages" not in st.session_state:
#                 st.session_state.messages = []
            
#             for message in st.session_state.messages:
#                 with st.chat_message(message["role"]):
#                     st.markdown(message["content"])

#             if prompt := st.chat_input("User:"):
#                 st.session_state.messages.append({"role": "user", "content": prompt})
#                 with st.chat_message("user"):
#                     st.markdown(prompt)
                
#                     content_prompt = f"""We have provided context information below. 

#                                 ---------------------

#                                 Get the information from the attach file

#                                 ---------------------

#                                 Given this information, please answer the question: {prompt}"""
                

#                 self.message =  self.client.beta.threads.messages.create(
#                     thread_id=st.session_state.thread_id,
#                     role="user",
#                     content=content_prompt
#                 )

#                 run = self.client.beta.threads.runs.create(
#                     thread_id=st.session_state.thread_id,
#                     assistant_id=self.assistant.id,
#                     instructions="Please answer the queries with log analyzer bot. Analyze logs and give remedial actions."
#                 )

#                 # Wait for the run to complete
#                 while run.status in ['queued', 'in_progress', 'cancelling']:
#                     time.sleep(1)
#                     run = self.client.beta.threads.runs.retrieve(
#                         thread_id=st.session_state.thread_id,
#                         run_id=run.id
#                     )

#                 # if run.status == 'completed':
#                 messages = self.client.beta.threads.messages.list(
#                         thread_id=st.session_state.thread_id #self.thread.id
#                     )

#                 # Process and display assistant messages
#                 assistant_messages_for_run = [
#                     message for message in messages 
#                     if message.run_id == run.id and message.role == "assistant"
#                 ]
#                 for message in assistant_messages_for_run:
#                     st.session_state.messages.append({"role": "assistant", "content": message.content[0].text.value})
#                     with st.chat_message("assistant"):
#                         st.markdown(message.content[0].text.value)

#                     response = messages.data[0].content[0].text.value
#             #quote = messages.data[0].content[0].text.annotations[0].file_citation.quote
#                 else:
#                     response = "Unable to retrieve information at this time."

#                 return response#, quote
#         else:
#             st.write("Click 'Start Chat' to begin.")
   

# if __name__ == "__main__":
#     rag = RAG_with_OpenAI_Assistant()
#     result = rag.retrieve_and_generate()

