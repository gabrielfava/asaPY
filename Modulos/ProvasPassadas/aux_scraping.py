#ASAPY
from importlib.machinery import SourceFileLoader
import exercicios_passados_classe
import requests
SourceFileLoader("util_asapy", "../Global/util_asapy.py").load_module()

__URL_GLOBAL = "https://www.urionlinejudge.com.br";

def printme(pagina):
   body = getCorpo(__URL_GLOBAL+"/judge/pt/problems/view/"+pagina);
   iInicio = find_str(body, "<iframe");
   pos = (body[iInicio:]);
   iFim = find_str(pos, ">")+1;
   tupla = pos[:iFim];
   page2 = getAttr(tupla,"src");
   ex = ex_passado();
   ex.setAutor("José de Alencar");
   bodyframe = getCorpo(__URL_GLOBAL+page2);
   return;
   
   


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