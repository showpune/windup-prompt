# Configure OpenAI service
## Use Azure OpenAI Service
If you are using azure openai service, you just need to provide `AZURE_OPENAI_DEPLOYMENT_NAME`, `AZURE_OPENAI_ENDPOINT` and `AZURE_OPENAI_API_KEY`
1) create open service from [link](https://portal.azure.com/#create/Microsoft.CognitiveServicesOpenAI)
2) Find the Endpoint(`AZURE_OPENAI_ENDPOINT`) and managed keys (`AZURE_OPENAI_API_KEY`) from overview
![image](https://github.com/showpune/windup-prompt/assets/1787505/836b2048-681d-42b9-8a37-873eb2734e8a)
3) Create a deployment with model type gpt and put the deployment name as `AZURE_OPENAI_DEPLOYMENT_NAME`
![image](https://github.com/showpune/windup-prompt/assets/1787505/5fe64dd1-32eb-48ba-8a76-1e942fe495e4)

