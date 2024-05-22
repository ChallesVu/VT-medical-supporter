import requests
import pandas as pd

init_data_url = "https://edoctor.io/_next/data/xfTRqpzBr5LLPdFdm5GA2/hoi-dap.json"
newsfeed_url_template = "https://cms.edoctor.io/newsfeeds?_limit=10&_start={}"


def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

qna_data = []

data = fetch_data(init_data_url)
newsfeeds = data.get('pageProps', {}).get('newsfeeds', [])
for item in newsfeeds:
    question = item.get('question', {})
    if question:
        content = question.get('content', '')
        comments = question.get('comments', '')
        qna_data.append({
            'Question': content,
            'Answer': comments
        })

start = 10
while start <= 100000:
    url = newsfeed_url_template.format(start)
    data = fetch_data(url)
    newsfeeds = data.get('newsfeeds', [])
    for item in newsfeeds:
        question = item.get('question', {})
        if question:
            content = question.get('content', '')
            comments = question.get('comments', '')
            qna_data.append({
                'Question': content,
                'Answer': comments
            })

    start += 10

df = pd.DataFrame(qna_data)
df.to_csv('edoctor_qna.csv', index=False, encoding='utf-8-sig')