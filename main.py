# Copyright (c) Microsoft. All rights reserved.

import asyncio
import semantic_kernel as sk
import os
from semantic_kernel.connectors.ai.open_ai import AzureTextCompletion
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion


def import_system_prompt(path:str) -> str:
    
    if not os.path.exists(path):
       raise ValueError(f"system prompt does not exist: {path}")
    with open(path, "r") as config_file:
        return config_file.read()
    
kernel = sk.Kernel()

deployment, api_key, endpoint = sk.azure_openai_settings_from_dot_env()

kernel.add_chat_service("chart",AzureChatCompletion(deployment, endpoint, api_key))

prompt_config = sk.PromptTemplateConfig.from_completion_parameters(
    max_tokens=2000, temperature=0.5, top_p=0.8
)

prompt_template = sk.ChatPromptTemplate(
    "{{$input}}", kernel.prompt_template_engine, prompt_config
)

prompt_template.add_system_message(import_system_prompt("./prompt/system.txt"))

function_config = sk.SemanticFunctionConfig(prompt_config, prompt_template)
chat_functions = kernel.import_semantic_skill_from_directory("./prompt", "windup")
## kernel.register_semantic_function("ChatBot", "Chat", function_config)


async def chat() -> bool:

    try:
        user_input = input("What platform do you want to migrate:> ")
    except KeyboardInterrupt:
        print("\n\nExiting chat...")
        return False
    except EOFError:
        print("\n\nExiting chat...")
        return False

    if user_input == "exit":
        print("\n\nExiting chat...")
        return False

    for name, chat_function in chat_functions.items():
        #chat_function.
        answer = chat_function(user_input)
        print(f"{name}:> {answer}")

    return True


async def main() -> None:
    chatting = True
    while chatting:
        chatting = await chat()


    
if __name__ == "__main__":
    asyncio.run(main())



