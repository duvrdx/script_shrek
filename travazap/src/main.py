from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
    
def main():
    browser_url = "https://web.whatsapp.com"
    msg_list = []
    contact_name = "" #NOME DO CONTATO QUE DESEJA ENVIAR 

    # Recortando roteiro
    a = open('src/roteiro_shrek.txt',"r")
    
    for l in a:
        msg_list.append(l[0:-1])
    a.close()
    
    # Criando configurações
    Config = Options()
    Config.add_argument('window-size=1280,720') #Definido tamanho de tela do Navegador
    
    # Instanciando Navegador
    Browser = webdriver.Chrome(executable_path='chromedriver', options=Config)
    
    # Abrindo Navegador e Esperando Conexão com o WhatsApp - Deve ser conectado o celular com o QR Code
    Browser.get(browser_url)
    sleep(30)
    
    #Entrando na conversa
    Browser.find_element_by_xpath(f'//*[@title="{contact_name}"]').click()
    sleep(1)
    
    #Loop para enviar as mensagens
    for msg in msg_list:
        Browser.find_element_by_class_name("p3_M1").click()
        Browser.find_element_by_xpath('//*[@title="Mensagem"]').send_keys(msg)
        Browser.find_element_by_class_name("_4sWnG").click()
        
        

if __name__ == '__main__':
    main()
    