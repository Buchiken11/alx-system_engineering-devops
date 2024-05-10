# To fix apache bad requset in wp-settings.php

exec{'fix-wrdpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path	  => '/usr/local/bin/:/bin/'
}
