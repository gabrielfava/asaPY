#ASAPY
import requests
__URL_GLOBAL = "https://www.urionlinejudge.com.br";

def printme(pagina):
   body = getCorpo(__URL_GLOBAL+"/judge/pt/problems/view/"+pagina);
   iInicio = find_str(body, "<iframe");
   pos = (body[iInicio:]);
   iFim = find_str(pos, ">")+1;
   tupla = pos[:iFim];
   page2 = getAttr(tupla,"src");
   
   bodyframe = getCorpo(__URL_GLOBAL+page2);
   print(bodyframe);

   return;
   
   
def find_str(s, char):
    index = 0
    if char in s:
        c = char[0]
        for ch in s:
            if ch == c:
                if s[index:index+len(char)] == char:
                    return index
            index += 1
    return -1

#TODO - TRATAR EQUIVALENCIA DE SINTAXE !
def getAttr(tupla, atributo):
    tamanhoAtr = len(atributo)+2; #ja apaga atributo="
    inicioAtr = find_str(tupla, atributo)+tamanhoAtr;
    if inicioAtr == -1:
        return "ERRO"
    fimAttr    = find_str(tupla[inicioAtr:], '"');
    return tupla[inicioAtr:inicioAtr+fimAttr];

def getCorpo(req):
    page = requests.get(req);
    return str(page.content);


printme("2166")
    
#print("titulo  => URI Online Judge - Problema 2166 - Raiz Quadrada de 2")
#print("autor   => M.C. Pinto, UNILA")
#print("probm   => ma das formas de calcular a raiz quadrada de um n\xc3\xbamero natural")