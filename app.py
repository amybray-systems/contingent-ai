"""
ContingentAI - Main Application File
A starter template to get you building quickly!
"""

from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///contingent_ai.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# ============================================================================
# DATABASE MODELS (Minimal to start)
# ============================================================================

class Department(db.Model):
    __tablename__ = 'departments'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    code = db.Column(db.String(20))
    budget_annual = db.Column(db.Numeric(12, 2))
    headcount_target = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    workers = db.relationship('Worker', backref='department', lazy=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'code': self.code,
            'budget_annual': float(self.budget_annual) if self.budget_annual else 0,
            'headcount_target': self.headcount_target
        }

class Worker(db.Model):
    __tablename__ = 'workers'
    
    id = db.Column(db.Integer, primary_key=True)
    worker_id = db.Column(db.String(50), unique=True, nullable=False)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(255))
    worker_type = db.Column(db.String(20))  # 'contractor', 'fte', 'eor'
    status = db.Column(db.String(20))  # 'active', 'inactive', 'terminated'
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date, nullable=True)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))
    job_title = db.Column(db.String(100))
    hourly_rate = db.Column(db.Numeric(10, 2), nullable=True)
    annual_salary = db.Column(db.Numeric(12, 2), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'worker_id': self.worker_id,
            'name': f"{self.first_name} {self.last_name}",
            'email': self.email,
            'worker_type': self.worker_type,
            'status': self.status,
            'department': self.department.name if self.department else None,
            'job_title': self.job_title,
            'hourly_rate': float(self.hourly_rate) if self.hourly_rate else None,
            'annual_salary': float(self.annual_salary) if self.annual_salary else None
        }

class Cost(db.Model):
    __tablename__ = 'costs'
    
    id = db.Column(db.Integer, primary_key=True)
    worker_id = db.Column(db.Integer, db.ForeignKey('workers.id'))
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))
    period_start = db.Column(db.Date)
    period_end = db.Column(db.Date)
    hours_worked = db.Column(db.Numeric(10, 2))
    cost_amount = db.Column(db.Numeric(12, 2))
    cost_type = db.Column(db.String(50))  # 'salary', 'fees', 'benefits', 'taxes'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# ============================================================================
# ROUTES
# ============================================================================

@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    """Main analytics dashboard"""
    # Get key metrics
    total_workers = Worker.query.filter_by(status='active').count()
    total_contractors = Worker.query.filter_by(status='active', worker_type='contractor').count()
    total_fte = Worker.query.filter_by(status='active', worker_type='fte').count()
    total_eor = Worker.query.filter_by(status='active', worker_type='eor').count()
    
    # Get departments
    departments = Department.query.all()
    
    # Calculate total monthly cost (simplified)
    total_cost = 0
    for worker in Worker.query.filter_by(status='active').all():
        if worker.hourly_rate:
            total_cost += float(worker.hourly_rate) * 160  # Assume 160 hrs/month
        elif worker.annual_salary:
            total_cost += float(worker.annual_salary) / 12
    
    # Get headcount by department
    dept_headcount = {}
    for dept in departments:
        count = Worker.query.filter_by(department_id=dept.id, status='active').count()
        dept_headcount[dept.name] = count
    
    return render_template('dashboard.html',
                         total_workers=total_workers,
                         total_contractors=total_contractors,
                         total_fte=total_fte,
                         total_eor=total_eor,
                         total_cost=round(total_cost, 2),
                         departments=departments,
                         dept_headcount=dept_headcount)

@app.route('/workers')
def workers_list():
    """List all workers"""
    workers = Worker.query.filter_by(status='active').all()
    return render_template('workers.html', workers=workers)

@app.route('/ai')
def ai_assistant():
    """AI Assistant chat interface"""
    return render_template('ai_chat.html')

@app.route('/api/ai/chat', methods=['POST'])
def ai_chat():
    """Handle AI chat requests"""
    data = request.get_json()
    user_message = data.get('message', '')
    
    # TODO: Implement OpenAI integration here
    # For now, return a simple response
    
    # Example response
    response = {
        'response': f"I received your message: '{user_message}'. AI integration coming soon!",
        'data': {}
    }
    
    return jsonify(response)

