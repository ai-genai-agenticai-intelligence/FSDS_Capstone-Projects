# Natural Language Processing
'''Customer review feedback Project
--how ML technique impliment in nlp '''


# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv(r'D:\AI NLP -NATURAL LANGUAGE PROCESSING DATA\Restaurant_Reviews.tsv', delimiter = '\t', quoting = 3)

# Cleaning the texts
import re 
import nltk
#nltk.download('stopwords')
from nltk.corpus import stopwords 
from nltk.stem.porter import PorterStemmer

corpus = []  

for i in range(0, 1000):
    review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)



# Creating the Bag of Words model
from sklearn.feature_extraction.text import TfidfVectorizer
cv = TfidfVectorizer(max_features=1500,ngram_range=(1,2),min_df=2,max_df=0.8 )
X = cv.fit_transform(corpus).toarray()

y = dataset.iloc[:, 1].values


''' Convert from nlp technique to number'''


# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)



''' IMPLIOMENT ALL CLASSIFICATION ALGORTHIM
------------------------------------------------->>>>>>>>>>>>>>>>>>>>>>
'''


'''
from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier()
classifier.fit(X_train, y_train) 
'''


from sklearn.linear_model import LogisticRegression
classifier =LogisticRegression(C=1.0,solver='lbfgs',max_iter=100,penalty='l2',intercept_scaling=1)
classifier.fit(X_train,y_train)


'''
from sklearn.neighbors import KNeighborsClassifier
classifier =KNeighborsClassifier(n_neighbors=4,p=1)
classifier.fit(X_train ,y_train)
'''

'''
from sklearn.svm import SVC
classifier=SVC(C=1.0, kernel="rbf", degree=3, gamma="scale", coef0=0.0)
classifier.fit(X_train, y_train)
'''

'''
# it is give a correct model
from sklearn.ensemble import RandomForestClassifier
classifier =RandomForestClassifier(max_depth=2, n_estimators=60, random_state=0,criterion='entropy')
classifier.fit(X_train,y_train)
'''

'''
from xgboost import XGBClassifier
classifier =XGBClassifier(random_state=0)
classifier.fit(X_train ,y_train)
'''
'''
from lightgbm import LGBMClassifier
classifier = LGBMClassifier(random_state=0)
classifier.fit(X_train, y_train)
'''



'''
from sklearn.naive_bayes import GaussianNB
classifier =GaussianNB()
classifier.fit(X_train, y_train)
'''
'''
#it will give correct model
from sklearn.naive_bayes import BernoulliNB
classifier =BernoulliNB()
classifier.fit(X_train, y_train)
'''
'''
from sklearn.naive_bayes import MultinomialNB
classifier =MultinomialNB()
classifier.fit(X_train, y_train)
'''

# Predicting the Test set results
y_pred = classifier.predict(X_test)


#Making a Confusion Matrix
from sklearn.metrics import confusion_matrix
cm= confusion_matrix(y_pred,y_test)
print(cm)

#Accurecy
from sklearn.metrics import accuracy_score
ac =accuracy_score(y_pred,y_test)
print(ac)

bias =classifier.score(X_train,y_train)
bias

variance =classifier.score(X_test,y_test)
variance


#AUC/ROC-------------------------
from sklearn.metrics import roc_auc_score ,roc_curve
y_pred_prob = classifier.predict_proba(X_test)[:,1]

auc_score =roc_auc_score(y_test,y_pred_prob)
auc_score

fpr ,tpr,thershold =roc_curve(y_test ,y_pred_prob)


#AUC/ROC CURVE LOGISTIC REGRESSION-------------
plt.figure(figsize=(8,6))
plt.plot(fpr, tpr, label=f'Logistic Regression (AUC = {auc_score:.2f})')
plt.plot([0,1], [0,1], 'k--')  # Random line
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend(loc='lower right')
plt.grid()
plt.show()

'''
#RANDOM FOREST CLASSIFICATION--------------
#Visualising the Training set results
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

X_set, y_set = X_train, y_train

# Create meshgrid
X1, X2 = np.meshgrid(
    np.arange(start=X_set[:, 0].min() - 1, stop=X_set[:, 0].max() + 1, step=0.01),
    np.arange(start=X_set[:, 1].min() - 1, stop=X_set[:, 1].max() + 1, step=0.01)
)

# Predict on grid
Z = classifier.predict(np.c_[X1.ravel(), X2.ravel()])
Z = Z.reshape(X1.shape)

# Plot decision boundary
plt.contourf(X1, X2, Z, alpha=0.75, cmap=ListedColormap(('red', 'green')))

# Set limits
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())

# Plot points
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(
        X_set[y_set == j, 0],
        X_set[y_set == j, 1],
        color=ListedColormap(('red', 'green'))(i),  # ✅ FIX: use 'color' not 'c'
        label=j
    )

# Labels
plt.title('Random Forest Classification (Training set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()
'''

