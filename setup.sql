create table MUSER(MUSER_ID integer primary key autoincrement,MUSER_USERNAME text not null,MUSER_USEREMAIL text not null unique,
MUSER_PASSWORD text not null);