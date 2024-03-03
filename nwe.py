import numpy as np 
import pandas as pd
interns = pd.read_csv("internship.csv")
interns.head(2)
interns.shape
interns.iloc[0]['company_name']
file_path = 'input1.txt'  # Provide the path to your text file
try:
    with open(file_path, 'r') as file:
        # Read the entire contents of the file
        content = file.read()
        
        # Process the content as per your requirements
        
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
import nltk
from nltk.stem import PorterStemmer
ps = PorterStemmer()
def stems(text):
    T = []
    
    for i in text.split():
        T.append(ps.stem(i))
    
    return " ".join(T)
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=5000,stop_words='english')
interns['tags']=interns['internship_title']+interns['company_name']+interns['location']+interns['start_date']+interns['duration']+interns['stipend']
vector = cv.fit_transform(interns['tags']).toarray()
vector[0]
vector.shape
from sklearn.metrics.pairwise import cosine_similarity
similarity = cosine_similarity(vector)
interns[interns['internship_title'] == 'Accounting and Finance'].index[0]
L = []

def recommend(internship):
    index = interns[interns['internship_title'] == internship].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x:x[1])

    for i in distances[1:6]:
        L.append(interns.iloc[i[0]])

    return L
a = content
L2=recommend(a)
print(L2)
import pickle
pickle.dump(interns,open('internships_1.pkl','wb'))
pickle.dump(similarity,open('similarity.pkl','wb'))
def write_details_to_file(file_name, details):
    with open(file_name, 'w', encoding='utf-8') as file:
        for key, value in details.items():
            file.write(f"{key}:{value}\n")

write_details_to_file(r'C:\Users\laptop2\ok\static\out11.txt', {
    'internship_title':L2[0]['internship_title'],
    'company_name':L2[0]['company_name'],
    'location':L2[0]['location'],
    'start_date':L2[0]['start_date'],
    'duration':L2[0]['duration'],
    'stipend':L2[0]['stipend'],
    'tags':L2[0]['tags']
})

write_details_to_file(r'C:\Users\laptop2\ok\static\out12.txt', {
    'internship_title':L2[1]['internship_title'],
    'company_name':L2[1]['company_name'],
    'location':L2[1]['location'],
    'start_date':L2[1]['start_date'],
    'duration':L2[1]['duration'],
    'stipend':L2[1]['stipend'],
    'tags':L2[1]['tags']
})

write_details_to_file(r'C:\Users\laptop2\ok\static\out13.txt', {
    'internship_title':L2[2]['internship_title'],
    'company_name':L2[2]['company_name'],
    'location':L2[2]['location'],
    'start_date':L2[2]['start_date'],
    'duration':L2[2]['duration'],
    'stipend':L2[2]['stipend'],
    'tags':L2[2]['tags']
})

write_details_to_file(r'C:\Users\laptop2\ok\static\out14.txt', {
    'internship_title':L2[3]['internship_title'],
    'company_name':L2[3]['company_name'],
    'location':L2[3]['location'],
    'start_date':L2[3]['start_date'],
    'duration':L2[3]['duration'],
    'stipend':L2[3]['stipend'],
    'tags':L2[3]['tags']
})

write_details_to_file(r'C:\Users\laptop2\ok\static\out15.txt', {
    'internship_title':L2[4]['internship_title'],
    'company_name':L2[4]['company_name'],
    'location':L2[4]['location'],
    'start_date':L2[4]['start_date'],
    'duration':L2[4]['duration'],
    'stipend':L2[4]['stipend'],
    'tags':L2[4]['tags']
})