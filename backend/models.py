from extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

#Modelo Usuario/cliente
class Usuarios(db.Model):
    __tablename__ = "usuarios"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(256), nullable=False)
    cargo = db.Column(db.String(50), default="cliente", nullable=False) 
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "cargo": self.cargo,
            "created_at": self.created_at.isoformat(),
        }
        
class Produtos(db.Model):
    __tablename__ = "produtos"
    id_produto = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    image = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            "id_produto": self.id_produto,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "image": self.image,
        }