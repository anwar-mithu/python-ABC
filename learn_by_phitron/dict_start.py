#we will learn how to create a dictionary in python
#06. Dictionaries
# VERY IMPORTANT for:
#- AI
#- APIs
#- JSON
#- Agent state
#A dictionary is one of the most important Python structures for AI, APIs, JSON, configuration files, model outputs, and agent state.
# %%
model = {
    "name": "gpt-4",
    "version": "0.1",
    "description": "A large language model for AI applications."
}

print(f"name of the model is: {model["name"]}")
print(f"version of thr model is: {model["version"]}")
print(f"description of the model is: {model["description"]}")
# %%
# the distionary is {key : value} 

api_info = { 
    "name": "OpenAI API",
    "version": "v1",    
    "key": "value",
    "password": "203948ß02"
}
#print all info in line by line
print(f"print all info in line by line: {api_info}")
for key, value in api_info.items():
    print(f"{key}: {value}")
# %%
