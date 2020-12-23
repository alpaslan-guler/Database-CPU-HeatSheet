import time
import os
import fnmatch
import MySQLdb as mdb
import logging
import time
import datetime

#cpu sicaklik degerinin okunmasi/Reading the CPU temperature value
def cpu_sicaklik_oku():
 res = os.popen('vcgencmd measure_temp').readline()
 return(res.replace("temp=","").replace("'C\n",""))


#mysql veritabanina veri eklenmesi/Adding data to mysql database
def insertDB(cpu_sicaklik):
  sql = "INSERT INTO cpu_temp (tarih, saat, sicaklik) VALUES ('%s', '%s', '%s' )" % (time.strftime("%Y-%m-%d"), time.strftime("%H:%M"), cpu_sicaklik)

  try:

    con = mdb.connect('localhost', 'raspberry', 'pi', 'raspberry_sistem');
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()
    con.close()

  except mdb.Error, e:
    logger.error(e)

#sicaklik okuma ve veritabanina yazma fonksiyonlarini calistiralim/Let's run the temperature reading and database write functions
cpu_sicaklik = float(cpu_sicaklik_oku())
print cpu_sicaklik
insertDB(cpu_sicaklik)
