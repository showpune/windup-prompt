# Copyright (c) Microsoft. All rights reserved.

import asyncio
import semantic_kernel as sk
import os
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from util import import_prompt

kernel = sk.Kernel()

deployment, api_key, endpoint = sk.azure_openai_settings_from_dot_env()

kernel.add_chat_service("chart",AzureChatCompletion(deployment, endpoint, api_key))

async def chat() -> bool:

    try:
        user_input = input("What platform do you want to migrate (AWS, Azure, GCP):> ")
    except KeyboardInterrupt:
        print("\n\nExiting chat...")
        return False
    except EOFError:
        print("\n\nExiting chat...")
        return False

    if user_input == "exit":
        print("\n\nExiting chat...")
        return False

       
    prompt_config = sk.PromptTemplateConfig.from_completion_parameters(
        max_tokens=2000, temperature=0.7, top_p=0.8
    )

    prompt_template = sk.ChatPromptTemplate(
        import_prompt("./prompt/chat/ask.txt"), kernel.prompt_template_engine, prompt_config
    )
    prompt_template.add_system_message(import_prompt("./prompt/system.txt"));
    function_config = sk.SemanticFunctionConfig(prompt_config, prompt_template)

    generateRule = kernel.register_semantic_function(
        'generateRule', 'generateRule', function_config
    )
    
    context_variables = sk.ContextVariables()
    context_variables["platform"] = user_input               
    answer = await generateRule.invoke_async(variables=context_variables)
    print(f"Rules:> {answer}")
    return True


async def main() -> None:
    # chatting = True
    # while chatting:
    #     chatting = await chat()
    await chat()

    
if __name__ == "__main__":
    asyncio.run(main())



