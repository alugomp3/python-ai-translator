import requests
from bs4 import BeautifulSoup
from langchain_openai.chat_models.azure import AzureChatOpenAI

def extract_text_url(url):
  response = requests.get(url)
  if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    for script_or_style in soup(['script','style']):
      script_or_style.decompose()
    texto = soup.get_text(separator=' ')
    # Limpar texto
    linhas = (line.strip() for line in texto.splitlines())
    parts = (phrase.strip() for line in linhas for phrase in line.split(' '))
    texto_limpo = '\n'.join(part for part in parts if part)
    return texto_limpo

  else:
    return response.status

  return text

client = AzureChatOpenAI(
    azure_endpoint = 'https://seu_endpoint',
    api_key = 'sua_Api_key',
    api_version = '2024-02-15-preview',
    deployment_name = 'gpt-4o-mini',
    max_retries = 0
)

def translate_article(text, lang):
  messages = [
      ("system", "Você atua como tradutor de textos"),
      ("user", f"Traduza o {text} para o idioma {lang} e responda em markdown")
      ]
  response = client.invoke(messages)
  print(response.content)
  return response.content

url = 'https://dev.to/kenakamu/azure-open-ai-in-vnet-3alo'
text = extract_text_url(url)
translate_article(text,'portugues')
