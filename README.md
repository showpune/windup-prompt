# windup-prompt: generate the windup rules by open AI
## Introduce
Three way to use OpenAI to generate windup rules
1) By chat with system prompt
2) A sequence of asks to get more context, make the result more precise
3) Use sematical kernal to make the ask plan to generate the rule

## Installation
1. Configration the connection to open AI
```
cp .env-sample .env
```
Config the connection string to azure open ai service, to create the azure open ai service and get the configuration, check [link](https://github.com/showpune/windup-prompt/blob/master/how-to.md)) 

Install the requirements
```
python -m pip install -r requirements.txt
```

## Simple: Generate the rules directly
Run the code 
```
python simple-main.py
```
Use the [system prompt](https://github.com/showpune/windup-prompt/blob/master/prompt/system.txt) and [user prompt](https://github.com/showpune/windup-prompt/blob/master/prompt/chat/ask.txt) to generate the windup rules, input any platform you want to migration:
![image](https://user-images.githubusercontent.com/1787505/236997115-126f8b89-ff2a-4410-90bf-c808ddedf41d.png)


## Chat Sequence
* Since the Open AI can't get all the context in one ask to generate the rules, you can use a sequence chat to get more information, like the service partern, API pattern and special concept, and then use the information as assist prompt to generate the rule
* You can find the sequence of chat from [Chat Sequence](https://github.com/showpune/windup-prompt/tree/master/prompt/windup).
* The chat will asked by the sequence of the folder name, we need the sequence since some ask is dependent. Like we have the special concept of a platform, then we can ask the API pattern
Test the sequence ask by 
```
python pipe-main.py
```
The result looks like

![image](https://user-images.githubusercontent.com/1787505/236998182-bef8aabd-8c6e-4215-9c8d-66623d086460.png)
![image](https://user-images.githubusercontent.com/1787505/236998273-61187753-8f07-4ab3-add2-2f268f42753f.png)
![image](https://user-images.githubusercontent.com/1787505/236998302-db6b8583-93d5-4e1c-882c-e2cadb06d1bf.png)

## Semantical Kernal: Generate the rule by auto-gpt
There are more ask
1) Should I care about the sequence in [Chat Sequence](https://github.com/showpune/windup-prompt/tree/master/prompt/windup)?
2) Is there any more skills shared by others I can use to generate the windup rules?
3) Is the skills I defined make sense?
Let sematical kernal to handle it: It will read all the skills from  [Chat Sequence](https://github.com/showpune/windup-prompt/tree/master/prompt/windup), merge with system skills and make a plan to generate the windup rules
```
python pipe-main.py
```
![image](https://user-images.githubusercontent.com/1787505/236999884-8e9d14cc-2a97-4bec-ab98-e9913553c312.png)
