<?php

require __DIR__ . "/vendor/autoload.php";

$method = $_SERVER['REQUEST_METHOD'];
$path = $_SERVER['PATH_INFO'] ?? "/";

$route = new \App\Router($method, $path);

$route->get("/login", "App\Controllers\AuthController::index");

$route->get("/", "App\Controllers\CalculatorController::index");
$route->post("/", "App\Controllers\CalculatorController::calculate");

$result = $route->handler();
if (!$result) {
  http_response_code(404);
  echo "Página não encontrada!";
  die();
}

echo $result($route->getParams());

//php -S localhost:8000 -t public/
