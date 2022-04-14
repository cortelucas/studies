<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Calculator | Home</title>
</head>

<body>
  <header>
    <h1>Calculator</h1>
    <a href="">Sair</a>
  </header>
  <main>
    <section>
      <form method="post" action="/">
        <input type="number" name="number_01" placeholder="Insira o número 1">
        <input type="number" name="number_02" placeholder="Insira o número 2">
        <select name="operator">
          <option value="+">+</option>
          <option value="-">-</option>
          <option value="*">*</option>
          <option value="/">/</option>
        </select>
        <input type="submit" value="Calcular">
      </form>
    </section>
  </main>
</body>

</html>