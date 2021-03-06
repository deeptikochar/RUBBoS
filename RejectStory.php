<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <body>
    <?php
    $scriptName = "RejectStory.php";
    include("PHPprinter.php");
    $startTime = getMicroTime();

    $storyId = $_POST['storyId'];
    if ($storyId == null)
    {
      $storyId = $_GET['storyId'];
      if ($storyId == null)
      {
         printError($scriptName, $startTime, "RejectStory", "<h3>You must provide a story identifier !<br></h3>");
         exit();
      }
    }

    getDatabaseLink($link);

    printHTMLheader("RUBBoS: Story submission result");

    print("<center><h2>Story submission result:</h2></center><p>\n");

//    $result = mysql_query("SELECT id FROM submissions WHERE id=$storyId") or die("ERROR: Query failed");
    $result = $link->query("SELECT id FROM submissions WHERE id = $storyId;") or die("ERROR: Query failed");
//    if (mysql_num_rows($result) == 0)
    if (count($result) == 0)
      die("<h3>ERROR: Sorry, but this story does not exist.</h3><br>\n");

    // Delete entry from database
//    mysql_query("DELETE FROM submissions WHERE id=$storyId", $link);
    $link->query("DELETE FROM submissions WHERE id=$storyId;");

    print("The story has been successfully removed from the submissions database table<br>\n");
    
//    mysql_close($link);
    $link->disconnect();   

    printHTMLfooter($scriptName, $startTime);
    ?>
  </body>
</html>
