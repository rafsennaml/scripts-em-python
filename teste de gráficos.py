import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df=pd.read_csv('bola1.csv', sep=';')



#print(df['Bola1'].value_counts(normalize=True))
labels1 = df['Bola1'].value_counts().index
values1 = df['Bola1'].value_counts().values
fig, axes = plt.subplots(3, 5, figsize=(16, 8))
axes = axes.flatten()
sns.barplot(x=labels1, y=values1, ax=axes[0])
axes[0].set_title('Freq. no sorteio da Bola 1')
axes[0].set_xlabel('Números')    
axes[0].set_ylabel('Frequência')
#fig.add_subplot(211)

#print(df['Bola2'].value_counts())
#print(df['Bola2'].value_counts(normalize=True))
labels2= df['Bola2'].value_counts().index
values2 = df['Bola2'].value_counts().values
sns.barplot(x=labels2, y=values2, ax=axes[1])
axes[1].set_title('Freq. no sorteio da Bola 2')
axes[1].set_xlabel('Números')    
axes[1].set_ylabel('Frequência')
#fig.add_subplot(212)


#print(df['ano'].value_counts())
#print(df['ano'].value_counts(normalize=True))

#print(df['Ganhadores'].value_counts())
#print(df['Ganhadores'].value_counts(normalize=True))

#print(df['Bola3'].value_counts())
#print(df['Bola3'].value_counts(normalize=True))
labels3= df['Bola3'].value_counts().index
values3 = df['Bola3'].value_counts().values
sns.barplot(x=labels3, y=values3, ax=axes[2])
axes[2].set_title('Freq. no sorteio da Bola 3')
axes[2].set_xlabel('Números')    
axes[2].set_ylabel('Frequência')
#axes[2].set_ylabel('Frequência')

#print(df['Bola4'].value_counts())
#print(df['Bola4'].value_counts(normalize=True))
labels4= df['Bola4'].value_counts().index
values4 = df['Bola4'].value_counts().values
sns.barplot(x=labels4, y=values4, ax=axes[3])
axes[3].set_title('Freq. no sorteio da Bola 4')
axes[3].set_xlabel('Números')    
axes[3].set_ylabel('Frequência')
#axes[3].set_ylabel('Frequência')
#axes[3].set_ylabel('Frequência')



#print(df['Bola5'].value_counts())
#print(df['Bola5'].value_counts(normalize=True))

labels5= df['Bola5'].value_counts().index
values5 = df['Bola5'].value_counts().values
sns.barplot(x=labels5, y=values5, ax=axes[4])
axes[4].set_title('Freq. no sorteio da Bola 5')
axes[4].set_xlabel('Números')    
axes[4].set_ylabel('Frequência')
#axes[4].set_ylabel('Frequência')


#print(df['Bola6'].value_counts())
#print(df['Bola6'].value_counts(normalize=True))
labels6= df['Bola6'].value_counts().index
values6 = df['Bola6'].value_counts().values
sns.barplot(x=labels5, y=values5, ax=axes[5])
axes[5].set_title('Freq. no sorteio da Bola 6')
axes[5].set_xlabel('Números')    
axes[5].set_ylabel('Frequência')
#axes[5].set_ylabel('Frequência')

#print(df['Bola7'].value_counts())
#print(df['Bola7'].value_counts(normalize=True))
labels6= df['Bola7'].value_counts().index
values6 = df['Bola7'].value_counts().values
sns.barplot(x=labels6, y=values6, ax=axes[6])
axes[6].set_title('Freq. no sorteio da Bola 7')
axes[6].set_xlabel('Números')    
axes[6].set_ylabel('Frequência')

#print(df['Bola8'].value_counts())
#print(df['Bola8'].value_counts(normalize=True))
labels6= df['Bola8'].value_counts().index
values6 = df['Bola8'].value_counts().values
sns.barplot(x=labels6, y=values6, ax=axes[7])
axes[7].set_title('Freq. no sorteio da Bola 8')
axes[7].set_xlabel('Números')    
axes[7].set_ylabel('Frequência')

#print(df['Bola9'].value_counts())
#print(df['Bola9'].value_counts(normalize=True))
labels7= df['Bola9'].value_counts().index
values7 = df['Bola9'].value_counts().values
sns.barplot(x=labels7, y=values7, ax=axes[8])
axes[8].set_title('Freq. no sorteio da Bola 9')
axes[8].set_xlabel('Números')    
axes[8].set_ylabel('Frequência')

#print(df['Bola10'].value_counts())
#print(df['Bola10'].value_counts(normalize=True))
labels8= df['Bola10'].value_counts().index
values8 = df['Bola10'].value_counts().values
sns.barplot(x=labels8, y=values8, ax=axes[9])
axes[9].set_title('Freq. no sorteio da Bola 10')
axes[9].set_xlabel('Números')    
axes[9].set_ylabel('Frequência')

#print(df['Bola11'].value_counts())
#print(df['Bola11'].value_counts(normalize=True))
labels9= df['Bola11'].value_counts().index
values9 = df['Bola11'].value_counts().values
sns.barplot(x=labels9, y=values9, ax=axes[10])
axes[10].set_title('Freq. no sorteio da Bola 11')
axes[10].set_xlabel('Números')    
axes[10].set_ylabel('Frequência')


#print(df['Bola12'].value_counts())
#print(df['Bola12'].value_counts(normalize=True))
labels10= df['Bola12'].value_counts().index
values10 = df['Bola12'].value_counts().values
sns.barplot(x=labels10, y=values10, ax=axes[11])
axes[11].set_title('Freq. no sorteio da Bola 12')
axes[11].set_xlabel('Números')    
axes[11].set_ylabel('Frequência')

#print(df['Bola13'].value_counts())
#print(df['Bola13'].value_counts(normalize=True))
labels11= df['Bola13'].value_counts().index
values11 = df['Bola13'].value_counts().values
sns.barplot(x=labels11, y=values11, ax=axes[12])
axes[12].set_title('Freq. no sorteio da Bola 13')
axes[12].set_xlabel('Números')    
axes[12].set_ylabel('Frequência')

#print(df['Bola14'].value_counts())
#print(df['Bola14'].value_counts(normalize=True))
labels12= df['Bola14'].value_counts().index
values12 = df['Bola14'].value_counts().values
sns.barplot(x=labels12, y=values12, ax=axes[13])
axes[13].set_title('Freq. no sorteio da Bola 14')
axes[13].set_xlabel('Números')    
axes[13].set_ylabel('Frequência')

#print(df['Bola15'].value_counts())
#print(df['Bola15'].value_counts(normalize=True))
labels13= df['Bola15'].value_counts().index
values13 = df['Bola15'].value_counts().values
sns.barplot(x=labels13, y=values13, ax=axes[14])
axes[14].set_title('Freq. no sorteio da Bola 15')
axes[14].set_xlabel('Números')    
axes[14].set_ylabel('Frequência')

plt.tight_layout()
plt.show()