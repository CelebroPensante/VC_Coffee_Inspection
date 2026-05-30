# ☕ Inspeção Visual de Grãos de Café Verde — Pipeline Clássico de Visão Computacional

Projeto de classificação automática de defeitos em grãos de café verde usando segmentação, extração de features manuais e classificadores clássicos de ML.

---

## 🚀 Como executar (3 comandos)

```bash
pip install -r requirements.txt
jupyter notebook
# Abra e execute os notebooks na ordem: 01 → 02 → 03 (→ 04 opcional)
```

> **Pré-requisito:** configure as credenciais do Kaggle (`~/.kaggle/kaggle.json`) antes de rodar.

---

## 📁 Estrutura do repositório

```
coffee_inspection/
├── notebooks/
│   ├── 01_segmentacao.ipynb       # Segmentação e isolamento dos grãos
│   ├── 02_features.ipynb          # Extração de features manuais
│   ├── 03_classificacao.ipynb     # Treinamento e avaliação dos modelos
│   └── 04_bonus_xai.ipynb         # XAI com SHAP (opcional)
├── outputs/
│   ├── X.csv                      # Matriz de features
│   ├── y.csv                      # Rótulos numéricos
│   ├── label_map.csv              # Mapeamento índice → nome de classe
│   └── *.png                      # Figuras geradas (boxplots, matrizes, etc.)
├── requirements.txt
└── README.md
```

---

## 📓 Notebooks

| Notebook | Conteúdo |
|---|---|
| `01_segmentacao.ipynb` | Download do dataset, comparação de dois métodos de segmentação (HSV + morfologia vs. Canny + contornos), extração de recortes |
| `02_features.ipynb` | Extração de features de forma, cor (HSV), textura (GLCM) e momentos de Hu; análise exploratória; exportação de X.csv e y.csv |
| `03_classificacao.ipynb` | Split treino/val/teste estratificado, normalização, GridSearchCV, avaliação (acurácia, F1, matriz de confusão), análise de erros |
| `04_bonus_xai.ipynb` | SHAP summary plots, permutation importance, ablation study por grupos de features |

---

## 🗃️ Dataset

**Dataset:** [sujitraarw/coffee-green-bean-with-17-defects-original](https://www.kaggle.com/datasets/sujitraarw/coffee-green-bean-with-17-defects-original)

**Classes (17):** Broken, Cut, Dry Cherry, Fade, Floater, Full Black, Full Sour, Fungus Damage, Husk, Immature, Parchment, Partial Black, Partial Sour, Severe Insect Damage, Shell, Slight Insect Damage, Withered

---

## ⚙️ Configurações globais

- `random_state = 42` em todas as operações aleatórias
- Split: 70% treino / 15% validação / 15% teste (estratificado)
- Normalização: `StandardScaler` ajustado apenas no treino
- Sem data leakage: teste nunca é visto durante treino/validação
