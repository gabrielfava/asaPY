import requests
printme(2661)
# retorna corpo da pagina
def printme(id):
   page = requests.get("https://www.urionlinejudge.com.br/judge/pt/problems/view/"+id);
   print(page.content);
   return;