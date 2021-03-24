
<?php
$output="";
$command = escapeshellcmd('python abc.py &');
  $output = shell_exec($command);
 ?>
<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
  <meta charset="utf-8">
  <title></title>
  <link rel="stylesheet" href="styles.css" type="text/css">
  <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.5.0/css/all.css" integrity="sha384-B4dIYHKNBt8Bc12p+WXckhzcICo0wtJAoU8YZTY5qE0Id1GSseTk6S+L3BlXeVIU" crossorigin="anonymous">
</head>
<body>
  <div class="text">
    <h2>
      <i class="fas fa-language"></i> Speech To Em<i class="far fa-laugh-beam bounce1"></i>ti<i class="fas fa-angry bounce2"></i>n Recognition
    </h2>
  </div>
  <form action="upload.php" method="post" enctype="multipart/form-data">
    <div class=" box1">
      <div class="box2">
        <div class="image">
          <i class="far fa-file-audio"></i>
        </div>
        <input type="file" name="audioFile" class="file" />
        <button type="submit"  value="Upload Audio" name="save_audio" class="upload">Upload<i class="fas fa-angle-double-right"></i></button>
      </div>
    </div>
  </form>
</body>
</html>
