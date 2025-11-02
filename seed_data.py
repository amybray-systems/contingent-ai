"""
Seed data for ContingentAI - Realistic workforce data based on your Upwork/VG experience
"""

import random
from datetime import datetime, timedelta

# DEPARTMENTS - Based on typical tech company structure
DEPARTMENTS = [
    {"name": "Engineering", "code": "ENG", "budget_annual": 5000000, "headcount_target": 120},
    {"name": "Product", "code": "PRD", "budget_annual": 1500000, "headcount_target": 25},
    {"name": "Design", "code": "DES", "budget_annual": 800000, "headcount_target": 15},
    {"name": "Marketing", "code": "MKT", "budget_annual": 1200000, "headcount_target": 30},
    {"name": "Sales", "code": "SAL", "budget_annual": 2000000, "headcount_target": 40},
    {"name": "Customer Success", "code": "CS", "budget_annual": 900000, "headcount_target": 25},
    {"name": "Operations", "code": "OPS", "budget_annual": 600000, "headcount_target": 12},
    {"name": "Finance", "code": "FIN", "budget_annual": 500000, "headcount_target": 10},
]

# LOCATIONS - Based on your 20+ countries experience
LOCATIONS = [
    {"country": "United States", "state_province": "California", "city": "San Francisco", "region": "North America", "timezone": "America/Los_Angeles", "currency": "USD"},
    {"country": "United States", "state_province": "New York", "city": "New York", "region": "North America", "timezone": "America/New_York", "currency": "USD"},
    {"country": "United States", "state_province": "Texas", "city": "Austin", "region": "North America", "timezone": "America/Chicago", "currency": "USD"},
    {"country": "Canada", "state_province": "Ontario", "city": "Toronto", "region": "North America", "timezone": "America/Toronto", "currency": "CAD"},
    {"country": "United Kingdom", "state_province": "England", "city": "London", "region": "EMEA", "timezone": "Europe/London", "currency": "GBP"},
    {"country": "Germany", "state_province": "Berlin", "city": "Berlin", "region": "EMEA", "timezone": "Europe/Berlin", "currency": "EUR"},
    {"country": "France", "state_province": "Île-de-France", "city": "Paris", "region": "EMEA", "timezone": "Europe/Paris", "currency": "EUR"},
    {"country": "Poland", "state_province": "Mazovia", "city": "Warsaw", "region": "EMEA", "timezone": "Europe/Warsaw", "currency": "PLN"},
    {"country": "India", "state_province": "Karnataka", "city": "Bangalore", "region": "APAC", "timezone": "Asia/Kolkata", "currency": "INR"},
    {"country": "Singapore", "state_province": "Singapore", "city": "Singapore", "region": "APAC", "timezone": "Asia/Singapore", "currency": "SGD"},
    {"country": "Australia", "state_province": "New South Wales", "city": "Sydney", "region": "APAC", "timezone": "Australia/Sydney", "currency": "AUD"},
    {"country": "Philippines", "state_province": "Metro Manila", "city": "Manila", "region": "APAC", "timezone": "Asia/Manila", "currency": "PHP"},
    {"country": "Brazil", "state_province": "São Paulo", "city": "São Paulo", "region": "LATAM", "timezone": "America/Sao_Paulo", "currency": "BRL"},
    {"country": "Mexico", "state_province": "Mexico City", "city": "Mexico City", "region": "LATAM", "timezone": "America/Mexico_City", "currency": "MXN"},
]

# VENDORS - Based on your EOR/staffing agency experience
VENDORS = [
    {
        "name": "Velocity Global",
        "vendor_type": "eor",
        "contact_name": "Sarah Johnson",
        "contact_email": "sarah.johnson@velocityglobal.com",
        "contact_phone": "+1-303-555-0100",
        "website": "https://velocityglobal.com",
        "services_offered": "EOR services, payroll, benefits, compliance",
        "regions_covered": "Global - 185+ countries",
        "status": "active"
    },
    {
        "name": "Remote",
        "vendor_type": "eor",
        "contact_name": "Michael Chen",
        "contact_email": "m.chen@remote.com",
        "contact_phone": "+1-415-555-0200",
        "website": "https://remote.com",
        "services_offered": "EOR, contractor management, payroll",
        "regions_covered": "Global - 70+ countries",
        "status": "active"
    },
    {
        "name": "Deel",
        "vendor_type": "eor",
        "contact_name": "Anna Kowalski",
        "contact_email": "anna@deel.com",
        "contact_phone": "+1-646-555-0300",
        "website": "https://deel.com",
        "services_offered": "EOR, contractor payments, compliance",
        "regions_covered": "Global - 150+ countries",
        "status": "active"
    },
    {
        "name": "Robert Half Technology",
        "vendor_type": "staffing",
        "contact_name": "David Martinez",
        "contact_email": "david.martinez@roberthalf.com",
        "contact_phone": "+1-650-555-0400",
        "website": "https://roberthalf.com",
        "services_offered": "IT staffing, contract placements, temp-to-perm",
        "regions_covered": "North America, Europe",
        "status": "active"
    },
    {
        "name": "Toptal",
        "vendor_type": "staffing",
        "contact_name": "Elena Petrov",
        "contact_email": "elena@toptal.com",
        "contact_phone": "+1-415-555-0500",
        "website": "https://toptal.com",
        "services_offered": "Elite freelance developers, designers, finance experts",
        "regions_covered": "Global",
        "status": "active"
    },
]

