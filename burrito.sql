create table conductor(
idcondu int auto_increment primary key,
nomcond varchar(50),
apecond varchar(50),
correo_cond varchar(100),
direc_cond varchar(100),
cod_cond char(8),
pass_cond varchar(50),
telef_cond int,
coorde_cond varchar(2000)
);

create table alumnos(
idalu int auto_increment primary key,
nomalu varchar(50),
apealu varchar(50),
sexo char(1),
codalu char(8),
pass_alu varchar(50),
correo_alu varchar(100),
direc_alu varchar(100),
telef_alu int,
constraint chk_sexo check (sexo in ('M','F'))
);

Create table Usuario(
idusu int auto_increment primary key,
codusu char(8),
paswusu varchar(50),
idalu int,
idcondu int,
constraint fk_alumnos_usuario foreign key (idalu) references alumnos(idalu),
constraint fk_conuductor_usuario foreign key (idcondu) references conductor(idcondu)
);

create table bus(
idbus int auto_increment primary key,
idusu int,
constraint fk_usuario_bus foreign key (idusu) references usuario(idusu)
);

create table localizacion(
latitud varchar(50),
longitud varchar(50),
fecha_hora datetime,
idbus int,
constraint fk_bus_localizacion foreign key (idbus) references bus(idbus)
);
