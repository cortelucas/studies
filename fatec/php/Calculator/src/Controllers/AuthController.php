<?php

namespace App\Controllers;

use App\Config\Logger;

class AuthController
{
  public static function index()
  {
    require '../src/Views/Login/index.php';
  }

  public static function logIn()
  {
    $user = $_POST['user'];
    $password = $_POST['password'];

    try {
      session_start();
      if (isset($user, $password)) {
        if ($user == 'admin' && $password == 'admin') {
          $_SESSION['user'] = $user;
          $_SESSION['password'] = $password;
          Logger::logger("O usuário $user logou no sistema", "info");
          if ($_SESSION['user']) {
            header('Location: /');
          } else {
            echo 'Erro ao logar';
          }
        } else {
          throw new \Exception('Usuário ou senha inválidos');
        }
      }
    } catch (\Exception $e) {
      echo $e->getMessage();
      Logger::logger("O usuário $user tentou logar no sistema", "error");
    } finally {
      die();
    }
  }

  public static function logOut()
  {
    $user = $_SESSION['user'];
    try {
      session_start();
      session_destroy();
      Logger::logger("O usuário $user logou no sistema", "info");
      header('Location: /login');
    } catch (\Exception $e) {
      echo $e->getMessage();
      Logger::logger("O usuário $user tentou logar no sistema", "error");
    } finally {
      die();
    }
  }
}
