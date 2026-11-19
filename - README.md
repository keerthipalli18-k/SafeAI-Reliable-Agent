# 🛡️ SafeAI – Reliable AI Agent with Tool Validation and Human Approval

## 1. Project Overview

SafeAI is a Python-based prototype designed to demonstrate safer tool execution through input validation and human approval.

It receives user requests, identifies supported actions, checks the inputs, and asks for human approval before executing a tool.

It also stores activity records in Supabase and displays them through a Streamlit dashboard.

**Note:** The current prototype uses a rule-based request interpreter. It is not yet connected to a Large Language Model (LLM).

## 2. Project Objectives

- Build a system that processes user requests.
- Validate inputs before executing tools.
- Require human approval before execution.
- Prevent invalid operations.
- Record tool activities in a database.
- Display activity logs through a dashboard.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Streamlit | Dashboard interface |
| Supabase | Database and activity storage |
| Regular Expressions | Request interpretation |
| VS Code | Development environment |
| Git and GitHub | Version control and project hosting |

## 4. Main Features

### Calculator
- Addition
- Subtraction
- Multiplication
- Division
- Division-by-zero validation

### Draft Creator
- Accepts a title and content.
- Validates the draft information.
- Creates a text draft after approval.

### Input Validation
- Checks tool names.
- Checks required arguments.
- Rejects invalid inputs.
- Prevents unsupported actions.

### Human Approval
- Displays the proposed action.
- Allows the user to approve or reject it.
- Executes approved actions only.

### Supabase Activity Logging
- Stores tool names.
- Stores input arguments.
- Stores validation status.
- Stores approval status.
- Stores execution results and timestamps.

### Streamlit Dashboard
- Accepts user requests.
- Displays proposed actions.
- Shows validation results.
- Provides approval and rejection controls.
- Displays recent activity logs.

## 5. Project Architecture

The application follows this workflow:

1. User enters a request.
2. Request Interpreter identifies the requested action.
3. Validator checks the inputs.
4. Invalid requests are rejected.
5. Valid requests are sent for human approval.
6. Approved requests are executed using the selected tool.
7. Results are stored in Supabase.
8. The dashboard displays the activity logs.

## 6. Project Folder Structure

```text
SafeAI/
│
├── tools/
│   ├── calculator.py
│   └── draft_creator.py
│
├── screenshots/
│
├── main.py
├── dashboard.py
├── agent.py
├── request_interpreter.py
├── validator.py
├── approval.py
├── logger.py
├── supabase_client.py
│
├── .env
├── .gitignore
├── requirements.txt
├── architecture.md
└── README.md
```

## 7. Installation and Setup

### Step 1: Clone the project

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd SafeAI
```

### Step 2: Create a virtual environment

```bash
python -m venv venv
```

### Step 3: Activate the environment

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### Step 4: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Configure environment variables

Create a `.env` file and add your Supabase project credentials:

```text
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_secret_key
```

Never upload your actual `.env` file or secret key to GitHub.

### Step 6: Run the application

Run the terminal application:

```bash
python main.py
```

Run the Streamlit dashboard:

```bash
python -m streamlit run dashboard.py
```

Open the local URL displayed in the terminal.

## 8. Testing and Results

The following tests were performed:

| Test Case | Expected Result | Status |
|---|---|---|
| Calculator addition | Correct result | Passed |
| Calculator subtraction | Correct result | Passed |
| Calculator multiplication | Correct result | To be verified |
| Division by zero | Request rejected | Passed |
| Draft creation | Draft generated | Passed |
| Human approval | Action executed | Passed |
| Human rejection | Action not executed | Passed |
| Unsupported request | Request rejected | Passed |
| Supabase logging | Activity recorded | Passed |
| Dashboard activity logs | Records displayed | Passed |

## 9. Limitations

- The current request interpreter uses predefined rules.
- It does not yet understand unrestricted natural language.
- It is not currently connected to an LLM API.
- Only the supported Calculator and Draft Creator tools are available.
- The prototype requires further security and reliability testing.

## 10. Future Enhancements

- Integrate an LLM API for better request understanding.
- Add more controlled tools.
- Improve input validation.
- Add stronger approval and execution safeguards.
- Add user authentication and role-based permissions.
- Improve dashboard analytics.
- Add more detailed audit logs.

## 11. Conclusion

SafeAI demonstrates how tool execution can be controlled through input validation, human approval, and activity logging.

The project helps show why an automated system should not execute every request without checking it first.

It provides a foundation for developing more reliable and controlled AI agents in the future.
