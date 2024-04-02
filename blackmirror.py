respostas = {
    "QUAL É O NOME COMPLETO DA PROTAGONISTA DO EPISÓDIO?": "Joan Tait",
    "QUEM DIRIGE A VIDA DE JOAN EM TEMPO REAL PARA UMA SÉRIE DE TELEVISÃO?": "Ela é dirigida em tempo real por um supercomputador.",
    "QUAL É O NOME DO SERVIÇO DE STREAMING FICTÍCIO QUE PARODIA A NETFLIX NO EPISÓDIO?": "Streamberry",
    "COMO JOAN DESCOBRE A EXISTÊNCIA DA SÉRIE SOBRE SUA VIDA?": "Ela descobre quando percebe que seu dia foi retratado pela série.",
    "QUAL É A REAÇÃO INICIAL DE JOAN AO DESCOBRIR A SÉRIE E O QUE ELA FAZ EM RESPOSTA?": "Ela nega os fatos, mas tende a aceitar e tenta processar a streamberry",
    "QUAIS SÃO OS TEMAS PRINCIPAIS EXPLORADOS NESTE EPISÓDIO DE BLACK MIRROR?": "O episódio explora questões atuais e perturbadoras relacionadas à privacidade, manipulação de dados pessoais e exposição na era digital.",
    "O EPISÓDIO TERMINA DE MANEIRA TÍPICA PARA A SÉRIE BLACK MIRROR? EXPLIQUE.": "Não, os finais de blackmirror são dramáticos e tendem a ser distópicos. O episódio termina de forma agradável quando se entende que a Joan parece estar feliz com sua nova liberdade, o que é um desfecho menos sombrio do que o usual para a série."
}

while True:
    pergunta = input("Digite sua pergunta: ")
    if pergunta in respostas:
        print(respostas[pergunta])
    else:
        break

