# Relatório de Análise Exploratória de Dados - Sentiment Analysis

## 📊 Sumário Executivo

Este relatório apresenta os resultados da análise exploratória de dados realizada no notebook `analise_exploratoria.ipynb`, que examinou detalhadamente o dataset Sentiment140 com 1.6 milhões de tweets para análise de sentimentos. A análise revelou insights importantes sobre padrões linguísticos, distribuição de sentimentos e características textuais dos dados.

---

## 🔍 1. Características Gerais do Dataset

### 1.1 Dimensões e Estrutura
- **Total de registros:** 1.600.000 tweets
- **Número de colunas:** 6 variáveis (target, ids, date, flag, user, text)
- **Tamanho em memória:** 507.21 MB
- **Período temporal:** Dados coletados em 2009
- **Qualidade dos dados:** 100% completo - sem valores ausentes

### 1.2 Tipos de Dados
```
target: int64      (rótulo de sentimento)
ids: int64         (identificador único)
date: object       (timestamp)
flag: object       (flag de consulta - "NO_QUERY")
user: object       (nome do usuário)
text: object       (conteúdo do tweet)
```

### 1.3 Unicidade dos Dados
- **Textos únicos:** 1.581.466 (98.8% de unicidade)
- **Usuários únicos:** 659.775 usuários distintos
- **Timestamps únicos:** 774.363 momentos diferentes
- **Texto mais frequente:** "isPlayer Has Died! Sorry" (210 ocorrências)

---

## 📈 2. Distribuição de Sentimentos

### 2.1 Balanceamento das Classes
O dataset apresenta uma **distribuição perfeitamente balanceada**:

| Sentimento | Quantidade | Percentual |
|------------|------------|------------|
| **Negativo** | 800.000 | 50.00% |
| **Positivo** | 800.000 | 50.00% |
| **Neutro** | 0 | 0.00% |

> **💡 Insight Crítico:** A ausência de sentimentos neutros simplifica o problema para classificação binária, mas pode limitar a aplicabilidade real do modelo em textos ambíguos.

### 2.2 Codificação dos Targets
- **Target 0:** Sentimento Negativo
- **Target 4:** Sentimento Positivo
- **Target 2:** Não presente no dataset (seria neutro)

---

## 📝 3. Análise Textual Detalhada

### 3.1 Estatísticas Gerais de Texto

| Métrica | Valor |
|---------|--------|
| **Comprimento médio** | 74.1 caracteres |
| **Palavras médias** | 12.5 palavras |
| **Maior texto** | 803 caracteres |
| **Menor texto** | 6 caracteres |

### 3.2 Comparação por Sentimento

| Métrica | Negativo | Positivo | Diferença |
|---------|----------|----------|-----------|
| **Comprimento médio** | 74.30 char | 73.89 char | +0.41 char |
| **Mediana comprimento** | 70.0 char | 69.0 char | +1.0 char |
| **Desvio padrão** | 36.75 | 36.16 | +0.59 |
| **Palavras médias** | 13.04 | 11.97 | **+1.07 palavras** |
| **Mediana palavras** | 12.0 | 11.0 | +1.0 palavra |
| **Caracteres médios** | 64.70 | 60.96 | +3.74 char |

> **🎯 Insight Principal:** Tweets negativos são consistentemente mais longos e detalhados, sugerindo que críticas e reclamações requerem mais elaboração textual que elogios.

### 3.3 Distribuição de Comprimento
- **Padrão observado:** Distribuição aproximadamente normal com leve assimetria positiva
- **Concentração:** Maioria dos tweets entre 40-120 caracteres
- **Outliers:** Textos muito longos (>200 char) representam pequena parcela

---

## 🔤 4. Análise de Vocabulário

### 4.1 Palavras Mais Frequentes (Geral)

| Posição | Palavra | Frequência | Contexto |
|---------|---------|------------|----------|
| 1 | **good** | 89.403 | Avaliação positiva |
| 2 | **day** | 82.366 | Referência temporal |
| 3 | **get** | 81.487 | Ação/obtenção |
| 4 | **like** | 77.749 | Comparação/preferência |
| 5 | **dont** | 66.929 | Negação |
| 6 | **today** | 64.611 | Temporal específico |
| 7 | **going** | 64.089 | Ação futura |
| 8 | **love** | 63.467 | Sentimento positivo |
| 9 | **work** | 62.776 | Atividade profissional |
| 10 | **cant** | 62.600 | Impossibilidade |

### 4.2 Diferenciação Vocabular por Sentimento

**Características dos Tweets Negativos:**
- **Top palavras:** "get", "dont", "work", "cant", "like", "day"
- **Padrões linguísticos:** 
  - Uso frequente de negações ("dont", "cant")
  - Verbos de ação ("get", "work")
  - Expressões de limitação ("miss", "want")

**Características dos Tweets Positivos:**
- **Top palavras:** "good", "love", "day", "like", "get", "thanks"
- **Padrões linguísticos:**
  - Adjetivos positivos ("good")
  - Expressões de gratidão ("thanks")
  - Sentimentos ("love")
  - Interjeições ("lol")

> **📊 Insight Vocabular:** Existe clara diferenciação lexical, com vocabulário negativo focado em limitações e impossibilidades, enquanto o positivo enfatiza qualidades e gratidão.

---

## 📊 5. Visualizações e Padrões Identificados

### 5.1 Distribuições Estatísticas
- **Histogramas:** Revelaram distribuição normal para comprimento de texto
- **Box plots:** Mostraram outliers significativos em ambas as classes
- **Violin plots:** Confirmaram densidade similar entre sentimentos

