function superpassword() {
    var day1 = document.getElementById('day').value;
    var month1 = document.getElementById('month').value;
    var year1 = document.getElementById('year').value;
    var super1 = year1.substr(2, 2) * month1 * day1 * (year1 - 1900) * 6666 % 1000000 + 1000000;
    var Note = "<span lang=\"ru\">Супер-пароль: </span>";
    document.getElementById('KQ').innerHTML = Note + String(super1).substr(String(super1).length - 6, 6);
  }