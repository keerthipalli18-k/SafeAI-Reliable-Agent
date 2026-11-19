
import streamlit as st

from request_interpreter import understand_request
from validator import validate_action
from tools.calculator import calculate
from tools.draft_creator import create_draft
from logger import save_log
from supabase_client import supabase


# -----------------------------------
# PAGE CONFIGURATION
# -----------------------------------

st.set_page_config(
    page_title="SafeAI Dashboard",
    page_icon="🛡️",
    layout="wide"
)


# -----------------------------------
# DASHBOARD HEADER
# -----------------------------------

st.title("🛡️ SafeAI")
st.subheader(
    "Reliable AI Agent with Tool Validation and Human Approval"
)

st.write(
    "Enter a request. SafeAI will interpret and validate it "
    "before asking for your approval."
)

st.divider()


# -----------------------------------
# USER REQUEST
# -----------------------------------

st.header("Enter Your Request")

user_request = st.text_area(
    "Enter your request",
    placeholder=(
        "Examples:\n"
        "Calculate 100 plus 200\n"
        "Create draft title: Welcome "
        "content: Welcome to SafeAI"
    ),
    height=120
)


# -----------------------------------
# GENERATE PROPOSAL
# -----------------------------------

if st.button("Generate Proposal", type="primary"):

    if not user_request.strip():

        st.warning("Please enter a request.")

    else:

        proposal = understand_request(user_request)

        tool_name = proposal["tool_name"]
        arguments = proposal["arguments"]

        # Validate the proposed action
        if tool_name != "None":

            is_valid, message = validate_action(
                tool_name,
                arguments
            )

        else:

            is_valid = False
            message = proposal["message"]

        # Save proposal in session state
        st.session_state.proposal = {
            "tool_name": tool_name,
            "arguments": arguments,
            "message": message,
            "is_valid": is_valid,
            "status": "Pending" if is_valid else "Invalid"
        }

        # Clear previous result
        st.session_state.pop("result", None)

        # Log invalid requests only once
        if not is_valid:

            logged_tool = (
                tool_name if tool_name != "None"
                else "Unknown Tool"
            )

            save_log(
                logged_tool,
                arguments,
                "Invalid",
                "Not requested",
                message
            )


# -----------------------------------
# DISPLAY PROPOSED ACTION
# -----------------------------------

if "proposal" in st.session_state:

    proposal = st.session_state.proposal

    tool_name = proposal["tool_name"]
    arguments = proposal["arguments"]

    st.divider()

    st.header("Proposed Action")

    st.write("**Tool:**", tool_name)

    st.write("**Arguments:**")

    st.json(arguments)

    # --------------------------------
    # VALID REQUEST
    # --------------------------------

    if proposal["is_valid"]:

        st.success(proposal["message"])

        # --------------------------------
        # HUMAN APPROVAL
        # --------------------------------

        if proposal["status"] == "Pending":

            st.header("Human Approval")

            st.warning(
                "Review the proposed action before approving it."
            )

            col1, col2 = st.columns(2)

            with col1:

                approve = st.button(
                    "Approve",
                    type="primary",
                    use_container_width=True
                )

            with col2:

                reject = st.button(
                    "Reject",
                    use_container_width=True
                )

            # --------------------------------
            # APPROVE ACTION
            # --------------------------------

            if approve:

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

                        raise ValueError(
                            "Unknown tool is not allowed."
                        )

                    save_log(
                        tool_name,
                        arguments,
                        "Valid",
                        "Approved",
                        result
                    )

                    st.session_state.result = {
                        "status": "Success",
                        "data": result
                    }

                    proposal["status"] = "Approved"

                except Exception as e:

                    error_message = str(e)

                    save_log(
                        tool_name,
                        arguments,
                        "Valid",
                        "Approved",
                        "Execution failed: " + error_message
                    )

                    st.session_state.result = {
                        "status": "Failed",
                        "data": error_message
                    }

                    proposal["status"] = "Failed"

                st.rerun()

            # --------------------------------
            # REJECT ACTION
            # --------------------------------

            if reject:

                save_log(
                    tool_name,
                    arguments,
                    "Valid",
                    "Rejected",
                    "Action was not executed"
                )

                proposal["status"] = "Rejected"

                st.session_state.result = {
                    "status": "Rejected",
                    "data": "Action rejected. Nothing was executed."
                }

                st.rerun()

        # --------------------------------
        # DISPLAY FINAL RESULT
        # --------------------------------

        if proposal["status"] == "Approved":

            if "result" in st.session_state:

                st.success("Action executed successfully!")

                st.subheader("Final Result")

                st.write(st.session_state.result["data"])

        elif proposal["status"] == "Rejected":

            st.warning(
                "Action rejected. Nothing was executed."
            )

        elif proposal["status"] == "Failed":

            if "result" in st.session_state:

                st.error(
                    "Execution failed: "
                    + str(st.session_state.result["data"])
                )

    # --------------------------------
    # INVALID REQUEST
    # --------------------------------

    else:

        st.error(
            "Request rejected: " + proposal["message"]
        )

        st.info(
            "Human approval was not requested because "
            "the request failed validation."
        )


# -----------------------------------
# SUPABASE ACTIVITY LOGS
# -----------------------------------

st.divider()

st.header("📋 Activity Logs")

st.write(
    "View the recent tool activities stored in Supabase."
)

if st.button("Refresh Activity Logs"):

    try:

        response = (
            supabase
            .table("tool_logs")
            .select("*")
            .order("id", desc=True)
            .limit(50)
            .execute()
        )

        if response.data:

            st.success(
                f"Loaded {len(response.data)} activity records."
            )

            st.dataframe(
                response.data,
                use_container_width=True,
                hide_index=True
            )

        else:

            st.info("No activity logs found.")

    except Exception as e:

        st.error(
            "Could not load activity logs: " + str(e)
        )


# -----------------------------------
# FOOTER
# -----------------------------------

st.divider()

st.caption(
    "SafeAI | Tool Validation | Human Approval | "
    "Supabase Activity Logging"
)
