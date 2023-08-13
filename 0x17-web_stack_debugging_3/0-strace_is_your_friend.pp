# Fixing the bad `phpp` extensions to `php`

exec { 'fix-php':
  provider => shell,
  command  => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php"
}
