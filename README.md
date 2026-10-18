# SmartTask — AI-Powered Task Management System

SmartTask is an AI-powered task management application designed to make everyday task organization easier through natural-language interaction with a SQL database. It uses an AI assistant to interpret user requests and perform task-management operations such as creating, viewing, updating, and deleting tasks.

## ✨ Features

- **AI-Powered Task Management:** Interact with the task manager using natural-language instructions.
- **Create Tasks:** Add new tasks with a title, description, and status.
- **View Tasks:** Retrieve task details from the SQL database.
- **Update Tasks:** Modify task status using a task ID or title.
- **Delete Tasks:** Remove tasks by specifying their ID or title.
- **Structured Task Results:** Display task lists in a structured table format.
- **Recent Tasks First:** Sort retrieved tasks by creation time, showing the newest first.
- **Controlled Database Queries:** Limit `SELECT` results to a maximum of 10 records.
- **Operation Verification:** Run a follow-up `SELECT` query after creating, updating, or deleting tasks to verify the database state.

## 🧠 How It Works

SmartTask combines an AI assistant with database operations to turn user instructions into task-management actions.

1. **User Input:** The user requests an action, such as creating a task or viewing pending tasks.
2. **AI Interpretation:** The AI assistant interprets the request according to the configured system prompt and task rules.
3. **Database Operation:** The appropriate SQL operation is performed against the `tasks` table.
4. **Verification:** After a create, update, or delete operation, a follow-up query checks the resulting database state.
5. **Response:** The assistant presents the result in a clear, user-friendly format.

## 🗄️ Database Schema

The application uses a `tasks` table with the following fields:

| Column | Description |
|---|---|
| `id` | Unique task identifier |
| `title` | Task title |
| `description` | Details about the task |
| `status` | Current task status |
| `created_at` | Task creation timestamp |

### Task Statuses

- `pending` — Task has not been started.
- `in_progress` — Task is currently being worked on.
- `completed` — Task has been finished.

## ⚙️ Supported CRUD Operations

CRUD stands for Create, Read, Update, and Delete.

| Operation | SQL action | Purpose |
|---|---|---|
| Create | `INSERT` | Add a new task |
| Read | `SELECT` | Retrieve existing tasks |
| Update | `UPDATE` | Change a task's status |
| Delete | `DELETE` | Remove a task |

### Query Rules

The AI assistant follows these task-management rules:

- Limit `SELECT` queries to 10 results maximum.
- Order retrieved tasks by `created_at DESC`.
- Verify create, update, and delete operations using a subsequent `SELECT` query.
- Present task lists in a structured table.
- Use task IDs or titles to identify tasks for updates and deletions.

## 🛠️ Technology Stack

- **Python** — Application logic.
- **SQL** — Task storage and database operations.
- **Large Language Model (LLM)** — Natural-language understanding and task-management assistance.
- **System Prompt Engineering** — Defines the assistant's behavior, database operation rules, and response format.

*Note: The exact LLM provider, SQL database engine, and additional libraries should be confirmed from the source code and `requirements.txt`.*

## 📁 Project Structure

```text
SmartTask/
├── apps/
│   └── ai_powered_todo.py
├── requirements.txt
├── .gitignore
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or a compatible version supported by the project's dependencies.
- Required Python packages listed in `requirements.txt`.
- Access to the SQL database configured by the application.
- Any API credentials required by the configured AI model.

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/Krizhere/SmartTask.git
cd SmartTask
```

**2. Create a virtual environment**

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Configure environment variables**

Set the required database connection details and AI provider credentials according to the configuration used in the source code. Keep API keys and other secrets out of version control.

**5. Run the application**

```bash
python apps/ai_powered_todo.py
```

Follow the application's configured startup instructions if it uses a framework-specific launcher or requires additional setup.

## 💡 Example Use Cases

You can use the assistant for requests such as:

- "Create a task titled Complete the project report."
- "Show me my latest tasks."
- "Update the status of task 3 to in progress."
- "Mark the project report as completed."
- "Delete the task with ID 5."
- "List my pending tasks in a table."

The exact commands supported depend on the application's AI model, prompt configuration, and database implementation.

## 🔒 Security Considerations

- Keep AI API keys and database credentials in environment variables.
- Use parameterized SQL queries to prevent SQL injection.
- Validate user input before executing database operations.
- Apply appropriate safeguards to destructive operations.
- Restrict database permissions to the operations required by the application.

## 🎯 Project Objective

The goal of SmartTask is to demonstrate how AI assistants can simplify traditional task-management workflows by combining natural-language interaction, SQL database operations, and clear result verification.

## 👨‍💻 Author

**Krish Kumar**

- GitHub: [@Krizhere](https://github.com/Krizhere)
- Project Repository: [SmartTask](https://github.com/Krizhere/SmartTask)

---

If you find this project useful, consider giving the repository a ⭐ on GitHub.
