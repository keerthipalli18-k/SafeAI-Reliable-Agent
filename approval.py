
def request_approval(tool_name, arguments):

    print("\n========== HUMAN APPROVAL ==========")

    print("Proposed Tool:", tool_name)
    print("Proposed Arguments:", arguments)

    print("\nDo you approve this action?")

    choice = input("Enter YES or NO: ").strip().lower()

    if choice == "yes":
        print("Human approval granted!")
        return True

    else:
        print("Action rejected by human reviewer.")
        return False
