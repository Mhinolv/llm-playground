import llm
model = llm.get_model("wizardlm-13b-v1")
response = model.prompt("Can you create a 5-day learning plan for the Pandas library in Python",
                        system="Asnwer like a Computer Science professor")
print(response.text())