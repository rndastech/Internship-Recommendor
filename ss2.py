import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Define a function to merge skills and companies
def merge_skills_and_companies(df):
    for index, row in df.iterrows():
        # Merge all elements in the Skill column for the current row
        merged_skill = ''.join(row['Skill'])
        df.at[index, 'Skill'] = merged_skill
        
        # Merge all elements in the Companies column for the current row
        merged_companies = ''.join(row['Companies']).replace(' ', '')
        df.at[index, 'Companies'] = merged_companies
        
    return df

# Load data containing skills, industries, companies, and popularity scores
df = pd.read_csv('SkillSet2.csv')

# Call the function to merge the skills and companies
df = merge_skills_and_companies(df)

# Initialize CountVectorizer
cv = CountVectorizer(max_features=5000, stop_words='english')
vector = cv.fit_transform(df['Companies']).toarray()

# Compute cosine similarity matrix
sim = cosine_similarity(vector)

# Define a function to recommend similar skills
def recommend(skill):
    L2 = []
    if skill.strip():  # Check if the skill is not empty
        if skill in df['Skill'].values:
            indices = df[df['Skill'] == skill].index
            if len(indices) > 0:
                index = indices[0]
                distances = sorted(enumerate(sim[index]), reverse=True, key=lambda x: x[1])
                
                # Sort distances based on popularity index of recommended skills
                distances = sorted(distances[1:6], key=lambda x: df.iloc[x[0]]['Popularity Index'], reverse=True)
                
                for i in distances:
                    L2.append(df.iloc[i[0]]['Skill'])  # Append the recommended skills
            else:
                print(f"The skill '{skill}' is not in the dataset.")
        else:
            print(f"The skill '{skill}' is not in the dataset.")
    else:
        print("Please provide a valid skill name.")

    return L2

# Provide the path to your text file
file_path = 'input1.txt'

try:
    with open(file_path, 'r') as file:
        content = file.read().strip()
        recommendations = recommend(content)  # Call the function with a skill title
        print(recommendations)  # Print the recommended skills
        # Save the recommended skills to a text file
        with open(r'C:\Users\laptop2\ok\static\out21.txt', 'w', encoding='utf-8') as file_out:
           
         file_out.write("%s\n" % recommendations[0])
        with open(r'C:\Users\laptop2\ok\static\out22.txt', 'w', encoding='utf-8') as file_out:
           
         file_out.write("%s\n" % recommendations[1])
        with open(r'C:\Users\laptop2\ok\static\out23.txt', 'w', encoding='utf-8') as file_out:
           
         file_out.write("%s\n" % recommendations[2])
        with open(r'C:\Users\laptop2\ok\static\out24.txt', 'w', encoding='utf-8') as file_out:
           
         file_out.write("%s\n" % recommendations[3])
        with open(r'C:\Users\laptop2\ok\static\out25.txt', 'w', encoding='utf-8') as file_out:
           
         file_out.write("%s\n" % recommendations[4])
except FileNotFoundError:
    print(f"File '{file_path}' not found.")

# Save the similarity matrix to a pickle file
import pickle
pickle.dump(sim, open('similarity.pkl', 'wb'))
