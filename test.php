<?php
require 'vendor/autoload.php';
use Uuid\Uuid;

$nodes = ['10.10.10.8:9042'];

// Connect to database.
$database = new evseevnn\Cassandra\Database($nodes, 'test');
$database->connect();
echo('flag');
// Run query.
$users = $database->query(' select * from trial;');

$oldstr = array(" Bob's uncle is Joe", " I'm confused");
$oldstr = str_replace("'", "''", $oldstr);
//Replace string


$search = 'author'; 
$search_end = $search;
$search_end++;
echo($search);
echo($search_end);
