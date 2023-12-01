# teste-compilador
 projeto da faculdade

Este código Python cria uma interface gráfica simples usando a biblioteca Tkinter para construir um analisador léxico básico. O programa permite que o usuário insira código-fonte em uma área de texto, escolha a linguagem de programação entre Python, Java e PHP, e execute a análise léxica, exibindo os tokens resultantes em uma tabela.

Aqui estão as principais partes do código:

Definição de Tokens:

O código define uma lista de tokens que representam elementos da linguagem de programação, como números, identificadores, operadores, etc.
Palavras-chave:

Cada linguagem de programação tem suas próprias palavras-chave. O código define conjuntos de palavras-chave para Python, Java e PHP.
Expressões Regulares para Tokens:

São definidas expressões regulares para identificar tokens como operadores matemáticos, parênteses, chaves, ponto e vírgula, etc.
Funções de Tokenização:

Funções como t_NUMERO e t_IDENTIFICADOR definem como os tokens são reconhecidos com base nas expressões regulares.
Erro Léxico:

A função t_error lida com caracteres ilegais durante o processo de tokenização.
Obter Palavras-chave para a Linguagem Selecionada:

A função obter_palavras_chave determina quais palavras-chave usar com base na linguagem de programação selecionada na interface gráfica.
Analisador Léxico e Função de Análise de Código:

Um analisador léxico é criado usando a ferramenta PLY. A função analisar_codigo_para_linguagem analisa o código-fonte e retorna uma lista de tokens.
Exibição de Resultados:

Os resultados da análise são exibidos em uma tabela usando a biblioteca PrettyTable.
Interface Gráfica (Tkinter):

Uma interface gráfica é criada com uma caixa de combinação para escolher a linguagem, uma área de texto para inserir o código-fonte, um botão para iniciar a análise e outra área de texto para exibir os resultados.
Loop Principal (janela.mainloop()):

Inicia o loop principal da interface gráfica.
Em resumo, esse código implementa uma ferramenta gráfica simples para análise léxica de código-fonte em três linguagens de programação diferentes.
