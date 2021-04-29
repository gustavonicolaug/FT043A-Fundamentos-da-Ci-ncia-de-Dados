"""
FT043 - Fundamentos da Ciencias de Dados
Exemplos VAs conjuntas
"""

# Importanto pacotes
import matplotlib.pyplot as plt
import numpy as np


# Definicao de uma VA com distribuicao f_X
x = np.array([(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2),(2, 0), (2, 1), (2, 2)])
X1 = np.array([0,1,2])
X2 = np.array([0,1,2])
f_X = np.array([0, 0.25, 0, 0.25, 0, 0.25, 0, 0.25, 0])
 
def sample_fx(x,f_X,n_samples): # Funcao para realizacao da variavel X
    size_support = f_X.size
    aux_support = np.arange(size_support)
    samples_X = np.zeros((1,2))
    ii = 0
    while  ii < n_samples:
        aux_sample = np.random.choice(aux_support, 1, p=list(f_X))
        array_sample = x[aux_sample]
        samples_X = np.vstack((samples_X,array_sample))
        ii+=1        
    samples_X = np.delete(samples_X, (0), axis=0)
    return samples_X
     

5, 15, 100, 500

# Gerando os dados para cada quantidade de amostras

dados_5 = sample_fx(x,f_X,5)
dados_15 = sample_fx(x,f_X,15)
dados_100 = sample_fx(x,f_X,100)
dados_500 = sample_fx(x,f_X,500)

print("Questão 2:")

#(a)Obtenha as distribuições marginais das variáveis X1 e X2.

plt.figure(1)
freq_rel_5 = np.array([np.count_nonzero(dados_5[:,0] == 0),np.count_nonzero(dados_5[:,0] == 1),np.count_nonzero(dados_5[:,0] == 2)])/5
plt.stem(X1, freq_rel_5)
plt.title('Distribuicao Marginal X1 para N=5',fontsize=15)
plt.xlabel('x',fontsize=15)
plt.ylabel('f(x)',fontsize=15)

plt.figure(2)
freq_rel_5 = np.array([np.count_nonzero(dados_5[:,1] == 0),np.count_nonzero(dados_5[:,1] == 1),np.count_nonzero(dados_5[:,1] == 2)])/5
plt.stem(X1, freq_rel_5)
plt.title('Distribuicao Marginal X2 para N=5',fontsize=15)
plt.xlabel('x',fontsize=15)
plt.ylabel('f(x)',fontsize=15)
plt.figure(3)
freq_rel_15 = np.array([np.count_nonzero(dados_15[:,0] == 0),np.count_nonzero(dados_15[:,0] == 1),np.count_nonzero(dados_15[:,0] == 2)])/15
plt.stem(X1, freq_rel_15)
plt.title('Distribuicao Marginal X1 para N=15',fontsize=15)
plt.xlabel('x',fontsize=15)
plt.ylabel('f(x)',fontsize=15)

plt.figure(4)
freq_rel_15 = np.array([np.count_nonzero(dados_15[:,1] == 0),np.count_nonzero(dados_15[:,1] == 1),np.count_nonzero(dados_15[:,1] == 2)])/15
plt.stem(X1, freq_rel_15)
plt.title('Distribuicao Marginal X2 para N=15',fontsize=15)
plt.xlabel('x',fontsize=15)
plt.ylabel('f(x)',fontsize=15)

plt.figure(5)
freq_rel_100 = np.array([np.count_nonzero(dados_100[:,0] == 0),np.count_nonzero(dados_100[:,0] == 1),np.count_nonzero(dados_100[:,0] == 2)])/100
plt.stem(X1, freq_rel_100)
plt.title('Distribuicao Marginal X1 para N=100',fontsize=15)
plt.xlabel('x',fontsize=15)
plt.ylabel('f(x)',fontsize=15)

plt.figure(6)
freq_rel_100 = np.array([np.count_nonzero(dados_100[:,1] == 0),np.count_nonzero(dados_100[:,1] == 1),np.count_nonzero(dados_100[:,1] == 2)])/100
plt.stem(X1, freq_rel_100)
plt.title('Distribuicao Marginal X2 para N=100',fontsize=15)
plt.xlabel('x',fontsize=15)
plt.ylabel('f(x)',fontsize=15)

plt.figure(7)
freq_rel_500 = np.array([np.count_nonzero(dados_500[:,0] == 0),np.count_nonzero(dados_500[:,0] == 1),np.count_nonzero(dados_500[:,0] == 2)])/500
plt.stem(X1, freq_rel_500)
plt.title('Distribuicao Marginal X1 para N=500',fontsize=15)
plt.xlabel('x',fontsize=15)
plt.ylabel('f(x)',fontsize=15)

plt.figure(8)
freq_rel_500 = np.array([np.count_nonzero(dados_500[:,1] == 0),np.count_nonzero(dados_500[:,1] == 1),np.count_nonzero(dados_500[:,1] == 2)])/500
plt.stem(X1, freq_rel_500)
plt.title('Distribuicao Marginal X2 para N=500',fontsize=15)
plt.xlabel('x',fontsize=15)
plt.ylabel('f(x)',fontsize=15)

plt.show()

#(b) Calcule P(X1 > X2).

