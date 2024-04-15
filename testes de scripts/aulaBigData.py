import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
'''
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
'''
#carregando os dados do arquivo json
df = pd.read_json('dados_saude_mockaroo.json')
#pre processamento dos dados
#df['dob'] = pd.to_datetime(df['dob'])
#df.ffill()
plt.figure(figsize=(10, 6))
sns.countplot(x='medications', data=df, color='#007CDB')
plt.ylabel('quantidade')
plt.show()
'''
#mineração de dados
scaler = StandardScaler()
df_scaler = scaler.fit_transform(df[['height', 'weight', 'blood_pressure', 'heart_rate']])
pca = PCA(n_components=2)
df_pca = pca.fit_transform(df_scaler)
kmeans = KMeans(n_clusters=5)
df['clusters'] = kmeans.fit_predict(df_pca)
#avaliação
print(df['clusters'].value_counts())
#visualizar os clusters gerados com um gráfico
plt.scatter(df_pca[:,0], df_pca[:, 1], c=df['clusters'])
plt.xlabel('PCA1')
plt.ylabel('PCA2')
plt.title('Cluster de pacientes')
plt.show()
'''
#TebsorFlow é para aprendizado de máquina e na próxima aula veremos ele, é uma lib
'''
!pip install Scikit-learn
!pip install Seaborn
!pip install matplotlib
!pip install NumPy
!pip install pandas

*************
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

#carregando os dados do arquivo json
df = pd.read_json('dados_saude_mockaroo.json')

#pre processamento dos dados
df['dob'] = pd.to_datetime(df['dob'])
df.fillna(method='ffill', inplace=True)


plt.figure(figsize=(10, 6))
sns.countplot(x='diagnosis', data=df)
plt.show

******************

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

#carregando os dados do arquivo json
df = pd.read_json('dados_saude_mockaroo.json')

#pre processamento dos dados
df['dob'] = pd.to_datetime(df['dob'])
df.fillna(method='ffill', inplace=True)


plt.figure(figsize=(10, 6))
sns.countplot(x='diagnosis', data=df)
plt.show()

#mineração de dados

scaler = StandardScaler()
df_scaler = scaler.fit_transform(df[['height', 'weight', 'blood_pressure', 'heart_rate']])

pca = PCA(n_components=2)
df_pca = pca.fit_transform(df_scaler)

kmeans = KMeans(n_clusters=5)
df['clusters'] = kmeans.fit_predict(df_pca)

#avaliação
print(df['clusters'].value_counts())

#visualizar os clusters gerados com um gráfico
plt.scatter(df_pca[:,0], df_pca[:, 1], c=df['clusters'])
plt.xlabel('PCA1')
plt.ylabel('PCA2')
plt.title('Cluster de pacientes')
plt.show()
'''