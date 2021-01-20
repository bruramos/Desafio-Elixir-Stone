# Desafio Elixir Stone
Resolução do exercício de desafio proposto em linguagem Python.

## Como criar as listas
- Lista de Itens:

  Criar a lista de itens no formato de matriz, seguindo o formato abaixo (também comentado no próprio código)
  ```
  [[item, quantidade_do_item, valor_unitário], ..., [item, quantidade_do_item, valor_unitário]]
  ```
  **Obs.: respeitar esta formatação, caso contrário o resultado não será conforme o esperado.**
  
- Lista de E-mails:

  Criar a lista com os e-mails em formato de string, seguindo o exemplo abaixo (também comentado no próprio código)
  ```
  ['a@gmail.com', 'b@hotmail.com',...]
  ```
## Funcionamento

- Cálculo do valor total da compra:

  O valor total da compra será a quantidade do item x valor unitário, para cada item presente na lista
  
- Cálculo da divisão por pessoa (e-mail):

  O cálculo utilizará o valor total da compra e dividirá de forma inteira pela quantidade de pessoas (arredondando para baixo);
  
  Caso a divisão não seja inteira, o resto dessa divisão será somado ao valor pago pelo última pessoa (e-mail).

## Testes
O teste automatizado proposto utiliza o framework pytest.

- Para instalar o pytest (Windows):
  ```
  pip install -U pytest
  ```
- Para rodar o teste automatizado:
  ```
  py.test test_desafio.py
  ```
