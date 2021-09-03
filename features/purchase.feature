Feature: Fazer uma compra

  Background: página de login, produtos e checkout.
    Given que efetue login com campos de usuario com "standard_user" e de senha com "secret_sauce"
    And que esteja na página de produtos.
    When filtrar "Name (Z to A)" e encontrar os produtos
    And clicar e inserir os produtos "Sauce Labs Onesie, Sauce Labs Fleece Jacket" no carrinho de compras
    Then os produtos estão no carrinho
    When clicar no botão de checkout
    Then estar na página de checkout

  Scenario: Estar no carrinho de compras, ir para checkout e dar erro no checkout por falta de dados.
    When preencher os dados do comprador com "Djonatas", "Borges" e dar continue.
    Then mensagem de erro "Error: Postal Code is required"

  Scenario: Estar no carrinho de compras, ir para checkout e finalizar a compra.
    When alocar dados do comprador com "Djonatas", "Borges" e "13670-000" e dar continue.
    Then estar na página de Overview e os produtos estão listados.
    When finalizar as compras
    Then compra finalizada com sucesso.
