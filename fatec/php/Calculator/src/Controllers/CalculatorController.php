<?php

namespace App\Controllers;

use App\Config\Logger;

class CalculatorController
{
  public static function index()
  {
    require '../src/Views/Calculator/index.php';
  }

  public static function calculate()
  {
    $number_01 = $_POST['number_01'];
    $number_02 = $_POST['number_02'];
    $operator = $_POST['operator'];
    $result = 0;
    switch ($operator) {
      case '+':
        $result = $number_01 + $number_02;
        echo $result;
        Logger::logger("Foi realizada a operação de soma", "info");
        break;
      case '-':
        $result = $number_01 - $number_02;
        echo $result;
        Logger::logger("Foi realizada a operação de subtração", "info");
        break;
      case '*':
        $result = $number_01 * $number_02;
        echo $result;
        Logger::logger("Foi realizada a operação de multiplicação", "info");
        break;
      case '/':
        if ($number_02 == 0) {
          $result = 'Divisão por zero';
          echo $result;
          Logger::logger("Foi realizada a operação de divisão por zero", "error");
        } else {
          $result = $number_01 / $number_02;
          echo $result;
          Logger::logger("Foi realizada a operação de divisão", "info");
        }
        break;
      default:
        $result = 'Operação inválida!';
        echo $result;
        Logger::logger("Operação inválida", "error");
        break;
    }
    require '../src/Views/Calculator/result.php';
  }
}
