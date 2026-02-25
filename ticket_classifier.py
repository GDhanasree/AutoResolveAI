import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("data/tickets.csv")

X = df["ticket_text"]
y = df["label"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Vectorize
vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train
model = LogisticRegression()
model.fit(X_train_vec, y_train)

# Evaluate
y_pred = model.predict(X_test_vec)
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)

# Save
joblib.dump(model, "models/classifier.pkl")
joblib.dump(vectorizer, "models/vectorizer.pkl")


# import pandas as pd
# import joblib
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.linear_model import LogisticRegression
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score, classification_report

# # Load dataset
# df = pd.read_csv("data/tickets.csv")

# X = df["ticket_text"]
# y = df["label"]

# # Stratified split (better practice)
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y,
#     test_size=0.2,
#     random_state=42,
#     stratify=y
# )

# # Better vectorizer
# vectorizer = TfidfVectorizer(
#     ngram_range=(1, 2),
#     max_features=5000,
#     stop_words="english"
# )

# X_train_vec = vectorizer.fit_transform(X_train)
# X_test_vec = vectorizer.transform(X_test)

# # Logistic Regression with better config
# model = LogisticRegression(max_iter=1000)
# model.fit(X_train_vec, y_train)

# # Evaluate
# y_pred = model.predict(X_test_vec)
# accuracy = accuracy_score(y_test, y_pred)

# print("Accuracy:", accuracy)
# print("\nClassification Report:\n")
# print(classification_report(y_test, y_pred))

# # Save model
# joblib.dump(model, "models/classifier.pkl")
# joblib.dump(vectorizer, "models/vectorizer.pkl")

# print("\nModel saved successfully.")