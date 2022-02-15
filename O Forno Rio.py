#!/usr/bin/env python
# coding: utf-8

# In[30]:


import pandas as pd

vendas_periodo_df = pd.read_csv(r'C:\Users\USER\Downloads\Vendas Realizadas no Período.csv')
ficha_tecnica = pd.read_csv(r'C:\Users\USER\Downloads\Composição do Produto por Loja (Indexada).csv')
##tempo_21 = pd.read_csv(r'C:\Users\USER\Downloads\INMET_SE_RJ_A652_RIO DE JANEIRO - FORTE DE COPACABANA_01-01-2021_A_31-12-2021.csv')
##tempo_22 = pd.read_csv(r'C:\Users\USER\Downloads\INMET_SE_RJ_A652_RIO DE JANEIRO - FORTE DE COPACABANA_01-01-2022_A_31-01-2022.csv')

display(vendas_periodo_df)
display(ficha_tecnica)
##display(tempo_21)
##display(tempo_22)


# In[25]:


#Separar coluna vendas_periodo_df LABELVENDARECEBIMENTO


# In[ ]:


#mostrar produtos mais vendidos por dia da semana (excluir bebidas, sobremesas, bordas e massas)


# In[ ]:


#mostrar produtos mais vendidos por horário vendas_periodo_df (excluir bebidas, sobremesas, bordas e massas)


# In[ ]:


#mostrar qual a combinação de pizza meio a meio mais pedida (excluir bebidas, sobremesas, bordas e massas)


# In[ ]:


#calcular previsão de consumo baseado nas vendas ultiplicando com os valores na ficha técnica

