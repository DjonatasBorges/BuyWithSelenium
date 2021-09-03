Feature: Fazer Login
  Scenario: Tela de login
    Given que eu esteja na página de login
    When tentar efetuar login preenchendo os campos de usuario com "locked_out_user" e de senha com "secret_sauce"
    Then receber e validar mensagem de erro: "Epic sadface: Sorry, this user has been locked out."