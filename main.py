
from request_interpreter import understand_request
from agent import process_request


def main():

    print("\n================================")
    print("       SAFEAI APPLICATION")
    print("================================")

    print("Type 'exit' to close SafeAI.")

    while True:

        user_request = input("\nEnter your request: ")

        if user_request.lower().strip() == "exit":
            print("Thank you for using SafeAI!")
            break

        # Understand the user request
        proposal = understand_request(user_request)

        print("\nRequest Interpretation:")
        print(proposal["message"])

        tool_name = proposal["tool_name"]
        arguments = proposal["arguments"]

        # Send request to agent
        if tool_name == "None":

            result = process_request(
                "Unknown Tool", {}
            )

        else:

            result = process_request(
                tool_name, arguments
            )

        print("\nSafeAI Result:")
        print(result)


if __name__ == "__main__":
    main()
