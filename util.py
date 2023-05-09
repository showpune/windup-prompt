
import glob
import os
from typing import Dict

def import_prompt(path:str) -> str:
    if not os.path.exists(path):
       raise ValueError(f"system prompt does not exist: {path}")
    with open(path, "r") as config_file:
        return config_file.read()

def import_chat_skill_from_directory(parent_directory: str, skill_directory_name: str
    ) -> Dict[str, str]:
        PROMPT_FILE = "skprompt.txt"

        skill_directory = os.path.join(parent_directory, skill_directory_name)
        skill_directory = os.path.abspath(skill_directory)

        if not os.path.exists(skill_directory):
            raise ValueError(f"Skill directory does not exist: {skill_directory_name}")

        skill = {}

        directories = glob.glob(skill_directory + "/*/")
        for directory in directories:
            dir_name = os.path.dirname(directory)
            function_name = os.path.basename(dir_name)
            if function_name != 'generateRules':
                prompt_path = os.path.join(directory, PROMPT_FILE)

                # Continue only if the prompt template exists
                if not os.path.exists(prompt_path):
                    continue

            
                # Load Prompt Template
                with open(prompt_path, "r") as prompt_file:
                    prompt = prompt_file.read();

                skill[function_name] = prompt

        return skill
    

