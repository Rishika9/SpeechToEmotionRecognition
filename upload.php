<?php
$conn=mysqli_connect('localhost','root','','audiolibdb');
if(!$conn)
{
  die('server not connected');
}
$query="select * from audios";
$result=mysqli_query($conn,$query);
$count=mysqli_num_rows($result)+1;
$ans1="";
$ans2="";
if(isset($_POST['save_audio']) && $_POST['save_audio']=="Upload Audio")
{

  $dir='uploads/'.(string)$count;
  $audio_path=$dir.basename($_FILES['audioFile']['name']);
  if(move_uploaded_file($_FILES['audioFile']['tmp_name'],$audio_path)){
    saveAudio($audio_path);
    $command = escapeshellcmd('python def.py &');
      $output = shell_exec($command);

        $s="";
        for($i=0;$i<strlen($output);$i++)
        {
          if($output[$i]==" ")
          {
            $ans1=$s;
            $s="";
          }
          else {
            $s=$s.$output[$i];
          }
        }
        $ans2=$s;
  }
}
function saveAudio($fileName){
  $conn=mysqli_connect('localhost','root','','audiolibdb');
  if(!$conn)
  {
    die('server not connected');
  }
  $query="insert into audios(filename) values ('{$fileName}')";
  mysqli_query($conn,$query);
  if(mysqli_affected_rows($conn)>0)
  {
    echo "audio file path saved in database.";
  }
  mysqli_close($conn);
}
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
    <div class=" box1">
      <div class="box2">
        <div class="image">
          <i class="fas fa-poll"></i>
        </div>
        <div class="new-file">
        <div>The Person might be <?php  echo $ans1;?><div>
        <div>The accuracy of the model is  <?php  echo $ans2;?> </div>
          </div>
      </div>
    </div>
  </body>
</html>