### 5.2 Correlações Identificadas
- **Correlação positiva forte:** Comprimento do texto vs. número de palavras (esperado)
- **Correlação fraca:** Sentimento vs. características textuais
- **Padrão temporal:** Distribuição uniforme ao longo do tempo

### 5.3 Outliers e Anomalias
- **Textos extremamente longos:** <1% do dataset (>300 caracteres)
- **Textos muito curtos:** ~2% do dataset (<20 caracteres)
- **Usuários muito ativos:** Alguns usuários com centenas de tweets

---

## 🧹 6. Qualidade e Integridade dos Dados

### 6.1 Completude dos Dados
- ✅ **Valores ausentes:** 0% em todas as colunas
- ✅ **Consistência:** Todos os targets são válidos (0 ou 4)
- ✅ **Formato:** Textos em formato string consistente

### 6.2 Características Específicas do Twitter
- **Menções:** Presença de @username
- **URLs:** Links diversos (http, www)
- **Hashtags:** Uso de # para tópicos
- **Linguagem informal:** Abreviações ("lol", "dont", "cant")
- **Emoticons:** Removidos no processamento original

### 6.3 Limitações Identificadas
1. **Temporal:** Dados de 2009 podem não refletir linguagem atual
2. **Domínio:** Específico para Twitter, pode não generalizar
3. **Binariedade:** Ausência de classe neutra limita aplicabilidade
4. **Processamento:** Emoticons já removidos, perdendo informação emocional

---

## 🎯 7. Principais Descobertas e Insights

### 7.1 Padrões Comportamentais
1. **Elaboração negativa:** Usuários tendem a ser mais verbosos ao expressar insatisfação
2. **Concisão positiva:** Elogios e satisfação são expressos de forma mais direta
3. **Vocabulário distintivo:** Clara separação lexical entre sentimentos
4. **Consistência temporal:** Padrões se mantêm ao longo do período

### 7.2 Implicações para Modelagem
1. **Balanceamento:** Dataset ideal para treinamento sem necessidade de ajustes
2. **Features textuais:** Comprimento pode ser feature preditiva
3. **Vocabulário:** Diferenciação clara facilita classificação
4. **Qualidade:** Ausência de ruído (missing values) otimiza treinamento

### 7.3 Oportunidades de Melhoria
1. **Atualização temporal:** Incorporar dados mais recentes
2. **Diversificação:** Incluir outras plataformas além do Twitter
3. **Granularidade:** Adicionar classificação de intensidade emocional
4. **Contexto:** Preservar informações como emoticons e formatação

---

## 📋 8. Recomendações Técnicas

### 8.1 Para Pré-processamento
- ✅ **Manter limpeza atual:** Remoção de URLs e menções é adequada
- ⚠️ **Considerar preservar:** Alguns emoticons podem ser informativos
- 🔄 **Normalização:** Padronizar contrações ("dont" → "don't")

### 8.2 Para Feature Engineering
- **Comprimento do texto:** Feature preditiva relevante
- **Contagem de palavras:** Diferenciação clara entre classes
- **Densidade de palavras negativas:** Pode melhorar performance
- **Ratios de pontuação:** Exclamações podem indicar intensidade

### 8.3 Para Validação
- **Estratificação:** Manter proporção 50/50 em train/test
- **Temporal:** Considerar divisão cronológica para validação
- **Usuários:** Evitar vazamento por usuários específicos

---

## 🏆 9. Conclusões da Análise Exploratória

### 9.1 Qualidade do Dataset
O **Sentiment140** demonstrou ser um dataset de **excelente qualidade** para análise de sentimentos:
- ✅ Completude total dos dados
- ✅ Balanceamento perfeito das classes
- ✅ Diversidade adequada de usuários e conteúdo
- ✅ Padrões linguísticos claros e diferenciados

### 9.2 Viabilidade para Machine Learning
O dataset apresenta **características ideais** para treinamento de modelos:
- **Diferenciação vocabular clara** facilita classificação
- **Ausência de ruído** otimiza processo de aprendizado
- **Volume adequado** (1.6M) permite treinar modelos complexos
- **Balanceamento** evita bias para classes específicas

### 9.3 Limitações e Considerações
- **Contexto temporal:** Dados de 2009 podem limitar aplicabilidade atual
- **Ausência de neutralidade:** Limita detecção de sentimentos ambíguos
- **Domínio específico:** Focado em redes sociais

### 9.4 Potencial de Aplicação
Com base na análise, o dataset é **altamente adequado** para:
- 🎯 Desenvolvimento de classificadores binários de sentimento
- 🎯 Estudos de padrões linguísticos em redes sociais
- 🎯 Benchmarking de modelos de NLP
- 🎯 Análise de comportamento textual por sentimento

---

## 📈 10. Próximos Passos Recomendados

### 10.1 Aprofundamento da Análise
1. **Análise temporal:** Padrões de sentimento ao longo do tempo
2. **Análise de usuários:** Comportamento individual vs. coletivo
3. **N-gramas:** Identificar frases características
4. **Clustering:** Descobrir sub-categorias dentro dos sentimentos

### 10.2 Preparação para Modelagem
1. **Divisão estratificada:** Train/validation/test mantendo proporções
2. **Tokenização avançada:** Considerar modelos baseados em BERT
3. **Augmentation:** Técnicas para aumentar diversidade se necessário
4. **Benchmark:** Estabelecer baseline com modelos simples

---

*Análise realizada em: 14 de Agosto de 2025*  
*Notebook analisado: `analise_exploratoria.ipynb`*  
*Dataset: Sentiment140 (1.6M tweets)*  
*Metodologia: Análise exploratória estatística e visual*