# JOB TITLES by department
JOB_TITLES = {
    "Engineering": [
        ("Software Engineer", 75, 95, 150000, 180000),
        ("Senior Software Engineer", 95, 135, 180000, 220000),
        ("Staff Engineer", 125, 165, 220000, 280000),
        ("Engineering Manager", 130, 170, 200000, 250000),
        ("DevOps Engineer", 80, 110, 160000, 200000),
        ("QA Engineer", 60, 85, 120000, 150000),
    ],
    "Product": [
        ("Product Manager", 85, 120, 140000, 180000),
        ("Senior Product Manager", 110, 150, 180000, 220000),
        ("Product Designer", 70, 100, 130000, 160000),
    ],
    "Design": [
        ("UI/UX Designer", 65, 95, 110000, 140000),
        ("Senior Designer", 85, 120, 140000, 170000),
        ("Design Lead", 100, 140, 160000, 200000),
    ],
    "Marketing": [
        ("Marketing Manager", 70, 95, 120000, 150000),
        ("Content Writer", 50, 75, 80000, 110000),
        ("SEO Specialist", 60, 85, 100000, 130000),
        ("Marketing Analyst", 65, 90, 110000, 140000),
    ],
    "Sales": [
        ("Account Executive", 60, 85, 100000, 140000),
        ("Sales Development Rep", 40, 60, 70000, 90000),
        ("Sales Manager", 80, 110, 140000, 180000),
    ],
    "Customer Success": [
        ("Customer Success Manager", 60, 85, 100000, 130000),
        ("Support Specialist", 40, 60, 70000, 95000),
        ("Technical Account Manager", 75, 105, 120000, 150000),
    ],
    "Operations": [
        ("Operations Manager", 70, 95, 120000, 150000),
        ("Business Analyst", 65, 90, 110000, 140000),
        ("HR Business Partner", 70, 95, 115000, 145000),
    ],
    "Finance": [
        ("Financial Analyst", 65, 90, 105000, 135000),
        ("Senior Financial Analyst", 85, 115, 135000, 165000),
        ("Accounting Manager", 80, 110, 130000, 160000),
    ],
}

# Generate realistic workers
def generate_workers(num_workers=200):
    """Generate realistic worker data"""
    workers = []
    
    # Distribution: 50% FTE, 35% Contractor, 15% EOR
    worker_types = (
        ["fte"] * int(num_workers * 0.50) + 
        ["contractor"] * int(num_workers * 0.35) + 
        ["eor"] * int(num_workers * 0.15)
    )
    random.shuffle(worker_types)
    
    first_names = ["John", "Jane", "Michael", "Sarah", "David", "Emily", "James", "Emma", 
                   "Robert", "Olivia", "William", "Ava", "Richard", "Sophia", "Maria",
                   "Chen", "Priya", "Mohammed", "Yuki", "Fatima", "Luis", "Ananya"]
    
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller",
                  "Davis", "Rodriguez", "Martinez", "Anderson", "Taylor", "Thomas", "Lee",
                  "Kumar", "Patel", "Singh", "Wong", "Chen", "Kim", "Nguyen", "Lopez"]
    
    for i, worker_type in enumerate(worker_types, start=1):
        # Pick random department and location
        dept = random.choice(DEPARTMENTS)
        location = random.choice(LOCATIONS)
        
        # Pick job title based on department
        job_titles_for_dept = JOB_TITLES.get(dept["name"], [("Specialist", 60, 85, 100000, 130000)])
        job_title, hourly_min, hourly_max, salary_min, salary_max = random.choice(job_titles_for_dept)
        
        # Status: 85% active, 10% inactive, 5% terminated
        status_roll = random.random()
        if status_roll < 0.85:
            status = "active"
        elif status_roll < 0.95:
            status = "inactive"
        else:
            status = "terminated"
        
        # Start date (random in last 2 years)
        start_date = datetime.now() - timedelta(days=random.randint(30, 730))
        
        # End date (only if inactive or terminated)
        end_date = None
        if status in ["inactive", "terminated"]:
            end_date = start_date + timedelta(days=random.randint(180, 600))
        
        # Rates/salary
        hourly_rate = None
        annual_salary = None
        
        if worker_type in ["contractor", "eor"]:
            hourly_rate = round(random.uniform(hourly_min, hourly_max), 2)
        else:  # FTE
            annual_salary = round(random.uniform(salary_min, salary_max), -3)  # Round to nearest $1000
        
        # Vendor (only for contractors and EOR)
        vendor = None
        if worker_type in ["contractor", "eor"]:
            vendor = random.choice(VENDORS)["name"]
        
        worker = {
            "worker_id": f"W{i:05d}",
            "first_name": random.choice(first_names),
            "last_name": random.choice(last_names),
            "email": f"worker{i}@example.com",
            "worker_type": worker_type,
            "status": status,
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d") if end_date else None,
            "department": dept["name"],
            "location": f"{location['city']}, {location['country']}",
            "vendor": vendor,
            "manager_name": f"{random.choice(first_names)} {random.choice(last_names)}",
            "job_title": job_title,
            "job_level": random.choice(["Junior", "Mid", "Senior", "Lead", "Principal"]),
            "hourly_rate": hourly_rate,
            "annual_salary": annual_salary,
        }
        
        workers.append(worker)
    
    return workers

