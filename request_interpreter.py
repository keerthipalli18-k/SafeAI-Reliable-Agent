
import re


def understand_request(user_request):

    text = user_request.lower().strip()

    # Identify calculator requests
    numbers = re.findall(r"-?\d+(?:\.\d+)?", text)

    operation = None

    if any(word in text for word in ["add", "plus", "sum", "addition"]):
        operation = "add"

    elif any(word in text for word in ["subtract", "minus", "difference"]):
        operation = "subtract"

    elif any(word in text for word in ["multiply", "multiplied", "times", "product"]):
        operation = "multiply"

    elif any(word in text for word in ["divide", "divided", "division"]):
        operation = "divide"

    if operation is not None:

        if len(numbers) != 2:
            return {
                "tool_name": "None",
                "arguments": {},
                "message": "Please provide exactly two numbers."
            }

        a = float(numbers[0])
        b = float(numbers[1])

        # Handle phrases such as "subtract 10 from 50"
        if operation == "subtract" and " from " in text:
            a, b = b, a

        arguments = {
            "a": a,
            "b": b,
            "operation": operation
        }

        return {
            "tool_name": "Calculator",
            "arguments": arguments,
            "message": "Calculator request identified."
        }

    # Identify draft creation requests
    if "draft" in text or "create message" in text:

        title_match = re.search(
            r"title:\s*(.*?)(?=\s+content:|$)",
            user_request,
            re.IGNORECASE
        )

        content_match = re.search(
            r"content:\s*(.*)",
            user_request,
            re.IGNORECASE | re.DOTALL
        )

        if not title_match or not content_match:
            return {
                "tool_name": "None",
                "arguments": {},
                "message": "Please provide Title and Content."
            }

        arguments = {
            "title": title_match.group(1).strip(),
            "content": content_match.group(1).strip()
        }

        return {
            "tool_name": "Draft Creator",
            "arguments": arguments,
            "message": "Draft request identified."
        }

    # Reject unsupported requests
    return {
        "tool_name": "None",
        "arguments": {},
        "message": "Sorry, I could not identify a supported action."
    }
