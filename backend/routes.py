from flask import Blueprint, request, jsonify
from extensions import db
from models import Produtos, Usuarios
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint("api", __name__, url_prefix="/api")

@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    cargo = data.get('cargo', 'cliente')

    # Aqui verifica se o email já existe
    existing_user = Usuarios.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({"message": "E-mail já cadastrado."}), 409  # se o email já existir, ele retorna o 409

    novo_usuario = Usuarios(
        name=name,
        email=email,
        cargo=cargo,
        password_hash=generate_password_hash(password)
    )

    db.session.add(novo_usuario)
    db.session.commit()

    return jsonify({"message": "Usuário criado com sucesso!"}), 201

@bp.route("/login", methods=["POST"])
def login():
    data = request.get_json() or {}
    email = data.get("email")
    password = data.get("password")

    if not all([email, password]):
        return jsonify({"error": "email e password são obrigatórios"}), 400

    user = Usuarios.query.filter_by(email=email).first()
    if not user or not user.check_password(password):
        return jsonify({"error": "Credenciais inválidas"}), 401

    return jsonify({"message": "Login OK", "user": user.to_dict()}), 200


'''
CRUD do Administrador
'''
# Listando usuarios
@bp.route('/users', methods=['GET'])
def get_users():
    users = Usuarios.query.all()
    user_list = []
    for user in users:
        user_list.append({
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "cargo": user.cargo
        })
    return jsonify(user_list), 200

#Criar Usuário
@bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    cargo = data.get('cargo', 'cliente')

    # Checa se o e-mail existe
    if Usuarios.query.filter_by(email=email).first():
        return jsonify({"message": "E-mail já cadastrado."}), 400

    novo_usuario = Usuarios(
        name=name,
        email=email,
        password_hash=generate_password_hash(password),
        cargo=cargo
    )
    db.session.add(novo_usuario)
    db.session.commit()

    return jsonify({"message": "Usuário criado com sucesso!"}), 201

# Editar por ID
@bp.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user = Usuarios.query.get_or_404(id)
    data = request.get_json()

    user.name = data.get('name', user.name)
    user.email = data.get('email', user.email)
    user.cargo = data.get('cargo', user.cargo)

    if 'password' in data and data['password']:
        user.password_hash = generate_password_hash(data['password']) 

    db.session.commit()

    return jsonify({"message": "Usuário atualizado com sucesso!"}), 200


@bp.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = Usuarios.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "Usuário deletado com sucesso!"}), 200

# FUNCOES RELACIONADA AOS PRODUTOS ----------------------------------------------------------
@bp.route('/product', methods=['GET'])
def get_products():
    products = Produtos.query.all()
    product_list = []
    for product in products:
        product_list.append({
            "id_produto": product.id_produto,
            "name": product.name,
            "description": product.description,
            "price": product.price,
            "image": product.image
        })
    return jsonify(product_list), 200

# CRIAR
@bp.route('/product', methods=['POST'])
def create_product():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    price = data.get('price')
    image = data.get('image')

    novo_produto = Produtos(
        name=name,
        description=description,
        price=price,
        image=image
    )
    db.session.add(novo_produto)
    db.session.commit()

    return jsonify({"message": "Produto criado com sucesso!"}), 201

#EDITAR
@bp.route('/product/<int:id>', methods=['PUT'])
def update_product(id):
    product = Produtos.query.get_or_404(id)
    data = request.get_json()

    product.name = data.get('name', product.name)
    product.description = data.get('description', product.description)
    product.price = data.get('price', product.price)
    product.image = data.get('image', product.image)

    db.session.commit()

    return jsonify({"message": "Produto atualizado com sucesso!"}), 200

#EXCLUIR
@bp.route('/product/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Produtos.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({"message": "Produto deletado com sucesso!"}), 200 