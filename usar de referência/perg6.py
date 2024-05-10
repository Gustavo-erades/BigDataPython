
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from textblob import TextBlob
import matplotlib.pyplot as plt

# Suponha que 'respostas' seja uma lista de respostas à pergunta
respostas = ["Sim, tive uma experiência ruim com o atendimento na recepção.",
             "Não, nunca tive problemas com meu consultório odontológico.",
             "Sim, o dentista anterior não era muito cuidadoso e eu me sentia desconfortável durante os procedimentos."]

# Pré-processamento
stop_words = set(stopwords.words('portuguese'))
tfidf_vectorizer = TfidfVectorizer(stop_words=stop_words)
tfidf = tfidf_vectorizer.fit_transform(respostas)

# Modelagem de tópicos usando LDA
lda_model = LatentDirichletAllocation(n_components=2, random_state=42)
lda_model.fit(tfidf)

# Análise de sentimento e atribuição de rótulos
sentimentos = []
for resposta in respostas:
    blob = TextBlob(resposta)
    sentimento = blob.sentiment.polarity
    if sentimento > 0:
        sentimentos.append('Positivo')
    elif sentimento < 0:
        sentimentos.append('Negativo')
    else:
        sentimentos.append('Neutro')

# Visualização
df = pd.DataFrame({'Respostas': respostas, 'Tópico': lda_model.transform(tfidf).argmax(axis=1), 'Sentimento': sentimentos})
plt.figure(figsize=(10, 6))
plt.hist(df['Tópico'], bins=range(3), alpha=0.5, color='blue', label='Tópicos')
plt.hist(df['Sentimento'].map({'Positivo': 0, 'Negativo': 1, 'Neutro': 2}), bins=range(4), alpha=0.5, color='red', label='Sentimento')
plt.xlabel('Categoria')
plt.ylabel('Contagem')
plt.xticks(range(3), ['Tópico 0', 'Tópico 1', 'Sentimento'])
plt.legend()
plt.title('Análise de Respostas Não Objetivas')
plt.show()
