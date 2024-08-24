import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.model_selection import cross_val_score
from sklearn.datasets import load_iris



# Dados de exemplo
iris = load_iris()
X, y = iris.data, iris.target
dfo = pd.read_csv('/Users/Luis1/Projetos/Detection/datasets/csv/btc_orderbook_df.csv')

# Valores de "contamination" para teste
contaminations = np.linspace(0.01, 0.2, 20)

anomaly_inputs = ['price','volume']



# Validação cruzada
scores = []
for contamination in contaminations:
    clf = IsolationForest(contamination=contamination)
    
    score = np.mean(cross_val_score(clf,  X, y, cv=5, scoring='accuracy'))
    print(score)
    scores.append(score)

# Encontrar o melhor "contamination"
best_contamination = contaminations[np.argmax(scores)]

print(f"Melhor contamination: {best_contamination}")
