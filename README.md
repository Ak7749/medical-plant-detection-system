# 🌿 Medical Plant Detection System

A comprehensive web-based application that uses AI to identify medicinal plants from images and provides detailed information about their therapeutic properties, usage instructions, and safety warnings.

## ✨ Features

### User Authentication
- Secure user registration with password strength validation
- Login/logout functionality with session management
- Password hashing using werkzeug.security
- User-specific dashboards and detection history

### Plant Detection
- **Image Upload**: Click or drag-and-drop interface for easy image uploads
- **Real-time Processing**: Instant plant identification from uploaded images
- **Confidence Scores**: Detection accuracy percentage for each identification
- **Detailed Information**: Comprehensive medicinal properties, usage guidelines, dosage, and warnings

### User Dashboard
- Welcome card with personalized greeting
- Statistics overview (total detections, last login, account status)
- Recent detections history with confidence scores
- Quick access to detection functionality

### Database
- SQLite database with SQLAlchemy ORM
- Pre-populated with 8 common medicinal plants:
  - Aloe Vera
  - Tulsi (Holy Basil)
  - Neem
  - Turmeric
  - Ginger
  - Peppermint
  - Lavender
  - Chamomile
- User detection history tracking
- Comprehensive plant information storage

### Security Features
- Password hashing with bcrypt
- Session-based authentication
- SQL injection protection via ORM
- File upload validation
- Secure filename handling
- CSRF protection

## 🛠️ Technology Stack

- **Backend**: Flask (Python web framework)
- **Database**: SQLite with SQLAlchemy ORM
- **Authentication**: Flask sessions with werkzeug password hashing
- **AI/ML**: TensorFlow (with mock predictions for demo)
- **Image Processing**: Pillow (PIL)
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Design**: Responsive, modern UI with gradient themes

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Ak7749/medical-plant-detection-system.git
cd medical-plant-detection-system
```

### 2. Create Virtual Environment

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Initialize Database

```bash
python init_db.py
```

This will create the `medical_plants.db` database and populate it with 8 medicinal plants.

### 5. Run the Application

```bash
python app.py
```

The application will start on `http://127.0.0.1:5000/`

## 📖 Usage Guide

### 1. Sign Up
1. Navigate to `http://127.0.0.1:5000/`
2. Click "Sign up here" on the login page
3. Fill in your details:
   - Full Name
   - Username
   - Email
   - Password (with strength indicator)
   - Confirm Password
4. Click "Create Account"

### 2. Login
1. Enter your username and password
2. Click "Sign In"
3. You'll be redirected to your dashboard

### 3. Detect a Plant
1. Click "Detect Plant" in the navigation menu
2. Upload an image by:
   - Clicking the upload area and selecting a file
   - Dragging and dropping an image
3. Supported formats: PNG, JPG, JPEG (max 16MB)
4. Click "Detect Plant" button
5. View detailed results including:
   - Plant identification with confidence score
   - Medical properties
   - Usage instructions for different methods
   - Dosage recommendations
   - Warnings and precautions
   - Educational disclaimer

### 4. View Dashboard
- See your total detections count
- View recent detection history
- Check last login time
- Quick access to start new detection

### 5. View History
- Access complete detection history
- Filter and search past detections
- Review confidence scores and timestamps

## 📁 Project Structure

```
medical-plant-detection-system/
├── app.py                      # Main Flask application
├── models.py                   # SQLAlchemy database models
├── database.py                 # Database configuration
├── init_db.py                  # Database initialization script
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
├── .gitignore                  # Git ignore file
├── model/                      # Directory for ML model files
│   └── .gitkeep               # Placeholder
├── static/
│   └── uploads/               # User uploaded images
│       └── .gitkeep           # Placeholder
└── templates/                 # HTML templates
    ├── login.html            # Login page
    ├── signup.html           # Registration page
    ├── index.html            # Plant detection page
    └── dashboard.html        # User dashboard
```

## 🔧 Configuration

### Flask Configuration (app.py)
- `SECRET_KEY`: Change in production for security
- `SQLALCHEMY_DATABASE_URI`: Database location
- `UPLOAD_FOLDER`: Directory for uploaded images
- `MAX_CONTENT_LENGTH`: Maximum file upload size (16MB)

### Allowed File Extensions
- PNG
- JPG
- JPEG

## 🎨 Design Specifications

### Color Scheme
- Primary Green: `#2e7d32`
- Dark Green: `#1b5e20`
- Success Green: `#4caf50`
- Warning Orange: `#ff9800`
- Error Red: `#f44336`
- Background: `#f5f5f5`
- Gradient Purple: `#667eea` to `#764ba2`

### UI Components
- Card-based layouts with 15px border radius
- Box shadows for depth
- Smooth transitions (0.3s)
- Responsive design (mobile-friendly)
- Loading spinner animations
- Drag-and-drop with visual feedback

## 🔮 Future Enhancements

- [ ] Train and integrate actual machine learning model
- [ ] Add more medicinal plants to database
- [ ] Implement feedback system for detection accuracy
- [ ] Add multi-language support
- [ ] Create mobile application (iOS/Android)
- [ ] Add plant comparison feature
- [ ] Implement social sharing
- [ ] Add favorites/bookmarking
- [ ] Email notifications for important warnings
- [ ] Admin panel for plant management
- [ ] API documentation with Swagger
- [ ] Export detection history as PDF
- [ ] Plant care recommendations
- [ ] Seasonal availability calendar

## ⚠️ Important Disclaimer

**This application is for educational purposes only.** The information provided about medicinal plants should not be considered professional medical advice. Always consult with qualified healthcare professionals before using any medicinal plants, especially if you:

- Have existing health conditions
- Are pregnant or nursing
- Are taking medications
- Have known allergies
- Are treating children

Some plants may cause allergic reactions or interact with medications. Individual results may vary.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

**Ak7749**

## 🙏 Acknowledgments

- Medicinal plant information compiled from various botanical and medical sources
- UI/UX inspired by modern healthcare applications
- Community feedback and contributions

## 📞 Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Contact: [Your contact information]

---

**Made with ❤️ for better healthcare education**