# app.py
from flask import Flask, request, jsonify, render_template, redirect, url_for
from config import get_db_connection

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Ruta para obtener todos los clientes
@app.route('/clientes', methods=['GET'])
def get_clientes():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Clientes')
    clientes = cursor.fetchall()
    conn.close()
    return render_template('clientes.html', clientes=clientes)

# Ruta para agregar un nuevo cliente
@app.route('/clientes/add', methods=['POST'])
def add_cliente():
    id_cliente = request.form['id_cliente']
    nombre = request.form['nombre']
    tdocumento = request.form['tdocumento']
    telefono = request.form['telefono']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Clientes (id_cliente, Nombre, TDocumento, Telefono) VALUES (?, ?, ?, ?)',
                   (id_cliente, nombre, tdocumento, telefono))
    conn.commit()
    conn.close()
    return redirect(url_for('get_clientes'))

# Ruta para actualizar un cliente
@app.route('/clientes/update/<id_cliente>', methods=['POST'])
def update_cliente(id_cliente):
    nombre = request.form['nombre']
    tdocumento = request.form['tdocumento']
    telefono = request.form['telefono']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE Clientes SET Nombre = ?, TDocumento = ?, Telefono = ? WHERE id_cliente = ?',
                   (nombre, tdocumento, telefono, id_cliente))
    conn.commit()
    conn.close()
    return redirect(url_for('get_clientes'))

# Ruta para borrar un cliente
@app.route('/clientes/delete/<id_cliente>', methods=['POST'])
def delete_cliente(id_cliente):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Clientes WHERE id_cliente = ?', (id_cliente,))
    conn.commit()
    conn.close()
    return redirect(url_for('get_clientes'))

# Rutas para Productos
@app.route('/productos', methods=['GET'])
def get_productos():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Productos')
    productos = cursor.fetchall()
    conn.close()
    return render_template('productos.html', productos=productos)

@app.route('/productos/add', methods=['POST'])
def add_producto():
    id_producto = request.form['id_producto']
    nombrep = request.form['nombrep']
    tproducto = request.form['tproducto']
    gproducto = request.form['gproducto']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Productos (id_producto, NombreP, TProducto, GProducto) VALUES (?, ?, ?, ?)',
                   (id_producto, nombrep, tproducto, gproducto))
    conn.commit()
    conn.close()
    return redirect(url_for('get_productos'))

@app.route('/productos/update/<id_producto>', methods=['POST'])
def update_producto(id_producto):
    nombrep = request.form['nombrep']
    tproducto = request.form['tproducto']
    gproducto = request.form['gproducto']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE Productos SET NombreP = ?, TProducto = ?, GProducto = ? WHERE id_producto = ?',
                   (nombrep, tproducto, gproducto, id_producto))
    conn.commit()
    conn.close()
    return redirect(url_for('get_productos'))

@app.route('/productos/delete/<id_producto>', methods=['POST'])
def delete_producto(id_producto):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Productos WHERE id_producto = ?', (id_producto,))
    conn.commit()
    conn.close()
    return redirect(url_for('get_productos'))

# Rutas para Compras
@app.route('/compras', methods=['GET'])
def get_compras():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Compras')
    compras = cursor.fetchall()
    conn.close()
    return render_template('compras.html', compras=compras)

@app.route('/compras/add', methods=['POST'])
def add_compra():
    id_cliente = request.form['id_cliente']
    id_producto = request.form['id_producto']
    cantidad = request.form['cantidad']
    preciou = request.form['preciou']
    #valor_total = int(cantidad) * float(preciou)

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Compras (id_cliente, id_producto, cantidad, PrecioU) VALUES (?, ?, ?, ?)',
                   (id_cliente, id_producto, cantidad, preciou))
    conn.commit()
    conn.close()
    return redirect(url_for('get_compras'))

@app.route('/compras/update/<id_doc>', methods=['POST'])
def update_compra(id_doc):
    id_cliente = request.form['id_cliente']
    id_producto = request.form['id_producto']
    cantidad = request.form['cantidad']
    preciou = request.form['preciou']
    #valor_total = int(cantidad) * float(preciou)

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE Compras SET id_cliente = ?, id_producto = ?, cantidad = ?, PrecioU = ? WHERE id_doc = ?',
                   (id_cliente, id_producto, cantidad, preciou, id_doc))
    conn.commit()
    conn.close()
    return redirect(url_for('get_compras'))

@app.route('/compras/delete/<id_doc>', methods=['POST'])
def delete_compra(id_doc):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Compras WHERE id_doc = ?', (id_doc,))
    conn.commit()
    conn.close()
    return redirect(url_for('get_compras'))

if __name__ == '__main__':
    app.run(debug=True)
