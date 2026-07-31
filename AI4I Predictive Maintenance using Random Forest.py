#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 


# In[2]:


df = pd.read_csv(r"C:\Users\ARIO\Documents\for IK saber\AI4I\ai4i2020.csv")
df.head()


# In[3]:


df.shape


# In[4]:


df.isnull().sum()


# In[5]:


df['Machine failure'].value_counts()


# In[6]:


df[['TWF','HDF','PWF','OSF','RNF']].sum()


# In[7]:


df[['TWF','HDF','PWF','OSF','RNF']].sum(axis=1).value_counts()


# In[8]:


df['failure_count'] = df[['TWF','HDF','PWF','OSF','RNF']].sum(axis=1)

cdf = df[df['failure_count']<= 1].copy()
print(cdf.shape)
cdf.head()


# In[9]:


def get_failure_type (row) : 
    if row ['TWF'] == 1 :
        return 'TWF'
    elif  row ['HDF'] == 1 : 
        return 'HDF'
    elif  row ['PWF'] == 1 : 
        return 'PWF'
    elif row ['OSF']  == 1: 
        return 'OSF'
    elif row ['RNF'] ==1 : 
        return 'RNF'
    else : 
        return 'Healthy'

cdf['failure_type']  =  cdf.apply(get_failure_type,axis=1)
cdf['failure_type'].value_counts()


# In[10]:


cdf.head()


# In[11]:


from sklearn.preprocessing import LabelEncoder 

le_type = LabelEncoder()
cdf['type_encoded'] = le_type.fit_transform(cdf['Type'])


# In[12]:


le_failure = LabelEncoder() 
cdf['failure_encoded'] = le_failure.fit_transform(cdf['failure_type'])


# In[13]:


cdf.head()


# In[14]:


ncdf = cdf.drop(columns=['UDI', 'Product ID', 'Type', 'Machine failure', 'TWF', 'HDF', 'PWF', 'OSF', 'RNF', 'failure_count'])
ncdf.head()


# In[19]:


features = ['type_encoded', 'Air temperature [K]', 'Process temperature [K]', 
            'Rotational speed [rpm]', 'Torque [Nm]', 'Tool wear [min]']

x = cdf[features]
y = cdf['failure_encoded']

print(x.shape)
print(y.shape)


# In[22]:


from sklearn.model_selection import train_test_split

x_train , x_test , y_train , y_test = train_test_split(x,y,test_size=0.2,random_state=42, stratify=y)
print(x_test.shape , x_train.shape)


# In[23]:


from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=100,random_state=42,class_weight='balanced')
model.fit(x_train,y_train)


# In[24]:


from sklearn.metrics import classification_report , confusion_matrix

y_hat = model.predict(x_test)

report = classification_report(y_test,y_hat , target_names=le_failure.classes_)
print(report)


# In[26]:


from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

cm = confusion_matrix(y_test, y_hat)

plt.figure(figsize=(8,6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=le_failure.classes_,
            yticklabels=le_failure.classes_)
plt.xlabel(' (Predicted)')
plt.ylabel( '(Actual)')
plt.title('Confusion Matrix')
plt.show()


# In[30]:


from imblearn.over_sampling import SMOTE

smote = SMOTE(random_state=42, k_neighbors=3)
X_train_balanced, y_train_balanced = smote.fit_resample(x_train, y_train)

print("befor SMOTE:", y_train.value_counts().to_dict())
print (" after SMOTE:", y_train_balanced.value_counts().to_dict())


# In[32]:


model_balanced = RandomForestClassifier(n_estimators=100, random_state=42)
model_balanced.fit(X_train_balanced, y_train_balanced)

y_hat_balanced = model_balanced.predict(x_test)

print(classification_report(y_test, y_hat_balanced, target_names=le_failure.classes_))


# In[ ]:




