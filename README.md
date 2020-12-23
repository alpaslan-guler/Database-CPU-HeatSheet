# Database-CPU-HeatSheet

Turkish:
===========

Veri tabanı Cpu Isı Çizelgesi

- sicaklik_cpu.py  Desktop ta bulunacak
- sicaklik.php /var/www/html/  içinde bulunacak
- crontab içindeki satır /etc/crontab içine eklenecek

- Kullanıcı ve db ssh ile oluşturulur
sudo mysql -u root -p

CREATE DATABASE raspberry_sistem;

USE raspberry_sistem;

CREATE TABLE cpu_temp ( id INT NOT NULL AUTO_INCREMENT,
tarih DATE NOT NULL,
saat TIME NOT NULL,
sicaklik varchar(50),
PRIMARY KEY ( id ));

GRANT INSERT,
SELECT ON raspberry_sistem.* TO 'raspberry'@'localhost' IDENTIFIED BY 'pi';

FLUSH PRIVILEGES;


Sistemin çalışması:
/etc/crontab dosyası içine crontab dosyası içindeki satır en alta eklenir.

/etc/crontab her 10 dakikada bir sicaklik_cpu.py i çalıştırarak db ye veri yazar.

/var/www/html/sicaklik.php den database te işlenen veriler okunabilir.

=======================================================================

English:
=========

Database Cpu Heat Chart

- temp_cpu.py will be found in Desktop
- Temp.php will be found in / var / www / html /
- the line in crontab will be added to / etc / crontab

- User and db generated with ssh
sudo mysql -u root -p

CREATE DATABASE raspberry_sistem;

USE raspberry_sistem;

CREATE TABLE cpu_temp (id INT NOT NULL AUTO_INCREMENT,
date DATE NOT NULL,
hours TIME NOT NULL,
temperature varchar (50),
PRIMARY KEY (id));

GRANT INSERT,
SELECT ON raspberry_sistem. * TO 'raspberry' @ 'localhost' IDENTIFIED BY 'pi';

FLUSH PRIVILEGES;


System operation:
The line in the crontab file is added to the bottom of the / etc / crontab file.

/ etc / crontab writes data to db by running hot_cpu.py every 10 minutes.

The data processed in the database can be read from /var/www/html/sicaklik.php.
