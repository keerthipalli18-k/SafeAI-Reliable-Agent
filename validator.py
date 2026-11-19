
def validate_action(tool_name, arguments):

    # Check calculator tool
    if tool_name == "Calculator":

        if set(arguments.keys()) != {"a", "b", "operation"}:
            return False, "Invalid calculator arguments"

        a = arguments["a"]
        b = arguments["b"]
        operation = arguments["operation"]

        # Check number types
        if isinstance(a, bool) or not isinstance(a, (int, float)):
            return False, "First value must be a number"

        if isinstance(b, bool) or not isinstance(b, (int, float)):
            return False, "Second value must be a number"

        # Check allowed operations
        if operation not in ["add", "subtract", "multiply", "divide"]:
            return False, "Invalid calculator operation"

        if operation == "divide" and b == 0:
            return False, "Division by zero is not allowed"

        return True, "Calculator request is valid"

    # Check draft creator tool
    elif tool_name == "Draft Creator":

        if set(arguments.keys()) != {"title", "content"}:
            return False, "Invalid draft arguments"

        title = arguments["title"]
        content = arguments["content"]

        if not isinstance(title, str) or not title.strip():
            return False, "Draft title cannot be empty"

        if not isinstance(content, str) or not content.strip():
            return False, "Draft content cannot be empty"

        if len(title) > 100:
            return False, "Draft title is too long"

        if len(content) > 2000:
            return False, "Draft content is too long"

        return True, "Draft request is valid"

    # Reject unknown tools
    else:
        return False, "Unknown tool is not allowed"