# Generate cost history (last 12 months)
def generate_costs(workers):
    """Generate monthly cost data for each worker"""
    costs = []
    
    for worker in workers:
        if worker["status"] != "active":
            continue
        
        # Generate 12 months of data
        for month_offset in range(12):
            period_end = datetime.now() - timedelta(days=30 * month_offset)
            period_start = period_end - timedelta(days=30)
            
            # Calculate cost
            if worker["worker_type"] in ["contractor", "eor"]:
                hours_worked = random.uniform(140, 180)  # ~35-45 hrs/week
                cost = hours_worked * worker["hourly_rate"]
                
                # Add EOR fees for EOR workers
                if worker["worker_type"] == "eor":
                    eor_fee = cost * 0.12  # 12% markup
                    costs.append({
                        "worker_id": worker["worker_id"],
                        "department": worker["department"],
                        "vendor": worker["vendor"],
                        "period_start": period_start.strftime("%Y-%m-%d"),
                        "period_end": period_end.strftime("%Y-%m-%d"),
                        "hours_worked": round(hours_worked, 2),
                        "cost_amount": round(eor_fee, 2),
                        "cost_type": "fees"
                    })
                    
                costs.append({
                    "worker_id": worker["worker_id"],
                    "department": worker["department"],
                    "vendor": worker["vendor"],
                    "period_start": period_start.strftime("%Y-%m-%d"),
                    "period_end": period_end.strftime("%Y-%m-%d"),
                    "hours_worked": round(hours_worked, 2),
                    "cost_amount": round(cost, 2),
                    "cost_type": "salary"
                })
            else:  # FTE
                monthly_salary = worker["annual_salary"] / 12
                
                # Add benefits cost (30% of salary)
                benefits = monthly_salary * 0.30
                
                costs.append({
                    "worker_id": worker["worker_id"],
                    "department": worker["department"],
                    "vendor": None,
                    "period_start": period_start.strftime("%Y-%m-%d"),
                    "period_end": period_end.strftime("%Y-%m-%d"),
                    "hours_worked": 160.0,
                    "cost_amount": round(monthly_salary, 2),
                    "cost_type": "salary"
                })
                
                costs.append({
                    "worker_id": worker["worker_id"],
                    "department": worker["department"],
                    "vendor": None,
                    "period_start": period_start.strftime("%Y-%m-%d"),
                    "period_end": period_end.strftime("%Y-%m-%d"),
                    "hours_worked": 0.0,
                    "cost_amount": round(benefits, 2),
                    "cost_type": "benefits"
                })
    
    return costs

# Generate vendor performance data
def generate_vendor_performance():
    """Generate monthly performance metrics for each vendor"""
    performance = []
    
    for vendor in VENDORS:
        for month_offset in range(12):
            metric_date = (datetime.now() - timedelta(days=30 * month_offset)).strftime("%Y-%m-%d")
            
            # Realistic performance metrics
            performance.append({
                "vendor": vendor["name"],
                "metric_date": metric_date,
                "fill_rate": round(random.uniform(75, 95), 2),
                "avg_time_to_fill": random.randint(14, 45),
                "quality_score": round(random.uniform(3.5, 5.0), 2),
                "cost_competitiveness": round(random.uniform(85, 105), 2),  # % of market rate
                "compliance_score": round(random.uniform(4.0, 5.0), 2),
            })
    
    return performance

# Main function to generate all seed data
if __name__ == "__main__":
    print("Generating seed data for ContingentAI...")
    
    workers = generate_workers(200)
    costs = generate_costs(workers)
    performance = generate_vendor_performance()
    
    print(f"✅ Generated {len(workers)} workers")
    print(f"✅ Generated {len(costs)} cost records")
    print(f"✅ Generated {len(performance)} vendor performance records")
    
    # You can save these to CSV or insert directly into database
    # For now, let's just show sample output
    
    print("\n📊 Sample Worker:")
    print(workers[0])
    
    print("\n💰 Sample Cost:")
    print(costs[0])
    
    print("\n📈 Sample Vendor Performance:")
    print(performance[0])
    
    print("\n✨ Seed data ready! Use this data to populate your database.")
