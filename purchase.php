<?php

## CONFIG ##

# LIST EMAIL ADDRESS
$recipient = "piiamt.tinuviel@gmail.com";

# SUBJECT (Subscribe/Remove)
$subject = "Purchase";

# RESULT PAGE
$location = "enter the URL of the result page here";

## FORM VALUES ##

# SENDER - WE ALSO USE THE RECIPIENT AS SENDER IN THIS SAMPLE
# DON'T INCLUDE UNFILTERED USER INPUT IN THE MAIL HEADER!
$sender = $recipient;

# MAIL BODY
$body .= "Name: ".$_REQUEST['name']." \n";
$body .= "Email: ".$_REQUEST['mail']." \n";
$body .= "Address: ".$_REQUEST['address']." \n";
$body .= "Painting: ".$REQUEST['paintingname']." \n";
# add more fields here if required

## SEND MESSGAE ##

mail( $recipient, $subject, $body, "From: $sender" ) or die ("Mail could not be sent.");

## SHOW RESULT PAGE ##

header( "Location: $location" );
?>
