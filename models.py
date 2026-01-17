from datetime import datetime
from database import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    """User model for authentication and tracking."""
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    full_name = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    last_login = db.Column(db.DateTime)
    
    # Relationships
    detections = db.relationship('Detection', backref='user', lazy=True, cascade='all, delete-orphan')
    feedbacks = db.relationship('Feedback', backref='user', lazy=True)
    
    def set_password(self, password):
        """Hash and set the user's password."""
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        """Check if the provided password matches the hash."""
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f'<User {self.username}>'


class MedicinalPlant(db.Model):
    """Medicinal plant model with detailed information."""
    __tablename__ = 'medicinal_plants'
    
    id = db.Column(db.Integer, primary_key=True)
    common_name = db.Column(db.String(100), nullable=False, index=True)
    scientific_name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    medical_properties = db.Column(db.JSON, nullable=False)  # Array of properties
    usage_instructions = db.Column(db.JSON, nullable=False)  # Object with different methods
    dosage = db.Column(db.Text, nullable=False)
    warnings = db.Column(db.JSON, nullable=False)  # Array of warnings
    season = db.Column(db.String(100))
    regions = db.Column(db.String(200))
    
    # Relationships
    detections = db.relationship('Detection', backref='plant', lazy=True)
    
    def __repr__(self):
        return f'<MedicinalPlant {self.common_name}>'


class Detection(db.Model):
    """Detection model to track user plant identifications."""
    __tablename__ = 'detections'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False, index=True)
    plant_id = db.Column(db.Integer, db.ForeignKey('medicinal_plants.id'), nullable=False, index=True)
    image_path = db.Column(db.String(255), nullable=False)
    confidence = db.Column(db.Float, nullable=False)
    detected_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False, index=True)
    
    # Relationships
    feedback = db.relationship('Feedback', backref='detection', uselist=False, lazy=True)
    
    def __repr__(self):
        return f'<Detection {self.id} - {self.confidence}%>'


class Feedback(db.Model):
    """Feedback model to track detection accuracy."""
    __tablename__ = 'feedbacks'
    
    id = db.Column(db.Integer, primary_key=True)
    detection_id = db.Column(db.Integer, db.ForeignKey('detections.id'), nullable=False, unique=True, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    is_correct = db.Column(db.Boolean, nullable=False)
    comment = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    
    def __repr__(self):
        return f'<Feedback {self.id} - Correct: {self.is_correct}>'
