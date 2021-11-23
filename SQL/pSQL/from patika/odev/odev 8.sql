/*
Merhabalar,

    1- test veritabanınızda employee isimli sütun bilgileri id(INTEGER), name VARCHAR(50), birthday DATE, email VARCHAR(100) olan bir tablo oluşturalım.
    2- Oluşturduğumuz employee tablosuna 'Mockaroo' servisini kullanarak 50 adet veri ekleyelim.
    3- Sütunların her birine göre diğer sütunları güncelleyecek 5 adet UPDATE işlemi yapalım.
    4- Sütunların her birine göre ilgili satırı silecek 5 adet DELETE işlemi yapalım.

Kolay Gelsin.

*/



--1
CREATE TABLE employee (
	id SERIAL PRIMARY KEY,
	name VARCHAR(50),
	birthday DATE,
	email VARCHAR(100)
	);


--2
insert into employee (name, email, birthday) values ('Angelika', 'achritchley0@washington.edu', null);
insert into employee (name, email, birthday) values ('Radcliffe', 'rvella1@eepurl.com', '2002-03-03');
insert into employee (name, email, birthday) values ('Claretta', 'chudson2@discuz.net', '1915-02-06');
insert into employee (name, email, birthday) values ('Vick', 'vtownrow3@wix.com', '1942-11-15');
insert into employee (name, email, birthday) values ('Bennett', 'bnesby4@techcrunch.com', '1964-07-14');
insert into employee (name, email, birthday) values ('Becky', 'beede5@epa.gov', '1970-08-22');
insert into employee (name, email, birthday) values ('Alisha', null, '1995-12-31');
insert into employee (name, email, birthday) values ('Emilie', 'eriddington7@addthis.com', '2013-12-04');
insert into employee (name, email, birthday) values ('Gabbi', 'gmallam8@ebay.com', '1931-02-09');
insert into employee (name, email, birthday) values ('Adele', 'aroarty9@fastcompany.com', '1951-06-27');
insert into employee (name, email, birthday) values ('Hartwell', 'hhawkeswooda@google.com', '2018-09-21');
insert into employee (name, email, birthday) values ('Alix', 'abattleb@wikimedia.org', '1995-02-26');
insert into employee (name, email, birthday) values ('Fonz', 'fmcgillicuddyc@economist.com', null);
insert into employee (name, email, birthday) values ('Andrej', 'ajobbingd@feedburner.com', '2013-10-05');
insert into employee (name, email, birthday) values ('Hildy', null, '1982-02-28');
insert into employee (name, email, birthday) values ('Billy', 'bscohierf@squarespace.com', '1933-03-02');
insert into employee (name, email, birthday) values ('Ignatius', 'igrassickg@sfgate.com', '1970-04-25');
insert into employee (name, email, birthday) values ('Hailee', 'hmaharryh@xinhuanet.com', '1940-01-25');
insert into employee (name, email, birthday) values ('Fan', 'fcoatmani@de.vu', '1907-12-17');
insert into employee (name, email, birthday) values ('Madonna', 'mgawj@wunderground.com', '1981-03-30');
insert into employee (name, email, birthday) values ('Brigham', 'bsawleyk@lycos.com', '1965-07-27');
insert into employee (name, email, birthday) values ('Ikey', 'ifogtl@opensource.org', '1919-02-23');
insert into employee (name, email, birthday) values ('Wenona', 'wtsarm@netscape.com', '1980-03-20');
insert into employee (name, email, birthday) values ('Salli', 'sbancroftn@irs.gov', '1904-07-29');
insert into employee (name, email, birthday) values ('Pancho', 'phucklesbyo@bloglovin.com', '1901-05-02');
insert into employee (name, email, birthday) values ('Davie', 'dkitchinp@fastcompany.com', null);
insert into employee (name, email, birthday) values ('Teresa', 'twayperq@cloudflare.com', '1990-09-23');
insert into employee (name, email, birthday) values ('Rachele', 'rquener@uiuc.edu', '1951-07-18');
insert into employee (name, email, birthday) values ('Reid', null, '1902-05-24');
insert into employee (name, email, birthday) values ('Tootsie', 'tcompstont@weebly.com', '1975-03-31');
insert into employee (name, email, birthday) values ('Felix', 'fgutierrezu@mlb.com', '2011-01-28');
insert into employee (name, email, birthday) values ('Bernie', 'breinbechv@ftc.gov', null);
insert into employee (name, email, birthday) values ('Louella', 'lklimentyevw@google.es', '2019-07-26');
insert into employee (name, email, birthday) values ('Alvira', 'ahuftonx@liveinternet.ru', '1929-06-28');
insert into employee (name, email, birthday) values ('Florenza', 'fmillsony@time.com', '1991-07-18');
insert into employee (name, email, birthday) values ('Tim', 'tbilberyz@hao123.com', '1974-04-05');
insert into employee (name, email, birthday) values ('Garnet', 'gbrende10@bluehost.com', '1960-02-08');
insert into employee (name, email, birthday) values ('Obadias', 'odrought11@fda.gov', '1932-10-31');
insert into employee (name, email, birthday) values ('Quinton', null, '2009-08-23');
insert into employee (name, email, birthday) values ('Brandi', 'bgrier13@wikispaces.com', '2000-12-25');
insert into employee (name, email, birthday) values ('Rolando', 'rbawme14@domainmarket.com', '1931-05-20');
insert into employee (name, email, birthday) values ('Star', 'saustins15@blogger.com', '1913-10-01');
insert into employee (name, email, birthday) values ('Willdon', 'wsibbering16@slate.com', null);
insert into employee (name, email, birthday) values ('Jennilee', 'jkirtley17@goodreads.com', '1996-07-13');
insert into employee (name, email, birthday) values ('Iorgo', 'idownton18@si.edu', null);
insert into employee (name, email, birthday) values ('Guido', 'gdufton19@paypal.com', '1971-04-22');
insert into employee (name, email, birthday) values ('Hadleigh', 'hmallalieu1a@fema.gov', '1924-09-14');
insert into employee (name, email, birthday) values ('De witt', 'djahner1b@nyu.edu', null);
insert into employee (name, email, birthday) values ('Jorge', 'jdavy1c@hatena.ne.jp', null);
insert into employee (name, email, birthday) values ('Tamra', 'tkemwall1d@elegantthemes.com', '1993-09-17');

