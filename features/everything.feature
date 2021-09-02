Feature: Fazer uma compra
  Scenario: Tela de login
    Given que eu esteja na página de login
    When efetuar login preenchendo os campos de usuario com "standard_user" e de senha com "secret_sauce"
    Then devo logar no site com sucesso.

  Scenario: Adicionar produtos no carrinho de compras
    Given que esteja na página de produtos
    When filtrar "Name (Z to A)" e encontrar os produtos
    Then clicar e inserir os produtos "Sauce Labs Onesie, Sauce Labs Fleece Jacket" no carrinho de compras
    And clicar para ir para o carrinho.

  Scenario: Estar no carrinho de compras, ir para checkout e finalizar a compra.
    Given que esteja na página do carrinho.
    When conferir se os produtos "Sauce Labs Onesie, Sauce Labs Fleece Jacket" estão no carrinho e ir para o checkout
    And preencher os dados do comprador com "Djonatas", "Borges" e "13670-000"
    Then finalizar a compra e voltar para o home.


