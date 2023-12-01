import tkinter as tk
from tkinter import ttk, scrolledtext
from ply import lex
from prettytable import PrettyTable

tokens = (
    'NUMERO',
    'IDENTIFICADOR',
    'MAIS',
    'MENOS',
    'VEZES',
    'DIVIDE',
    'PARENTESE_ESQ',
    'PARENTESE_DIR',
    'CHAVE_ESQ',
    'CHAVE_DIR',
    'PONTO_VIRGULA',
    'IGUAL',
    'PALAVRA_CHAVE',
)

palavras_key_python = {
    'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'
}

palavras_key_java = {
    'abstract',	'assert', 'boolean', 'break', 'byte',
'case', 'catch', 'char', 'class', 'const',
'continue', 'default', 'do', 'double', 'else',
'enum', 'extends', 'final', 'finally', 'float',
'for', 'goto', 'if', 'implements', 'import',
'instanceof', 'int','interface',	'long'	,'native',
'new'	,'package','private', 'protected',	'public',
'return'	,'short'	,'static'	,'strictfp'	,'super',
'switch',	'synchronized',	'this',	'throw',	'throws',
'transient'	,'try',	'void',	'volatile',	'while'
}

palavras_key_php = {
    '__halt_compiler', 'abstract', 'and', 'array', 'as', 'break', 'callable', 'case', 'catch',
    'class', 'clone', 'const', 'continue', 'declare', 'default', 'die', 'do', 'echo', 'else',
    'elseif', 'empty', 'enddeclare', 'endfor', 'endforeach', 'endif', 'endswitch', 'endwhile',
    'eval', 'exit', 'extends', 'final', 'for', 'foreach', 'function', 'global', 'goto', 'if',
    'implements', 'include', 'include_once', 'instanceof', 'insteadof', 'interface', 'isset',
    'list', 'namespace', 'new', 'or', 'print', 'private', 'protected', 'public', 'require',
    'require_once', 'return', 'static', 'switch', 'throw', 'trait', 'try', 'unset', 'use', 'var', 'while', 'xor'

}

t_MAIS = r'\+'
t_MENOS = r'-'
t_VEZES = r'\*'
t_DIVIDE = r'/'
t_PARENTESE_ESQ = r'\('
t_PARENTESE_DIR = r'\)'
t_CHAVE_ESQ = r'\{'
t_CHAVE_DIR = r'\}'
t_PONTO_VIRGULA = r';'
t_IGUAL = r'='

t_ignore = ' \t'

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_IDENTIFICADOR(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value in obter_palavras_chave():
        t.type = 'PALAVRA_CHAVE'
    return t

def t_error(t):
    print(f"Caractere ilegal: {t.value[0]}")
    t.lexer.skip(1)

def obter_palavras_chave():
    linguagem = caixa_combinacao_linguagem.get()
    if linguagem == "Python":
        return palavras_key_python
    elif linguagem == "Java":
        return palavras_key_java
    elif linguagem == "PHP":
        return palavras_key_php
    else:
        return set()

analisador_lexico = lex.lex()

def analisar_codigo():
    codigo = area_texto_codigo.get("1.0", tk.END)
    tokens = analisar_codigo_para_linguagem(codigo)
    exibir_resultados(tokens)

def analisar_codigo_para_linguagem(codigo):
    analisador_lexico.input(codigo)
    tokens = []
    while True:
        tok = analisador_lexico.token()
        if not tok:
            break
        tokens.append(tok)
    return tokens

def exibir_resultados(tokens):
    tabela_resultados = PrettyTable()
    tabela_resultados.field_names = ["Tipo", "Valor"]
    for tok in tokens:
        tabela_resultados.add_row([tok.type, tok.value])

    texto_resultados.config(state=tk.NORMAL)
    texto_resultados.delete(1.0, tk.END)
    texto_resultados.insert(tk.END, tabela_resultados)
    texto_resultados.config(state=tk.DISABLED)

# front
janela = tk.Tk()
janela.title("Projeto Compilador")

rotulo_linguagem = tk.Label(janela, text="Escolha a Linguagem:")
rotulo_linguagem.pack(pady=5)

linguagens = ["Python", "Java", "PHP"]
caixa_combinacao_linguagem = ttk.Combobox(janela, values=linguagens)
caixa_combinacao_linguagem.set("Python")
caixa_combinacao_linguagem.pack(pady=5)

area_texto_codigo = scrolledtext.ScrolledText(janela, wrap=tk.WORD, width=60, height=10)
area_texto_codigo.pack(padx=10, pady=10)

botao_analisar = tk.Button(janela, text="Analisar", command=analisar_codigo)
botao_analisar.pack(pady=5)

texto_resultados = scrolledtext.ScrolledText(janela, wrap=tk.WORD, width=60, height=10, state=tk.DISABLED)
texto_resultados.pack(padx=10, pady=10)

janela.mainloop()