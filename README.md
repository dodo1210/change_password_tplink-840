# MUDAR SENHA ROTEADOR TP LINK 840N

Este projeto tem como objetivo entrar no roteador e realizar a alteração de senha do WIFI no roteador TP LINK 840n. O código foi feito na linguagem Python utilizando o método scrapping para entrar no roteador e trocar a senha. O sistema operacional Windows

  - Passo a passo
    
    - Configurações:
    
      - Instale as bibliotecas, <a href="https://selenium-python.readthedocs.io">selenium</a> e time.
    
    - Depois baixe o <a href="https://chromedriver.storage.googleapis.com/index.html?path=84.0.4147.30/">driver do google chrome da selenium</a>, com este você pode realizar o scrapping corretamente
    
    - Código:
    
      - No código, importe as bibliotecas com as suas respectivas classes.
      
      - Adicione configurações do selenium para desabilitar a tela de visualização.
      
      - Crie o driver, adicione o caminho onde ele foi instalado e realize a execução do mesmo.
      
      - Neste momento pode inserir o usuário e a senha do roteador obtendo o id das suas respectivas inputs no HTML.
      
      - Crie a ação de clicar no botão de login, usando a id do HTML respectiva a este botão.
      
      - Adicione a time.sleep para que dê tempo de carregar a página de configurações completa.
      
      - A página do Tp 840 é toda feita com iframes, que são outros HTML's dentro de um único site. Então é necessário adicionar um comando de switch iframe para que possa nevegar entre os diferentes códigos HTML.
      
      - Acesse o id iframe1, que é a tela onde contém o menu principal. Após isso, pegue as classes HTML referente as duas opções anteriores para chegar na troca senha. Obs: Por se tratar de uma classe, há mais de um elemento com o mesmo 'nome', então criada-se uma lista com todos os elementos que têm a classe. Nesses casos que contém mais de um elemento com o mesmo nome, é necessário contar quantos elementos há até a opção que você deseja. Para chegar na opção Wireless é a quarta opção. Enquanto que, para chegar em Segurança Wireless é a sexta opção. Então acesse respecivamente cada elemento da lista.  
      
      - Após apresentar a sua atual senha, mude para a id iframe2 e insira a id que representa a input da senha. Na input é necessária fazer uma ação de clique, limpar o conteúdo atual e por fim adicionar a nova senha.
      
      - Para finalizar use a classe que representa o botão salvar e execute a ação de clique.
      
      - Pronto a senha foi trocada.

  - Arquivos:
  
    - acessar_roteador.py: Este é o código executavel, onde o usuário insere o nome e senha do roteador para acessa-lo, como também, a nova senha que deseja para a sua rede Wireless. Este código não gera interface, por favor abra o mesmo e verifique nos comentários os locais para inserir usuário e senha do seu roteador e Wifi.
    
    - Readme: Descrição do projeto
    
  - Bibliotecas:
    
    - selenium: Biblioteca usada junto com um driver para que possa simular ações em um site. Normalmente usada para testes e scraping. Neste projeto foi utilizada unicamente para scrapping de alteração de senha e configuração do driver 
    
    - time: Biblioteca de tempo. No atual projeto seu uso foi para pausar o processo em alguns segundos, assim a página pôde ser carregada totalmente para realizar as ações corretas no scrapping. Em alguns casos ações o scraping pode dar errado, por conta da rapidez que o método agi, assim não dá tempo de alguns elementos no site seja carregado totalmente.
    
    
