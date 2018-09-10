import pandas as pd
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split

df=pd.read_csv("D:\\PROJECTS\\Python\\DrAIvex project 2(Titanic-Death-count)\\train.csv")

mean=df['Age'].mean()

df['Age'].fillna(mean,inplace=True)


Pclass=pd.get_dummies(df['Pclass'])
Sex=pd.get_dummies(df['Sex'])
Age=pd.get_dummies(df['Age'])

df=pd.concat([df,Pclass,Sex,Age],axis=1)
df.drop(['PassengerId','Sex','Age','Pclass','Name','Ticket','Cabin','SibSp','Parch','Fare','Embarked'],axis=1,inplace=True)
print(df.head(3))
'''
#print(df.head(3))
df.drop(['PassengerId','Name','Ticket','Cabin','SibSp','Parch','Fare','Embarked'],axis=1,inplace=True)
print(df.head(3))




x=df.drop('Survived',axis=1)
y=df['Survived']

x_train,x_test,y_train,y_test=train_test_split(x, y, test_size=0.2, random_state=0)
reg=LogisticRegression()
reg.fit(x_train,y_train)
pred=reg.predict(x_test)
print(pred)'''