#list are needed in AI because they are mutable, ordered, and can hold heterogeneous data types. This allows for easy manipulation of data, such as adding or removing elements, sorting, and iterating through the list. Lists are also versatile and can be used to store various types of information, making them essential for AI applications where data structures need to be flexible and efficient.
# %%
model_list = [
    "gpt-4o", "gpt-4", "gpt-3.5", "gpt-3.5-turbo", "gpt-3.5-turbo-16k", "gpt-3.5-turbo-16k-0613", "gpt-3.5-turbo-0613"]

print(f"Available models: {model_list}")
# %%
print(f"the last one: {model_list[-1]}")
# %%
model_list.append(["gemma-7b", "gemma-7b-chat", "gemma-7b-chat-v1.0", "gemma-7b-chat-v1.0-2024-06-17"])
print(f"model list updated: {model_list}")
# %%
del model_list[6:11]
print(f"model list updated: {model_list}")
# %%
scores = [0.9, 0.8, 0.7, 0.6, 0.5]
scores.sort()
print(f"sorted scores: {scores}")
# %%

nested_model_list_score = [
    ["gpt-4o", 0.9],    
    ["gpt-4", 0.8],
    ["gpt-3.5", 0.7],
    ["gpt-3.5-turbo", 0.6],
    ["gpt-3.5-turbo-16k", 0.5]
]
#find the model with the highest score
best_model = max(nested_model_list_score, key=lambda x: x[1])
print("best model: ", best_model)
# %%

questions = ["What is AI?", "What is machine learning?", "What is deep learning?"]
answers = ["AI is the simulation of human intelligence in machines.", "Machine learning is a subset of AI that allows systems to learn from data.", "Deep learning is a subset of machine learning that uses neural networks with many layers."]

make_pairs = list(zip(questions, answers))
print("question and answer pairs: ", make_pairs)

# %%
models = ["gpt-4o", "gpt-4", "gpt-3.5", "gpt-3.5-turbo", "gpt-3.5-turbo-16k"]
scores = [0.9, 0.8, 0.7, 0.6, 0.5]
make_pairs_2 = list(zip(models, scores))
print("model and score pairs: ", make_pairs_2)

# %%
empty_list = []
print(f"empty list: {empty_list}")
empty_list.append("mithun, bielefeld, Germany")
empty_list.append("AI enthusiast")
empty_list.append("Python programmer")
print(f"empty list updated: {empty_list}")
# %%
text_to_sql = ["SELECT * FROM users WHERE age > 30;", "INSERT INTO users (name, age) VALUES ('John', 25);", "UPDATE users SET age = 26 WHERE name = 'John';", "DELETE FROM users WHERE age < 20;"]
print("text to SQL: ", text_to_sql)
print("first SQL query: ", text_to_sql[0])
# %%
text_to_mdx = [dimension for dimension in range(1, 6)]
print("text to MDX: ", text_to_mdx)
# %%
