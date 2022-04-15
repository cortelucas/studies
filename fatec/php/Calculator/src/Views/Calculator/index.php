<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Calculator | Home</title>
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

  body {
    background: #f5f5f5;
    font-family: 'Open Sans', sans-serif;
  }

  .header-nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 20px;
    height: 60px;
    background-color: #fff;
    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
  }

  .calculator-section {
    display: flex;
    justify-content: center;
    align-items: center;
    height: calc(100vh - 60px);
    background-color: #fff;
    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
  }

  .calculator-section form {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    width: 400px;
    height: 400px;
    background-color: #fff;
    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
  }

  .calculator-input {
    width: 80%;
    height: 40px;
    padding: 0 20px;
    border-radius: 4px;
    margin: 10px 0;
    border-bottom: 1px solid #ccc;
    background-color: #fff;
    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
  }

  .calculator-input:focus {
    height: 48px;
  }

  .calculator-commands {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 80%;
    height: 40px;
    padding: 0 20px;
    margin: 10px 0;
  }

  .calculator-select {
    width: 80%;
    height: 40px;
    padding: 0 20px;
    border-radius: 4px;
    border: none;
    margin: 10px 0;
    border-bottom: 1px solid #ccc;
    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
  }

  .calculator-button {
    width: 100%;
    height: 40px;
    padding: 0 20px;
    border-radius: 4px;
    border-bottom: 1px solid #ccc;
    background-color: #fff;
    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
  }

  .calculator-button:hover {
    background-color: #C6C6C6;
    color:#FFF;
  }
</style>

<body>
  <header>
    <div class="header-nav">
      <div>
        <h1>Calculator</h1>
      </div>
      <div>
        Olá <?= $_SESSION['user']; ?>
      </div>
      <div>
        <a href="/logout">Sair</a>
      </div>
    </div>
  </header>

  <main>
    <section class="calculator-section">
      <form method="post" action="/">
        <input class="calculator-input" type="number" name="number_01" placeholder="Insira o número 1">
        <input class="calculator-input" type="number" name="number_02" placeholder="Insira o número 2">
        <div class="calculator-commands">
          <div>
            <select class="calculator-select" name="operator">
              <option selected value="+">+</option>
              <option value="-">-</option>
              <option value="*">*</option>
              <option value="/">/</option>
            </select>
          </div>
          <div>
            <input class="calculator-button" type="submit" value="Calcular">
          </div>
        </div>
      </form>
    </section>
  </main>
</body>

</html>