@app.route('/scenarios')
def scenarios():
    """Scenario planning page"""
    return render_template('scenarios.html')

@app.route('/vendors')
def vendors():
    """Vendor management page"""
    return render_template('vendors.html')

# ============================================================================
# API ENDPOINTS (for AJAX requests)
# ============================================================================

@app.route('/api/workers')
def api_workers():
    """Get workers as JSON"""
    workers = Worker.query.filter_by(status='active').all()
    return jsonify([w.to_dict() for w in workers])

@app.route('/api/departments')
def api_departments():
    """Get departments as JSON"""
    departments = Department.query.all()
    return jsonify([d.to_dict() for d in departments])

@app.route('/api/dashboard/stats')
def api_dashboard_stats():
    """Get dashboard statistics"""
    stats = {
        'total_workers': Worker.query.filter_by(status='active').count(),
        'by_type': {
            'contractor': Worker.query.filter_by(status='active', worker_type='contractor').count(),
            'fte': Worker.query.filter_by(status='active', worker_type='fte').count(),
            'eor': Worker.query.filter_by(status='active', worker_type='eor').count(),
        },
        'by_department': {}
    }
    
    # Get by department
    departments = Department.query.all()
    for dept in departments:
        count = Worker.query.filter_by(department_id=dept.id, status='active').count()
        stats['by_department'][dept.name] = count
    
    return jsonify(stats)

# ============================================================================
# CLI COMMANDS (for database management)
# ============================================================================

@app.cli.command('init-db')
def init_db():
    """Initialize the database."""
    db.create_all()
    print('✅ Database initialized!')

@app.cli.command('seed-db')
def seed_db():
    """Seed the database with sample data."""
    # Create sample departments
    departments_data = [
        {"name": "Engineering", "code": "ENG", "budget_annual": 5000000, "headcount_target": 120},
        {"name": "Product", "code": "PRD", "budget_annual": 1500000, "headcount_target": 25},
        {"name": "Design", "code": "DES", "budget_annual": 800000, "headcount_target": 15},
        {"name": "Marketing", "code": "MKT", "budget_annual": 1200000, "headcount_target": 30},
        {"name": "Sales", "code": "SAL", "budget_annual": 2000000, "headcount_target": 40},
    ]
    
    for dept_data in departments_data:
        dept = Department(**dept_data)
        db.session.add(dept)
    
    db.session.commit()
    print(f'✅ Created {len(departments_data)} departments')
    
    # Create sample workers
    eng_dept = Department.query.filter_by(code='ENG').first()
    
    sample_workers = [
        {
            "worker_id": "W00001",
            "first_name": "John",
            "last_name": "Smith",
            "email": "john.smith@example.com",
            "worker_type": "fte",
            "status": "active",
            "start_date": datetime.now() - timedelta(days=365),
            "department_id": eng_dept.id,
            "job_title": "Senior Software Engineer",
            "annual_salary": 180000
        },
        {
            "worker_id": "W00002",
            "first_name": "Sarah",
            "last_name": "Johnson",
            "email": "sarah.j@example.com",
            "worker_type": "contractor",
            "status": "active",
            "start_date": datetime.now() - timedelta(days=180),
            "department_id": eng_dept.id,
            "job_title": "Software Engineer",
            "hourly_rate": 95.00
        },
        {
            "worker_id": "W00003",
            "first_name": "Michael",
            "last_name": "Chen",
            "email": "m.chen@example.com",
            "worker_type": "eor",
            "status": "active",
            "start_date": datetime.now() - timedelta(days=90),
            "department_id": eng_dept.id,
            "job_title": "DevOps Engineer",
            "hourly_rate": 110.00
        }
    ]
    
    for worker_data in sample_workers:
        worker = Worker(**worker_data)
        db.session.add(worker)
    
    db.session.commit()
    print(f'✅ Created {len(sample_workers)} sample workers')
    print('✅ Database seeded successfully!')

# ============================================================================
# MAIN
# ============================================================================

if __name__ == '__main__':
    # Create tables if they don't exist
    with app.app_context():
        db.create_all()
    
    # Run the app
    app.run(debug=True, port=5000)
