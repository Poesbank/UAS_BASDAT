SELECT * FROM uas_basdat.data_logistik;
USE uas_basdat;
INSERT INTO data_logistik(Logistic_id, Tanggal_Pengiriman, Jenis_Pengiriman, Status, Jalur_Pengiriman, Jenis_Barang, Asal_Pengiriman, Tujuan_Pengiriman) VALUES (088,'2010-10-10','reguler','terkirim','udara','liquid','asal','bangtoyib');
SELECT * FROM data_logistik WHERE Logistic_id LIKE '%1%';