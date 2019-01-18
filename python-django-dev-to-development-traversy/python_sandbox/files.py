# Python has functions for creating, reading, updating, and deleting files.

meuArquivo = open('meu-arquivo.txt', 'w')
print('Nome do arquivo:', meuArquivo.name)
print('Fechado:', meuArquivo.closed)
print('Modo de abertura', meuArquivo.mode)

# Escrevendo no arquivo
meuArquivo.write('Eu gosto de Python')
meuArquivo.write('\nEu gosto de Python')
meuArquivo.close()

# Concatenando com caracteres especiais (encoding='utf-8')
meuArquivo = open('meu-arquivo.txt', 'a', encoding='utf-8')
meuArquivo.write('\nTambém curto ReactJs')
meuArquivo.close()

# Leitura do arquivo
meuArquivo = open('meu-arquivo.txt', 'r+', encoding='utf-8')
conteudo = meuArquivo.read(100)
print(conteudo)