# Copyright (c) Microsoft. All rights reserved.

import asyncio
import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion,OpenAIChatCompletion
from util import import_chat_skill_from_directory,import_prompt


kernel = sk.Kernel()

useAzureOpenAI = True

# Configure AI service used by the kernel
if useAzureOpenAI:
    deployment, api_key, endpoint = sk.azure_openai_settings_from_dot_env()
    kernel.add_chat_service("chart",AzureChatCompletion(deployment, endpoint, api_key))
else:
    api_key, org_id = sk.openai_settings_from_dot_env()
    kernel.add_text_completion_service("chart", OpenAIChatCompletion("text-davinci-003", api_key, org_id))
    
prompt_config = sk.PromptTemplateConfig.from_completion_parameters(
            max_tokens=2000, temperature=0.5, top_p=0.8
)
    
chat_prompts = import_chat_skill_from_directory("./prompt", "windup")

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


    context_variables = sk.ContextVariables()
    context_variables["platform"] = user_input      
    answer = None
    assists = []

    for name, chat_prompt in sorted(chat_prompts.items(), key=lambda item: item[0]):
        prompt_template = sk.ChatPromptTemplate(
            "{{$user_input}}", kernel.prompt_template_engine, prompt_config
        )
        # prompt_template.add_system_message(import_prompt("./prompt/system.txt"));
        prompt_template.add_user_message(chat_prompt);
        for assist in assists:
            prompt_template.add_assistant_message(assist)
        function_config = sk.SemanticFunctionConfig(prompt_config, prompt_template)
        generateRule = kernel.register_semantic_function(
            'generateRule', 'generateRule', function_config
        )
        
        answer = await generateRule.invoke_async(variables=context_variables)
        print(f"{name}:> {answer}")
        print("\n")
        assists.append(f"{answer}")

    return True


async def main() -> None:
    # chatting = True
    # while chatting:
    #     chatting = await chat()
    await chat()

    
if __name__ == "__main__":
    asyncio.run(main())



