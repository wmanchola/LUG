CREATE DATABASE TIENDA;
USE TIENDA;

CREATE TABLE CLIENTES (
	id_cliente INT NOT NULL PRIMARY KEY,
	Nombre NVARCHAR (100) NOT NULL,
	TDocumento char (3) NOT NULL,
	--Documento NVARCHAR (20) NOT NULL
	Telefono NVARCHAR (50) NOT NULL
);

CREATE TABLE PRODUCTOS (
	id_producto NVARCHAR(50) NOT NULL PRIMARY KEY,
	NombreP NVARCHAR (100) NOT NULL,
	TProducto INT NOT NULL,
	GProducto NVARCHAR(100) NOT NULL,
);

CREATE TABLE COMPRAS (
	id_doc INT identity(1,1) PRIMARY KEY,
	--NombreP NVARCHAR (100) NOT NULL
	id_cliente INT FOREIGN KEY REFERENCES CLIENTES(id_cliente),
	id_producto NVARCHAR(50) FOREIGN KEY REFERENCES PRODUCTOS(id_producto),
	Cantidad INT NOT NULL,
	PrecioU NUMERIC (19,2) NOT NULL
);

INSERT INTO CLIENTES VALUES(80901123, 'Juan Perez Gomez', 'CC', '3216549878');
INSERT INTO CLIENTES VALUES(90801123, 'Andrea Flores Rios', 'CC', '3207894564');
INSERT INTO CLIENTES VALUES(900123456, 'Maria Camila Mora', 'NIT', '3218965874');
INSERT INTO CLIENTES VALUES(800125489, 'Carlos Andres Vives', 'NIT', '3185694876');
INSERT INTO CLIENTES VALUES(1025468971, 'Alejandra Moreno Sierra', 'CC', '3157812252');

INSERT INTO PRODUCTOS VALUES('A001', 'Manzana roja', 101, 'Frutas');
INSERT INTO PRODUCTOS VALUES('B001', 'Tomate rojo', 102, 'Verduras');
INSERT INTO PRODUCTOS VALUES('C001', 'Jabon de baño', 103, 'Aseo personal');
INSERT INTO PRODUCTOS VALUES('C002', 'Cepillo de dientes', 103, 'Aseo personal');
INSERT INTO PRODUCTOS VALUES('D001', 'Escoba', 104, 'Aseo Hogar');
INSERT INTO PRODUCTOS VALUES('E001', 'Arroz blanco', 105, 'Granos');
INSERT INTO PRODUCTOS VALUES('E002', 'Frijol rojo', 105, 'Granos');
INSERT INTO PRODUCTOS VALUES('E003', 'garbanzos', 105, 'Granos');
INSERT INTO PRODUCTOS VALUES('F001', 'Carne de res', 106, 'Proteina animal');
INSERT INTO PRODUCTOS VALUES('F002', 'Carne de cerdo', 106, 'Proteina animal');
INSERT INTO PRODUCTOS VALUES('F003', 'Carne de pollo', 106, 'Proteina animal');
INSERT INTO PRODUCTOS VALUES('F004', 'Pescado', 106, 'Proteina animal');


INSERT INTO COMPRAS VALUES(80901123, 'A001', 1, 800);
INSERT INTO COMPRAS VALUES(80901123, 'B001', 5, 300);
INSERT INTO COMPRAS VALUES(80901123, 'C001', 2, 2700);
INSERT INTO COMPRAS VALUES(80901123, 'D001', 1, 5850);
INSERT INTO COMPRAS VALUES(80901123, 'E001', 25, 2230);
INSERT INTO COMPRAS VALUES(1025468971, 'C001', 6, 2700);
INSERT INTO COMPRAS VALUES(1025468971, 'C002', 4, 6600);
INSERT INTO COMPRAS VALUES(1025468971, 'C002', 4, 6600);
INSERT INTO COMPRAS VALUES(900123456, 'B001', 12, 300);
INSERT INTO COMPRAS VALUES(900123456, 'E001', 1, 2230);
INSERT INTO COMPRAS VALUES(900123456, 'E002', 2, 2780);
INSERT INTO COMPRAS VALUES(900123456, 'E003', 1, 1500);
INSERT INTO COMPRAS VALUES(800125489, 'D001', 1, 5850);
INSERT INTO COMPRAS VALUES(800125489, 'F004', 1, 18000);
INSERT INTO COMPRAS VALUES(90801123, 'A001', 1, 800);
INSERT INTO COMPRAS VALUES(90801123, 'B001', 1, 300);
INSERT INTO COMPRAS VALUES(90801123, 'C001', 1, 2700);
INSERT INTO COMPRAS VALUES(90801123, 'D001', 1, 5850);
INSERT INTO COMPRAS VALUES(90801123, 'E001', 1, 2230);
INSERT INTO COMPRAS VALUES(90801123, 'E002', 1, 2780);
INSERT INTO COMPRAS VALUES(90801123, 'E003', 1, 1500);
INSERT INTO COMPRAS VALUES(90801123, 'F001', 1, 18300);
INSERT INTO COMPRAS VALUES(90801123, 'F002', 1, 12400);
INSERT INTO COMPRAS VALUES(90801123, 'F003', 1, 8000);
INSERT INTO COMPRAS VALUES(90801123, 'F004', 1, 18000);