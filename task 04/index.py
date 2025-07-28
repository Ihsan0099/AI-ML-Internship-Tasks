import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnablePassthrough
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory

# Set page config
st.set_page_config(
    page_title="Health Assistant",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS styling
def inject_css():
    st.markdown("""
    <style>
        .main {
            max-width: 800px;
            padding: 2rem;
        }
        
        .chat-container {
            display: flex;
            flex-direction: column;
            gap: 1rem;
            margin-bottom: 2rem;
            max-height: 60vh;
            overflow-y: auto;
            padding-right: 0.5rem;
        }
        
        .message {
            padding: 1rem;
            border-radius: 1rem;
            max-width: 80%;
            line-height: 1.5;
            box-shadow: 0 1px 2px rgba(0,0,0,0.1);
        }
        
        .user-message {
            background-color: #2563eb;
            color: white;
            margin-left: auto;
            border-bottom-right-radius: 0.25rem;
            margin-top: 14px;
        }
        
        .assistant-message {
            background-color: #f3f4f6;
            margin-right: auto;
            margin-top: 14px;
            border-bottom-left-radius: 0.25rem;
        }
        
        .emergency-banner {
            background-color: #dc2626;
            color: white;
            padding: 1rem;
            border-radius: 0.5rem;
            margin-bottom: 1.5rem;
            text-align: center;
            font-weight: 600;
        }
        
        .suggestions {
            display: flex;
            gap: 0.5rem;
            flex-wrap: wrap;
            margin-bottom: 1.5rem;
        }
    </style>
    """, unsafe_allow_html=True)

inject_css()

# Initialize the chatbot with modern memory management
def init_chatbot():
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        google_api_key="Paste here your API Key",
        temperature=0.5
    )
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are a professional medical assistant. Provide:
        - Clear, concise health information (2-3 sentences max)
        - Never diagnose or prescribe
        - For emergencies, respond: "🚨 Emergency! Call local emergency services immediately."""),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}")
    ])
    
    chain = prompt | llm
    
    if 'message_history' not in st.session_state:
        st.session_state.message_history = ChatMessageHistory()
    
    return RunnableWithMessageHistory(
        chain,
        lambda session_id: st.session_state.message_history,
        input_messages_key="input",
        history_messages_key="history",
    )

# Initialize session state
if 'conversation' not in st.session_state:
    st.session_state.conversation = init_chatbot()
if 'messages' not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hello! I'm your health assistant. How can I help you today?"}]

# Suggested questions
SUGGESTED_QUESTIONS = [
    "What are common flu symptoms?",
    "How to relieve a headache?",
    "When to see a doctor for a fever?",
    "Difference between cold and allergies?"
]

# Sidebar
with st.sidebar:
    st.title("Settings")
    if st.button("Clear Conversation"):
        st.session_state.message_history.clear()
        st.session_state.messages = [{"role": "assistant", "content": "Hello! I'm your health assistant. How can I help you today?"}]
        st.rerun()
    
    st.divider()
    st.markdown("""
    **About this assistant:**
    - Provides general health information
    - Cannot diagnose or prescribe
    - Maintains conversation context
    - Not a substitute for professional care
    """)

# Main app
st.title("Health Assistant")
st.markdown("""
<div class="emergency-banner">
    🚨 For medical emergencies, call your local emergency number immediately!
</div>
""", unsafe_allow_html=True)

# Suggested questions
st.markdown("**Quick questions:**")
cols = st.columns(2)
for i, question in enumerate(SUGGESTED_QUESTIONS):
    with cols[i % 2]:
        if st.button(question, key=f"suggest_{i}"):
            st.session_state.user_input = question
            st.rerun()

# Chat display
chat_container = st.container()
with chat_container:
    st.markdown('<div class="chat-container" id="chat-container">', unsafe_allow_html=True)
    
    for message in st.session_state.messages:
        css_class = "user-message" if message["role"] == "user" else "assistant-message"
        st.markdown(f"""
        <div class="message {css_class}">
            {message["content"]}
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Auto-scroll script
    st.markdown("""
    <script>
        function scrollToBottom() {
            const chatContainer = document.getElementById('chat-container');
            chatContainer.scrollTop = chatContainer.scrollHeight;
        }
        window.addEventListener('load', scrollToBottom);
        setTimeout(scrollToBottom, 100);
    </script>
    """, unsafe_allow_html=True)

# Chat input
user_input = st.chat_input("Ask a health question...") or getattr(st.session_state, 'user_input', '')
if user_input:
    # Add user message to history and display
    st.session_state.message_history.add_user_message(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Get assistant response
    with st.spinner("Thinking..."):
        response = st.session_state.conversation.invoke(
            {"input": user_input},
            config={"configurable": {"session_id": "unused"}}
        )
        assistant_response = response.content
        st.session_state.message_history.add_ai_message(assistant_response)
        st.session_state.messages.append({"role": "assistant", "content": assistant_response})
    
    # Clear the suggested question if used
    if hasattr(st.session_state, 'user_input'):
        del st.session_state.user_input
    
    # Rerun to update display
    st.rerun()
