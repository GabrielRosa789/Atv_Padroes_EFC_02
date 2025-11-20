RESUMO TÉCNICO — Padrões de Projeto Aplicados

Este documento apresenta o estudo teórico dos quatro padrões de projeto utilizados no desenvolvimento da aplicação de e-commerce, seguindo os princípios apresentados no site Refactoring.Guru. Para cada padrão são descritos: conceito, problema resolvido, justificativa de escolha, benefícios e impacto no código caso não fosse utilizado.


-> 1) Strategy

Descrição:
O padrão Strategy permite encapsular diferentes algoritmos ou comportamentos e torná-los intercambiáveis em tempo de execução. Cada estratégia representa uma forma distinta de executar uma operação, mantendo o código cliente desacoplado.

Problema que resolve:
Durante o cálculo do valor final do carrinho de compras, diferentes regras de desconto podem ser aplicadas (percentual, valor fixo, progressivo, cupom etc.). Se essas regras estivessem todas implementadas dentro de uma única classe, o código se tornaria rígido, grande e difícil de manter.

Por que foi adotado neste projeto:
O carrinho de compras precisa alterar a forma de cálculo do desconto sem modificar sua própria implementação interna. O uso do Strategy permite trocar o algoritmo de desconto no momento da execução de forma simples e organizada.

Benefícios:
- elimina condicionais complexas e repetitivas
- cada forma de desconto fica isolada em sua própria classe
- é possível adicionar novas regras sem alterar código existente
- melhora legibilidade e manutenção

Como o código seria sem o padrão:
Todo o cálculo de desconto ficaria dentro da classe de carrinho, resultando em grande número de condicionais e forte acoplamento entre regra de negócio e fluxo da aplicação.


-> 2) Factory Method

Descrição:
O padrão Factory Method centraliza a lógica de criação de objetos em um único ponto, permitindo que o código cliente crie instâncias sem depender diretamente de classes concretas.

Problema que resolve:
O sistema precisa criar diferentes tipos de produtos (por exemplo: livro, eletrônico, vestuário). Se a decisão de qual classe deve ser instanciada ficasse espalhada pelo código, qualquer alteração exigiria modificações em vários locais.

Por que foi adotado neste projeto:
A criação de produtos foi encapsulada em uma fábrica, mantendo o código cliente sem conhecimento de qual classe concreta está sendo utilizada. Isso facilita a adição futura de novos tipos de produto sem modificar o restante do sistema.

Benefícios:
- centraliza a lógica de criação de objetos
- reduz acoplamento entre cliente e classes concretas
- facilita evolução e extensibilidade

Como o código seria sem o padrão:
Cada parte do sistema precisaria decidir manualmente qual classe de produto instanciar, gerando duplicação de lógica e aumentando o risco de erros ao modificar ou adicionar tipos de produtos.


-> 3) Observer

Descrição:
O padrão Observer define um mecanismo de notificação no qual objetos interessados (observadores) são automaticamente avisados quando um evento ocorre em outro objeto (o sujeito observado).

Problema que resolve:
Quando um pedido muda de status (exemplo: pago, enviado, concluído), diferentes partes do sistema precisam reagir, como: envio de mensagem ao cliente, registro de log etc. Fazer essas ações diretamente dentro da classe Pedido aumentaria o acoplamento e tornaria a classe responsável por múltiplas funções.

Por que foi adotado neste projeto:
O Observer permite que a classe Pedido dispare notificações sem conhecer quem escuta ou como cada observador reage. Novos observadores podem ser adicionados sem modificar o código existente.

Benefícios:
- reduz acoplamento entre o sujeito e seus observadores
- facilita expansão do sistema sem alterações na classe principal
- melhora organização e responsabilidade das classes

Como o código seria sem o padrão:
A classe Pedido teria que chamar diretamente todas as ações (exemplo: funções de envio de e-mail e escrita de log), acumulando responsabilidades demais e dificultando manutenção.


-> 4) Facade

Descrição:
O padrão Facade fornece uma interface simplificada para acessar um conjunto de operações complexas. Ele organiza múltiplas chamadas internas em uma única função de alto nível.

Problema que resolve:
O fluxo de compra envolve várias etapas: cálculo do valor final, processamento de pagamento, criação de pedido, registro de observadores e atualização de status. Se o cliente tivesse que chamar todos esses serviços diretamente, o código se tornaria complexo e difícil de utilizar.

Por que foi adotado neste projeto:
A classe CheckoutFacade encapsula todo o processo de finalização de compra, permitindo que o cliente execute uma operação completa chamando apenas um método.

Benefícios:
- simplifica o uso do sistema
- reduz a complexidade visível para o cliente
- facilita manutenção, pois o fluxo está centralizado
- deixa o código mais limpo e legível

Como o código seria sem o padrão:
O cliente precisaria chamar manualmente cada etapa do processo, conhecer o fluxo interno e manipular classes que não deveriam estar expostas, aumentando o acoplamento e tornando a lógica mais frágil.


-> Conclusão

O uso combinado dos padrões Strategy, Factory Method, Observer e Facade proporcionou:

- baixo acoplamento entre componentes
- alta extensibilidade
- responsabilidades bem distribuídas
- código mais claro, organizado e de fácil manutenção

O resultado final demonstra a aplicação prática dos conceitos estudados e atende aos requisitos propostos pela atividade acadêmica.

