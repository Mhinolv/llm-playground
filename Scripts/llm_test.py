import llm
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

dataPath = '/Users/MarkHinojosa/llm-base/Raw Data/REVIEWS.csv'
reviewDF = pd.read_csv(dataPath)
sampleText = reviewDF['text_'].head(20)

model = llm.get_model("wizardlm-13b-v1")
response = model.prompt(f"Give me a sumary these reviews : {sampleText}",
                        system="Asnwer like a Data Analyst")
print(response.text())