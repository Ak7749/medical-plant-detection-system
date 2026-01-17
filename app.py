import os
import random
from datetime import datetime
from functools import wraps
from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from werkzeug.utils import secure_filename
from database import db, init_db
from models import User, MedicinalPlant, Detection

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-change-this-in-production'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///medical_plants.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Initialize database
init_db(app)

# Allowed file extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# Plant classes for detection
PLANT_CLASSES = [
    'Aloe Vera', 'Tulsi (Holy Basil)', 'Neem', 'Turmeric', 
    'Ginger', 'Peppermint', 'Lavender', 'Chamomile',
    'Eucalyptus', 'Rosemary'
]


def allowed_file(filename):
    """Check if file extension is allowed."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def login_required(f):
    """Decorator to require login for routes."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please login to access this page.', 'error')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


@app.route('/')
def index():
    """Redirect to login or dashboard."""
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login page and handler."""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            session['user_id'] = user.id
            session['username'] = user.username
            user.last_login = datetime.utcnow()
            db.session.commit()
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password.', 'error')
    
    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """Signup page and handler."""
    if request.method == 'POST':
        full_name = request.form.get('full_name')
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        # Validation
        if not all([full_name, username, email, password, confirm_password]):
            flash('All fields are required.', 'error')
            return render_template('signup.html')
        
        if password != confirm_password:
            flash('Passwords do not match.', 'error')
            return render_template('signup.html')
        
        if len(password) < 6:
            flash('Password must be at least 6 characters long.', 'error')
            return render_template('signup.html')
        
        # Check if user already exists
        if User.query.filter_by(username=username).first():
            flash('Username already exists.', 'error')
            return render_template('signup.html')
        
        if User.query.filter_by(email=email).first():
            flash('Email already registered.', 'error')
            return render_template('signup.html')
        
        # Create new user
        user = User(
            username=username,
            email=email,
            full_name=full_name
        )
        user.set_password(password)
        
        db.session.add(user)
        db.session.commit()
        
        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('login'))
    
    return render_template('signup.html')


@app.route('/logout')
def logout():
    """Logout user."""
    session.clear()
    flash('Logged out successfully.', 'success')
    return redirect(url_for('login'))


@app.route('/dashboard')
@login_required
def dashboard():
    """User dashboard."""
    user = User.query.get(session['user_id'])
    detections = Detection.query.filter_by(user_id=user.id).order_by(Detection.detected_at.desc()).limit(5).all()
    total_detections = Detection.query.filter_by(user_id=user.id).count()
    
    return render_template('dashboard.html', 
                         user=user, 
                         detections=detections,
                         total_detections=total_detections)


@app.route('/detect')
@login_required
def detect():
    """Detection page."""
    return render_template('index.html')


@app.route('/api/detect', methods=['POST'])
@login_required
def api_detect():
    """API endpoint for plant detection."""
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400
    
    file = request.files['image']
    
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if not allowed_file(file.filename):
        return jsonify({'error': 'Invalid file type. Only PNG, JPG, JPEG allowed'}), 400
    
    try:
        # Save uploaded image
        filename = secure_filename(file.filename)
        timestamp = datetime.utcnow().strftime('%Y%m%d_%H%M%S')
        unique_filename = f"{session['user_id']}_{timestamp}_{filename}"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
        file.save(filepath)
        
        # Mock prediction (random selection since model not available)
        predicted_plant_name = random.choice(PLANT_CLASSES)
        confidence = round(random.uniform(75.0, 99.0), 2)
        
        # Get plant information from database
        plant = MedicinalPlant.query.filter_by(common_name=predicted_plant_name).first()
        
        if plant:
            # Save detection to database
            detection = Detection(
                user_id=session['user_id'],
                plant_id=plant.id,
                image_path=unique_filename,
                confidence=confidence
            )
            db.session.add(detection)
            db.session.commit()
            
            # Return plant information
            return jsonify({
                'success': True,
                'plant': {
                    'id': plant.id,
                    'common_name': plant.common_name,
                    'scientific_name': plant.scientific_name,
                    'description': plant.description,
                    'medical_properties': plant.medical_properties,
                    'usage_instructions': plant.usage_instructions,
                    'dosage': plant.dosage,
                    'warnings': plant.warnings,
                    'season': plant.season,
                    'regions': plant.regions
                },
                'confidence': confidence,
                'detection_id': detection.id
            })
        else:
            return jsonify({
                'success': True,
                'plant': {
                    'common_name': predicted_plant_name,
                    'scientific_name': 'N/A',
                    'description': 'Plant information not available in database.',
                    'medical_properties': [],
                    'usage_instructions': {},
                    'dosage': 'N/A',
                    'warnings': [],
                    'season': 'N/A',
                    'regions': 'N/A'
                },
                'confidence': confidence
            })
    
    except Exception as e:
        return jsonify({'error': f'Error processing image: {str(e)}'}), 500


@app.route('/history')
@login_required
def history():
    """Detection history page."""
    page = request.args.get('page', 1, type=int)
    per_page = 20
    
    detections = Detection.query.filter_by(user_id=session['user_id'])\
        .order_by(Detection.detected_at.desc())\
        .paginate(page=page, per_page=per_page, error_out=False)
    
    return render_template('history.html', detections=detections)


@app.route('/plants')
@login_required
def plants():
    """List all medicinal plants."""
    all_plants = MedicinalPlant.query.all()
    return render_template('plants.html', plants=all_plants)


@app.route('/plant/<int:plant_id>')
@login_required
def plant_detail(plant_id):
    """Plant detail page."""
    plant = MedicinalPlant.query.get_or_404(plant_id)
    return render_template('plant_detail.html', plant=plant)


if __name__ == '__main__':
    # WARNING: Debug mode should be disabled in production
    # Set debug=False and use a production WSGI server like gunicorn
    app.run(debug=True)
