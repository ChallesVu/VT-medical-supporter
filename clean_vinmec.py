import pandas as pd

file_path = 'vinmec_qna.csv'
data = pd.read_csv(file_path)

cleaned_data = data.dropna(subset=['question', 'answer'])

cleaned_data = cleaned_data[cleaned_data['question'].str.strip() != '']
cleaned_data = cleaned_data[cleaned_data['answer'].str.strip() != '']

cleaned_file_path = 'cleaned_vinmec_qna.csv'
cleaned_data.to_csv(cleaned_file_path, index=False)

cleaned_data.head(), cleaned_file_path