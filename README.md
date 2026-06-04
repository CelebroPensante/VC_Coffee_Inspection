# Sistema de Inspeção Visual Automática — Grãos de Café

**Disciplina:** Visão Computacional  
**Cenário:** B — Inspeção de grãos de café em cooperativa  
**Dataset:** [Coffee Green Bean with 17 Defects](https://www.kaggle.com/datasets/sujitraarw/coffee-green-bean-with-17-defects-original) (Kaggle)  
**Equipe:** Kauã abrahao de almeida, Vitor Gustavo J. de Carvalho e Lucas Tiepo de Oliveira  
**Prazo:** 07/06/2026

---

## Visão geral

Este projeto implementa um pipeline completo de visão computacional para classificação automática de grãos de café verdes com defeitos, cobrindo segmentação, extração de features manuais, classificação clássica e explicabilidade (XAI).

```
imagem RGB
  → segmentação (HSV ou Canny)
  → extração de features (forma, Hu, cor, textura)
  → tabela X + vetor y
  → Random Forest / SVM
  → avaliação (acurácia, F1, matriz de confusão)
  → XAI (SHAP, permutation importance, ablation study)
```

---

## Estrutura do repositório

```
projeto-inspecao-cafe/
├── notebooks/
│   ├── 01_segmentacao.ipynb       # Comparação de dois métodos de segmentação
│   ├── 02_features.ipynb          # Extração de features manuais e análise exploratória
│   ├── 03_classificacao.ipynb     # Treinamento, avaliação e comparação dos modelos
│   └── 04_bonus_xai.ipynb         # SHAP, permutation importance e ablation study
├── outputs/
├── README.md
└── requirements.txt
```

---

## Execução rápida (3 comandos)

```bash
# 1. Instalar dependências
pip install -r requirements.txt

# 2. Abrir o Jupyter
jupyter notebook

# 3. Executar os notebooks em ordem:
#    01_segmentacao → 02_features → 03_classificacao → 04_bonus_xai
```

> **Nota:** o notebook `01_segmentacao.ipynb` faz download automático do dataset via `kagglehub`.  

---

## Dependências

```
numpy
pandas
opencv-python
scikit-image
scikit-learn
matplotlib
seaborn
tqdm
kagglehub
shap
jupyter
```

Arquivo completo em `requirements.txt`.

---

## Pipeline detalhado

### 1. Segmentação (`01_segmentacao.ipynb`)

Dois métodos comparados visualmente em amostras de cada classe:

| Método | Técnica | Vantagem | Limitação |
|--------|---------|----------|-----------|
| A | Limiarização HSV + morfologia | Simples, rápido | Sensível a variações de iluminação |
| B | Canny + fechamento + contornos | Não depende de cor | Ruído em texturas complexas |

O método escolhido é salvo em `outputs/pipeline_config.json`.

### 2. Extração de features (`02_features.ipynb`)

Vetor com **32 features** por grão, cobrindo quatro famílias:

| Família | Features |
|---------|----------|
| Forma (6) | área, perímetro, excentricidade, solidez, extent, circularidade |
| Momentos de Hu (7) | 7 momentos invariantes em escala log |
| Cor HSV (14) | média + desvio-padrão de H, S, V + histograma de matiz (8 bins) |
| Textura GLCM (4) | contraste, homogeneidade, energia, correlação |

Todas extraídas **dentro da máscara** do grão (sem contaminação do fundo).

### 3. Classificação (`03_classificacao.ipynb`)

- **Split:** 70 % treino / 15 % validação / 15 % teste (estratificado, `random_state=42`)
- **Normalização:** `StandardScaler` ajustado **apenas** em `X_train`
- **Modelos:** Random Forest e SVM RBF, ambos com `GridSearchCV` (5-fold estratificado)
- **Métricas reportadas:** acurácia, precisão, recall, F1 (macro e micro), matriz de confusão absoluta e normalizada

### 4. XAI — bônus (`04_bonus_xai.ipynb`)

| Técnica | Implementação |
|---------|---------------|
| SHAP | `TreeExplainer` sobre Random Forest, `summary_plot` e bar plot global |
| Permutation importance | `sklearn.inspection`, 10 repetições, barras de erro |
| Ablation study | 7 grupos de features, F1-macro e acurácia no conjunto de teste |

---

## Reprodutibilidade

`random_state = 42` fixado em todos os pontos: splits, `GridSearchCV`, `RandomForestClassifier`, `SVC` e `np.random.seed`.  
Executando os notebooks em ordem, os resultados são idênticos a cada execução.

---

## Resultados (após execução)

> Preencher após executar os notebooks.

| Modelo | Acurácia | Precisão (macro) | Recall (macro) | F1 (macro) |
|--------|----------|-----------------|----------------|------------|
| Random Forest | — | — | — | — |
| SVM RBF | — | — | — | — |

---

## Referências

- Dataset: [Coffee Green Bean with 17 Defects — Kaggle](https://www.kaggle.com/datasets/sujitraarw/coffee-green-bean-with-17-defects-original)
- Scikit-learn documentation: [scikit-learn.org](https://scikit-learn.org)
- OpenCV documentation: [docs.opencv.org](https://docs.opencv.org)
