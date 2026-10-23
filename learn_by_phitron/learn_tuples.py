#a tuple is very similar to a list, but it is immutable, meaning that once it is created, it cannot be modified. Tuples are defined using parentheses () instead of square brackets [].
# %%
model_info = ("gpt-4o", 0.9, "OpenAI", "2024-06-17")
print(f"Model info: {model_info}")
print(f"Model name: {model_info[0]}")
# %%
