# MUDAR SENHA ROTEADOR TP LINK 840N

Este projeto tem como objetivo entrar no roteador e realizar a alteração de senha do WIFI no roteador TP LINK 840n. O código foi feito na linguagem Python utilizando o método scrapping para entrar no roteador e trocar a senha

  - Arquivos:
  
    - acessar_roteador.py: Este é o código executavel, onde o usuário insere o nome e senha do roteador para acessa-lo, como também, a nova senha que deseja para a sua rede Wireless. Este código não gera interface, por favor abra o mesmo e verifique nos comentários os locais para inserir usuário e senha do seu roteador e Wifi.
    
    - Read me: Descrição do projeto
    
  - Bibliotecas:
    
    - selenium: Biblioteca usada junto com um driver para que possa simular ações em um site. Normalmente usada para testes e scraping. Neste projeto foi utilizada unicamente para scrapping de alteração de senha e configuração do driver 
    
    - time: Biblioteca de tempo. No atual projeto seu uso foi para pausar o processo em alguns segundos, assim a página pôde ser carregada totalmente para realizar as ações corretas no scrapping. Em alguns casos ações o scraping pode dar errado, por conta da rapidez que o método agi, assim não dá tempo de alguns elementos no site seja carregado totalmente.
    
    
