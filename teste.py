import requests

nome_livro = input('Digite o nome do livro: ')

key = 'AIzaSyCySvq_FsmzL4hA7UeqCKXQ0itB4_HHXXE'
url = f'https://www.googleapis.com/books/v1/volumes?q=isbn:{nome_livro}'

response = requests.get(url)
data = response.json()

for datas in data['items']:
    data = datas['volumeInfo']

print(f'Titulo: {data["title"]}')
print(f'Autor: {data["authors"][0]}')
print(f'Ano de lançamento: {data["publishedDate"]}')
print(f'Descrição: {data["description"]}')
# print(f'Imagem: {data['']}')
# for d in data['industryIdentifiers']:
#     # print(f'{d['type']}: {d['identifier']}')
#     print(f'{d['identifier']}')
#     print(f'{d['identifier']}')
print(f'{data["industryIdentifiers"][0]["identifier"]}')
print(f'{data["industryIdentifiers"][1]["identifier"]}')
