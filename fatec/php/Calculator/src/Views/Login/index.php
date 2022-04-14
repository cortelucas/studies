<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Calculadora | Login</title>
</head>

<style>
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }

  input {
    outline: none;
    border: none;
  }

  input:focus::-webkit-input-placeholder {
    color: transparent;
  }

  input:focus:-moz-placeholder {
    color: transparent;
  }

  input:focus::-moz-placeholder {
    color: transparent;
  }

  input:focus:-ms-input-placeholder {
    color: transparent;
  }

  input::-webkit-input-placeholder {
    color: #999999;
  }

  input:-moz-placeholder {
    color: #999999;
  }

  input::-moz-placeholder {
    color: #999999;
  }

  input:-ms-input-placeholder {
    color: #999999;
  }

  label {
    display: block;
    margin: 0;
  }

  button {
    outline: none !important;
    border: none;
    background: transparent;
  }

  button:hover {
    cursor: pointer;
  }

  .limiter {
    width: 100%;
    margin: 0 auto;
  }

  .container-login {
    width: 100%;
    min-height: 100vh;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    align-items: center;
  }

  .wrap-login {
    width: 100%;
    overflow: hidden;
    display: flex;
    flex-wrap: wrap;
    align-items: stretch;
    flex-direction: row-reverse;
  }

  .login-container__image {
    width: calc(100% - 560px);
    background-image: url('https://images.unsplash.com/photo-1587145820266-a5951ee6f620?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80');
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center;
    position: relative;
    z-index: 1;
  }

  .login-container__image::before {
    content: "";
    display: block;
    position: absolute;
    z-index: -1;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    background-color: rgba(0, 0, 0, 0.1);
  }

  .login-form {
    width: 560px;
    min-height: 100vh;
    display: block;
    padding: 173px 55px 55px 55px;
  }

  .login-form__title {
    width: 100%;
    margin-bottom: 50px;
    display: block;
    font-family: Arial, Helvetica, sans-serif;
    font-size: 36px;
    font-weight: bold;
    color: #333;
    text-align: center;
  }

  .login-form__wrap_input {
    display: flex;
    flex-wrap: wrap;
    align-items: flex-end;
    width: 100%;
    height: 80px;
    position: relative;
    border: 1px solid #e6e6e6;
    border-radius: 8px;
    margin-bottom: 8px;
  }

  .login-form__label {
    font-family: "Lucida Sans", "Lucida Sans Regular", "Lucida Grande",
      "Lucida Sans Unicode", Geneva, Verdana, sans-serif;
    font-size: 18px;
    color: #999;
    line-height: 1.2;
    display: block;
    position: absolute;
    pointer-events: none;
    width: 100%;
    padding-left: 24px;
    left: 0;
    top: 30px;
  }

  .login-form__input {
    display: block;
    width: 100%;
    background: transparent;
    font-family: "Lucida Sans", "Lucida Sans Regular", "Lucida Grande",
      "Lucida Sans Unicode", Geneva, Verdana, sans-serif;
    font-size: 18px;
    color: #555555;
    line-height: 1.2;
    padding: 0 26px;
  }

  input.login-form__input {
    height: 100%;
    -webkit-transition: all 0.4s;
    -o-transition: all 0.4s;
    -moz-transition: all 0.4s;
    transition: all 0.4s;
  }

  .login-form__focus {
    position: absolute;
    display: block;
    width: calc(100% + 2px);
    height: calc(100% + 2px);
    top: -1px;
    left: -1px;
    pointer-events: none;
    border: 1px solid #6675df;
    border-radius: 10px;

    visibility: hidden;
    opacity: 0;

    -webkit-transition: all 0.4s;
    -o-transition: all 0.4s;
    -moz-transition: all 0.4s;
    transition: all 0.4s;

    -webkit-transform: scaleX(1.1) scaleY(1.3);
    -moz-transform: scaleX(1.1) scaleY(1.3);
    -ms-transform: scaleX(1.1) scaleY(1.3);
    -o-transform: scaleX(1.1) scaleY(1.3);
    transform: scaleX(1.1) scaleY(1.3);
  }

  .login-form__input:focus+.login-form__focus {
    visibility: visible;
    opacity: 1;

    -webkit-transform: scale(1);
    -moz-transform: scale(1);
    -ms-transform: scale(1);
    -o-transform: scale(1);
    transform: scale(1);
  }

  .login-form__input:focus {
    height: 48px;
  }

  .login-form__input:focus+.login-form__focus+.login-form__label {
    top: 14px;
    font-size: 13px;
  }

  .login-form__focus_selection {
    visibility: visible;
    opacity: 1;

    -webkit-transform: scale(1);
    -moz-transform: scale(1);
    -ms-transform: scale(1);
    -o-transform: scale(1);
    transform: scale(1);
  }

  .has-val {
    height: 48px !important;
  }

  .has-val+.login-form__focus+.login-form__label {
    top: 14px;
    font-size: 13px;
  }

  .login-form__container_button {
    width: 100%;
    display: -webkit-box;
    display: -webkit-flex;
    display: -moz-box;
    display: -ms-flexbox;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
  }

  .login-form__button {
    display: -webkit-box;
    display: -webkit-flex;
    display: -moz-box;
    display: -ms-flexbox;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 0 20px;
    margin-top: 50px;
    width: 100%;
    height: 50px;
    border-radius: 10px;
    background: #6675df;

    font-family: "Lucida Sans", "Lucida Sans Regular", "Lucida Grande",
      "Lucida Sans Unicode", Geneva, Verdana, sans-serif;
    font-size: 12px;
    color: #fff;
    line-height: 1.2;
    text-transform: uppercase;
    letter-spacing: 1px;

    -webkit-transition: all 0.4s;
    -o-transition: all 0.4s;
    -moz-transition: all 0.4s;
    transition: all 0.4s;
  }

  .login-form__button:hover {
    background: #333333;
  }

  /* Responsive */
  @media (max-width: 992px) {
    .login-form {
      width: 50%;
      padding-left: 30px;
      padding-right: 30px;
    }

    .login-container__image {
      width: 50%;
    }
  }

  @media (max-width: 768px) {
    .login-form {
      width: 100%;
    }

    .login-container__image {
      display: none;
    }
  }

  @media (max-width: 576px) {
    .login-form {
      padding-left: 15px;
      padding-right: 15px;
      padding-top: 70px;
    }
  }
</style>

<body>
  <section class="limiter">
    <div class="container-login">
      <div class="wrap-login">
        <form class="login-form" method="post">
          <span class="login-form__title">Login</span>

          <div class="login-form__wrap_input">
            <input class="login-form__input" type="text" name="user" id="user">
            <span class="login-form__focus"></span>
            <span class="login-form__label">Usuário</span>
          </div>

          <div class="login-form__wrap_input">
            <input class="login-form__input" type="password" name="password" id="password">
            <span class="login-form__focus"></span>
            <span class="login-form__label">Senha</span>
          </div>

          <div class="login-form__container_button">
            <button class="login-form__button" type="submit">Entrar</button>
          </div>
        </form>
        <div class="login-container__image"></div>
      </div>
    </div>
  </section>
</body>

<script>
  (() => {
    'use strict';

    const inputs = document.querySelectorAll('.login-form__input');
    inputs.forEach(input => {
      input.addEventListener('blur', () => {
        if (input.value.trim() !== '') {
          input.classList.add('has-val');
        } else {
          input.classList.remove('has-val');
        }
      });
    })
  })();
</script>

</html>