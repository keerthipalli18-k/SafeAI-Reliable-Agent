
from supabase_client import supabase


def save_log(tool_name, input_data, validation_status,
             approval_status, execution_result):

    try:
        data = {
            "tool_name": tool_name,
            "input_data": input_data,
            "validation_status": validation_status,
            "approval_status": approval_status,
            "execution_result": str(execution_result)
        }

        response = supabase.table("tool_logs").insert(data).execute()

        print("Activity saved to Supabase!")
        return response

    except Exception as e:
        print("Could not save activity:", e)
        return None