--3
--3.1
UPDATE employee
SET name = 'UPDATED' 
WHERE name ~~ 'B%';
--3.2
UPDATE employee
SET birthday = null 
WHERE name = 'UPDATED' and ID > 20;
--3.3
UPDATE employee
SET email = null
WHERE id BETWEEN 25 AND 30;
--3.4
UPDATE employee
SET name = 'HAHAHA DEZZZ NUTZZZ'
WHERE id NOT BETWEEN 1 AND 40;
--3.5
UPDATE employee
SET name = 'HAHAHA DEZZZ NUTZZZ',
	email = '2023secimlerindehukumetdegismeli@gmail.com'
WHERE id IN (30, 40, 18);

--4
--4.1
DELETE FROM employee
WHERE Name ~~ '%l';
--4.2
DELETE FROM employee
WHERE name ~~ 'H%' or birthday = null;
--4.3
DELETE FROM employee
WHERE id < 5 AND name ~~ 'R%';
--4.4
DELETE FROM employee
WHERE name NOT LIKE 'UPDATED' OR birthday <> null;
--4.5
DELETE FROM IF EXISTS employee
WHERE name ~~ 'UPDATED' AND birthday = ''; -- ben date kisminin bos oldugunda nasil silinecigini anlayamadim, sonra cozerim ben yemege gidiyorum :D (location: ege universitesi kutuphanesi)