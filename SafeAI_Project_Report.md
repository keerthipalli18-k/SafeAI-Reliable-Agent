# SAFEAI – PROJECT REPORT

## 1. Introduction

SafeAI is a Python-based prototype that demonstrates how tool execution can be made safer using input validation and human approval.

The system accepts user requests, identifies supported tools, validates the inputs, and asks for human approval before executing an action.

It uses Supabase to store activity logs and Streamlit to display the application dashboard.

## 2. Problem Statement

Automated systems may perform incorrect or unwanted actions when user requests are not properly checked.

SafeAI addresses this problem by introducing validation, human approval, and activity logging before and after tool execution.

## 3. Objectives

- Understand user requests.
- Identify supported tools.
- Validate inputs before execution.
- Request human approval.
- Prevent invalid actions.
- Store execution details in Supabase.
- Display activity logs through Streamlit.

## 4. Technologies Used

| Technology | Application |
|---|---|
| Python | Application development |
| Streamlit | Web dashboard |
| Supabase | Database |
| Regular Expressions | Rule-based request interpretation |
| VS Code | Code development |

## 5. System Modules

### 5.1 Request Interpreter

Identifies supported requests using predefined rules and keywords.

### 5.2 Validator

Checks whether the requested tool and its arguments are valid.

### 5.3 Human Approval

Allows the user to approve or reject a proposed action.

### 5.4 Calculator

Performs addition, subtraction, multiplication, and division.

### 5.5 Draft Creator

Creates text drafts using a title and content.

### 5.6 Activity Logger

Stores tool activity, validation status, approval status, and execution results.

### 5.7 Streamlit Dashboard

Provides a user interface for submitting requests, reviewing actions, and viewing activity logs.

## 6. Working Process

1. The user enters a request.
2. The interpreter identifies the requested action.
3. The validator checks the inputs.
4. Invalid requests are rejected.
5. Valid requests are displayed for human approval.
6. The user approves or rejects the action.
7. Approved actions are executed.
8. The activity is recorded in Supabase.
9. The dashboard displays recent activity records.

## 7. Database Design

The project uses a Supabase table named `tool_logs`.

| Column | Purpose |
|---|---|
| id | Record identifier |
| tool_name | Name of the selected tool |
| input_data | Arguments supplied to the tool |
| validation_status | Valid or Invalid |
| approval_status | Approved, Rejected, or Not requested |
| execution_result | Result or rejection message |
| created_at | Record creation time |

## 8. Testing and Results

The following tests were performed:

| Test | Result |
|---|---|
| Calculator addition | Passed |
| Calculator subtraction | Passed |
| Draft creation | Passed |
| Human approval | Passed |
| Human rejection | Passed |
| Division by zero validation | Passed |
| Unsupported request rejection | Passed |
| Supabase activity logging | Passed |
| Streamlit activity display | Passed |

## 9. Screenshots

The following screenshots are included as project evidence:

1. SafeAI dashboard.
2. Calculator execution.
3. Draft Creator execution.
4. Human approval screen.
5. Human rejection result.
6. Division-by-zero rejection.
7. Unsupported request rejection.
8. Supabase activity logs.
9. Streamlit activity log table.

## 10. Limitations

- The current request interpreter is rule-based.
- The application does not yet use an LLM API.
- Only two tools are currently supported.
- Further security and reliability testing is required.

## 11. Future Enhancements

- Integrate an LLM API.
- Add more controlled tools.
- Improve request understanding.
- Add user authentication.
- Improve approval safeguards.
- Add advanced activity monitoring.

## 12. Conclusion

SafeAI demonstrates how input validation, human approval, and activity logging can help control tool execution.

The prototype provides a foundation for building more reliable and responsible AI agent systems.
