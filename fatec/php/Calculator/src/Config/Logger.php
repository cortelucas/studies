<?php

namespace App\Config;

use Monolog\Handler\StreamHandler;

class Logger
{

  public static function logger($msg, $type)
  {
    $log = new \Monolog\Logger('app');
    $log->pushHandler(new StreamHandler(dirname(__FILE__) . '/../../Logs/logs.txt'));
    switch ($type) {
      case 'info':
        $log->info($msg);
        break;
      case 'notice':
        $log->notice($msg);
        break;
      case 'error':
        $log->error($msg);
        break;
      case 'warning':
        $log->warning($msg);
        break;
      case 'debug':
        $log->debug($msg);
        break;
      case 'critical':
        $log->critical($msg);
        break;
      case 'alert':
        $log->alert($msg);
        break;
      case 'emergency':
        $log->emergency($msg);
        break;
      default:
        $log->info($msg);
        break;
    }
  }
}
