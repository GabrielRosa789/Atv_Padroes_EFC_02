Mini E-Commerce — Aplicação com Padrões de Projeto

Este projeto foi desenvolvido como atividade acadêmica para demonstrar a aplicação prática de padrões de projeto utilizando a linguagem Python.

A aplicação simula um fluxo de compra em um e-commerce, envolvendo:

- criação de produtos
- aplicação de estratégias de desconto
- realização de pagamento
- criação de pedido
- notificação automática de eventos

Todos os requisitos foram implementados seguindo a estrutura recomendada pelo site Refactoring.Guru.


-> Como executar

1. Clonar o repositório
git clone <url-do-repositorio>

2. Entrar na pasta do projeto
cd projeto

3. Executar a aplicação
python src/main.py

Durante a execução, o sistema demonstrará:

- cálculo do desconto usando o padrão Strategy
- processamento de pagamento
- criação e atualização de pedido
- disparo automático de notificações


-> Estrutura do projeto

src/
├── main.py
│
├── patterns/
│   ├── strategy/
│   ├── factory/
│   ├── observer/
│   └── facade/
│
├── models/
└── services/


-> Padrões de projeto utilizados

O sistema utiliza quatro padrões de projeto, cada um empregado com propósito definido e papel claro dentro do fluxo da aplicação.


1) Strategy – Estratégia de Desconto

Permite trocar a forma de cálculo de desconto sem alterar o código do carrinho de compras.

Localização:
src/patterns/strategy/

Arquivos principais:
- discount_strategy.py
- percentage_discount.py
- fixed_discount.py
- progressive_discount.py
- coupon_discount.py
- shopping_cart.py


2) Factory Method – Criação de Produtos

Padroniza a criação de objetos Produto sem expor ao código cliente qual classe concreta está sendo instanciada.

Localização:
src/patterns/factory/

Arquivos principais:
- product.py
- product_factory.py


3) Observer – Notificação de Alterações de Status

Sempre que o pedido muda de status (pago, enviado, concluído), os observadores são notificados automaticamente.

Localização:
src/patterns/observer/

Arquivos principais:
- subject.py
- observers.py

Integração direta no pedido:
src/models/order.py


4) Facade – Simplificação do Fluxo de Checkout

Encapsula todo o processo de compra:

- processamento de pagamento
- criação do pedido
- registro de observadores
- atualização de status do pedido

Localização:
src/patterns/facade/

Arquivo principal:
- checkout_facade.py


-> Funcionamento geral

O fluxo funciona da seguinte forma:

1. O carrinho de compras contém um valor e usa uma estratégia para calcular desconto.
2. A Facade execura o processo de checkout completo.
3. Um pedido é criado.
4. Observadores recebem notificações automáticas.
5. O sistema permanece desacoplado e fácil de manter.


-> Resumo teórico

O estudo detalhado dos padrões, incluindo:

- justificativa de escolha
- problema que resolve
- benefícios
- impacto no projeto

Está disponível em:
RESUMO.md


-> Autor
Gabriel de Araujo Rosa 23009817
Jose luiz marchi 22017930

