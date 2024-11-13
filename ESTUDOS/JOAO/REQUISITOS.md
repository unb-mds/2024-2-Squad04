# Proposta de requisitos
---

Lista de requisitos para o projeto, que são consideradas **essenciais** para atingirmos um Minimal Viable Product.

Abaixo das features, será listado algumas opções do que cada feature deve ter. Obviamente, isso não quer dizer que todas devem ser implementadas, mas fica disponível pra escolha. Opções escritas em _itálico_ são as que eu acredito que deve ter.



## Gerenciamento de produtos:

1. CRUD básico
  - _ID_
  - _Nome do produto_
  - _Quantidade base_
  - _Categoria de item_
  - Preço de compra
  - Preço de venda
  - Data de criação
  - Por quem criado
  - Breve descrição

2. Controle do estoque
  - _Alerta de estoque baixo configurável_
  - _Entrada de item (quantidade)_
  - _Saída de item (quantidade)_
  - Retorno de item
  - Perda de item
  - Alerta de estoque cheio

## Fluxo de inventário:

1. Entrada e saída de item
  - _Quantide alterada (para mais ou menos)_
  - _Data e hora de mudança_
  - _Razão de alteração (compra, venda, retorno, perda)_
  - Responsável por operação
  - Origem/destino

2. Status atual de estoque
  - _Quantidade disponível_
  - Quantidade reservada
  - Quantidade em trânsito
  - Quantidade danificada

## Controle de usuário:

1. Autentificação
  - _Sign up_
  - _Login_
  - _Gerenciamento de sessão_

2. Acesso mediante posição
  - _Admin (acesso total)_
  - Trabalhador (acesso limitado)
  - Apenas visualização