freq_X1_maior_X2_5 = np.count_nonzero(dados_5 [:,0]>dados_5[:,1])/5
freq_X1_maior_X2_15 = np.count_nonzero(dados_15 [:,0]>dados_15[:,1])/15
freq_X1_maior_X2_100 = np.count_nonzero(dados_100 [:,0]>dados_100[:,1])/100
freq_X1_maior_X2_500 = np.count_nonzero(dados_500 [:,0]>dados_500[:,1])/500

print("Item b")
print("Frequência em que X1 > X2 (N=5)= ",freq_X1_maior_X2_5)
print("Frequência em que X1 > X2 (N=15)= ",freq_X1_maior_X2_15)
print("Frequência em que X1 > X2 (N=100)= ",freq_X1_maior_X2_100)
print("Frequência em que X1 > X2 (N=500)= ",freq_X1_maior_X2_500)
print("\n")
"""
"""

#(c) Calcule E{X1} e E{X2}.

X_mean_5 = dados_5.mean(axis=0) 
X_mean_15 = dados_15.mean(axis=0) 
X_mean_100 = dados_100.mean(axis=0) 
X_mean_500 = dados_500.mean(axis=0) 

print("Item c")
print("Média X1 e X2 (N=5) = ",X_mean_5)
print("Média X1 e X2 (N=15) = ",X_mean_15)
print("Média X1 e X2 (N=100) = ",X_mean_100)
print("Média X1 e X2 (N=500) = ",X_mean_500)
print("\n")
#(d) Calcule o desvio padrão das variáveis X1 e X2.

X_std_5 = dados_5.std(axis=0)
X_std_15 = dados_15.std(axis=0)
X_std_100 = dados_100.std(axis=0)
X_std_500 = dados_500.std(axis=0)

print("Item d")
print("Desvio Padrão X1 e X2 (N=5) = ",X_std_5)
print("Desvio Padrão X1 e X2 (N=15) = ",X_std_15)
print("Desvio Padrão X1 e X2 (N=100) = ",X_std_100)
print("Desvio Padrão X1 e X2 (N=500) = ",X_std_500)
print("\n")

#(e) Calcule o coeficiente de correlação entre as X1 e X2.

X_corrcoef_5 = np.corrcoef(dados_5.T)[0][1]
X_corrcoef_15 = np.corrcoef(dados_15.T)[0][1]
X_corrcoef_100 = np.corrcoef(dados_100.T)[0][1]
X_corrcoef_500 = np.corrcoef(dados_500.T)[0][1]

print("Item e ")
print ("Coeficiente de Correlação X1 e X2 (N=5) = ", X_corrcoef_5);
print ("Coeficiente de Correlação X1 e X2 (N=15) = ", X_corrcoef_15);
print ("Coeficiente de Correlação X1 e X2 (N=100) = ", X_corrcoef_100);
print ("Coeficiente de Correlação X1 e X2 (N=500) = ", X_corrcoef_500);
print("\n")

#(f) Verifique se as variáveis X1 e X2 são estatisticamente independentes.

print("Item f ")
print("Será verificado se F(1,1) = Fx1(1).Fx2(1), assim como calculado na parte teórica \n")

freq_11_5 = sum(np.all(dados_5 == [1,1],axis=1))/5
freq_x1_x1_5 = np.count_nonzero(dados_5 [:,0]==1)/5 * np.count_nonzero(dados_5[:,1]==1)/5

freq_11_15 = sum(np.all(dados_15 == [1,1],axis=1))/15
freq_x1_x1_15 = np.count_nonzero(dados_15 [:,0]==1)/15 * np.count_nonzero(dados_15[:,1]==1)/15

freq_11_100 = sum(np.all(dados_100 == [1,1],axis=1))/100
freq_x1_x1_100 = np.count_nonzero(dados_100[:,0]==1)/100 * np.count_nonzero(dados_100[:,1]==1)/100

freq_11_500 = sum(np.all(dados_500 == [1,1],axis=1))/500
freq_x1_x1_500 = np.count_nonzero(dados_500 [:,0]==1)/500 * np.count_nonzero(dados_500[:,1]==1)/500

print("(N=5) F(1,1) =",freq_11_5, "; Fx1(1).Fx2(1) = ", freq_x1_x1_5)
print("(N=15) F(1,1) =",freq_11_15, "; Fx1(1).Fx2(1) = ", freq_x1_x1_15)
print("(N=100) F(1,1) =",freq_11_100, "; Fx1(1).Fx2(1) = ", freq_x1_x1_100)
print("(N=500) F(1,1) =",freq_11_500, "; Fx1(1).Fx2(1) = ", freq_x1_x1_500)
"""
print ("Coeficiente de Correlação X1 e X2 (N=5) = ", X_corrcoef_5);
print ("Coeficiente de Correlação X1 e X2 (N=15) = ", X_corrcoef_15);
print ("Coeficiente de Correlação X1 e X2 (N=100) = ", X_corrcoef_100);
print ("Coeficiente de Correlação X1 e X2 (N=500) = ", X_corrcoef_500);
print("\n")
"""
#(g) Verifique se as variáveis X1 e X2 são descorrelacionadas.


#X_mean = dados.mean(axis=0) # Calculo da media
#X_std = dados.std(axis=0) # Calculo do desvio padrao
#X_cov = np.cov(dados.T) # Calculo da matriz de covariancia
#X_corrcoef = np.corrcoef(dados.T) # Calculo da matriz de correlacao
