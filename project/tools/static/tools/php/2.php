<?php
if (isset($_POST['hidden_field'])) // если данные скрытого поля переданы обработчику
  {
	  
$xm =  $_POST['xm']; // А здесь с name "xm"	  
	  
$url = 'https://tools.xmeye.net/deviceSuperPassword?text='.$xm;

$ch = curl_init($url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

$response = curl_exec($ch);
curl_close($ch);



$array = json_decode(file_get_contents("$url"), true); //Получить содержимое файла целиком, и декодировать строку JSON
$String = implode(' ',$array);  //Объединяет элементы массива в строку

 $Number = explode(" ", $String); //Разбивает строку с помощью разделителя
$Number[0];  //Первая строка в массиве 
$Number[1];  //Вторая строка в массиве



echo '<b>Коды сбросов</b>: <br>';
echo substr($Number[0], 0, 6);
echo '<br>'.$Number[0];

  }


?>