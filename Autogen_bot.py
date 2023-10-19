from autogen import AssistantAgent, UserProxyAgent, config_list_from_json

# Load LLM inference endpoints from the configuration file
config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST.json")

# Initialize the assistant agent with the LLM configurations
assistant = AssistantAgent("assistant", llm_config={"config_list": config_list})

# Initialize the user proxy agent for code execution (optional, but included for completeness)
user_proxy = UserProxyAgent("user_proxy", code_execution_config={"work_dir": "coding"})

# Define a function to handle user input and initiate a chat
def chat_with_bot(user_message):
    response = user_proxy.initiate_chat(assistant, message=user_message)
    return response

# Example usage
user_input = input("You: ")
bot_response = chat_with_bot(user_input)
print(f"Bot: {bot_response}")
