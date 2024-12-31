import autogen

BASE_URL="http://localhost:11434/v1"
config_list_mistral = [
        {
            'base_url': BASE_URL,
            'api_key': "NULL",
            'model': "mistral"
        }
]

config_list_codellama = [
        {
            'base_url': BASE_URL,
            'api_key': "NULL",
            'model': "codellama"
        }
]

llm_config_mistral={
        "config_list": config_list_mistral,
}

llm_config_codellama={
        "config_list": config_list_codellama,
}

coder = autogen.AssistantAgent(
        name="Coder",
        llm_config=llm_config_codellama
)

user_proxy = autogen.UserProxyAgent(
        name="user_proxy",
        human_input_mode="NEVER",
        max_consecutive_auto_reply=10,
        is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
        code_execution_config={"work_dir": "web", "use_docker": False},
        llm_config=llm_config_mistral,
        system_message="""Reply TERMINATE if the task has been solved at full satisfaction.
        Otherwise, reply CONTINUE, or the reason why the task is not solved yet."""
)


task="""
Write an indentated Python script to generate the prime numbers in the range of 1 to 100, and then the user_proxy agent should run the script to verify the output
"""
user_proxy.initiate_chat(coder, message=task)

'''
assistant = autogen.AssistantAgent(
        name="Assistant",
        llm_config=llm_config_mistral
)

task="""Tell me a joke """
groupchat = autogen.GroupChat(agents=[user_proxy, coder, assistant], messages=[], max_round=12)
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config_mistral)
user_proxy.initiate_chat(manager, message=task)
'''
