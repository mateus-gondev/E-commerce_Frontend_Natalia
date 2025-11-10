from flask import Blueprint, request, jsonify
from extensions import db
from models import User
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
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({"message": "E-mail já cadastrado."}), 409  # se o email já existir, ele retorna o 409

    new_user = User(
        name=name,
        email=email,
        cargo=cargo,
        password_hash=generate_password_hash(password)
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "Usuário criado com sucesso!"}), 201

@bp.route("/login", methods=["POST"])
def login():
    data = request.get_json() or {}
    email = data.get("email")
    password = data.get("password")

    if not all([email, password]):
        return jsonify({"error": "email e password são obrigatórios"}), 400

    user = User.query.filter_by(email=email).first()
    if not user or not user.check_password(password):
        return jsonify({"error": "Credenciais inválidas"}), 401

    return jsonify({"message": "Login OK", "user": user.to_dict()}), 200


'''
CRUD do Administrador
'''
# Listando usuarios
@bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
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

    if User.query.filter_by(email=email).first():
        return jsonify({"message": "E-mail já cadastrado."}), 400

    new_user = User(
        name=name,
        email=email,
        password_hash=generate_password_hash(password),
        cargo=cargo
    )
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "Usuário criado com sucesso!"}), 201

# Editar por ID
@bp.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get_or_404(id)
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
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "Usuário deletado com sucesso!"}), 200