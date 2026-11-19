
from validator import validate_action
from approval import request_approval
from logger import save_log

from tools.calculator import calculate
from tools.draft_creator import create_draft


def process_request(tool_name, arguments):

    print("\n========== SAFEAI AGENT ==========")

    # Step 1: Validate request
    is_valid, message = validate_action(
        tool_name, arguments
    )

    print("\nValidation:", message)

    # Step 2: Reject invalid requests
    if not is_valid:

        save_log(
            tool_name,
            arguments,
            "Invalid",
            "Not requested",
            message
        )

        return message

    # Step 3: Request human approval
    approved = request_approval(
        tool_name, arguments
    )

    # Step 4: Check approval
    if not approved:

        save_log(
            tool_name,
            arguments,
            "Valid",
            "Rejected",
            "Action was not executed"
        )

        return "Action rejected. Nothing was executed."

    # Step 5: Execute approved tool
    try:

        if tool_name == "Calculator":

            result = calculate(
                arguments["a"],
                arguments["b"],
                arguments["operation"]
            )

        elif tool_name == "Draft Creator":

            result = create_draft(
                arguments["title"],
                arguments["content"]
            )

        else:
            return "Unknown tool"

        # Step 6: Save activity
        save_log(
            tool_name,
            arguments,
            "Valid",
            "Approved",
            result
        )

        print("\nExecution completed successfully!")

        return result

    except Exception as e:

        save_log(
            tool_name,
            arguments,
            "Valid",
            "Approved",
            "Execution failed: " + str(e)
        )

        return "Execution failed: " + str(e)
