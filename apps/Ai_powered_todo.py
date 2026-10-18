from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langgraph.checkpoint.memory import InMemorySaver
import streamlit as st

# Initialize the database connection
db = SQLDatabase.from_uri("sqlite:///my_tasks.db")

# create the table
db.run(
    """
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        status TEXT CHECK(status IN ('pending','in_progress','completed')) NOT NULL DEFAULT 'pending',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
"""
)

## llm,tools,memory,system_prompt,agent,chat history
llm = ChatGroq(model="openai/gpt-oss-120b")

#SqlDatabaseToolkit to create tools for CRUD operations on the tasks table
toolkit = SQLDatabaseToolkit(db=db, llm=llm)

#tools like create_task, read_tasks, update_task, delete_task are created by the toolkit
tools = toolkit.get_tools()


system_prompt = """
You are a task management assistant that interacts with a SQL database containing a 'tasks' table.

TASK RULES:
- Limit SELECT queries to 10 results max with ORDER BY created_at DESC
- After CREATE/UPDATE/DELETE, confirm with SELECT query
- If the user requests a list of tasks, present the output in a structured table format

CRUD OPERATIONS:
- CREATE: INSERT INTO tasks(title, description, status)
- READ: SELECT * FROM tasks WHERE ... LIMIT 10
- UPDATE: UPDATE tasks SET status=? WHERE id=? OR title=?
- DELETE: DELETE FROM tasks WHERE id=? OR title=?

Table schema: id, title, description, status(pending/in_progress/completed), created_at.
"""

#Create the agent with caching to avoid re-creation of memory object on every rerun
@st.cache_resource
def get_agent():
    agent = create_agent(
        model=llm,
        tools=tools,
        checkpointer=InMemorySaver(),
        system_prompt=system_prompt
    )
    return agent

agent = get_agent()

#Streamlit UI
st.subheader("Task Management Assistant")

#Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    role = message["role"]
    content = message["content"]
    st.chat_message(role).markdown(content)

#User input
prompt = st.chat_input("Ask me anything about your tasks!")

if prompt:
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    #Spinner while generating response
    with st.chat_message("assistant"):
            with st.spinner("Generating response..."):
                response = agent.invoke(
                    {"messages": [{"role": "user", "content": prompt}]},
                    {"configurable": {"thread_id":"1"}}
                )
                result=response['messages'][-1].content
                st.markdown(result)
                st.session_state.messages.append({"role": "assistant", "content": result})
