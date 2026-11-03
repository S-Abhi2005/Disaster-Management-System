# adminlogin.py - Run this in backend folder
from app.core.database import SessionLocal
from app.core.security import hash_password
from app.users.models import User
from app.auth.schemas import Role

def seed_admin():
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.email == "admin@test.com").first()
        hashed = hash_password("admin1234")
        if user:
            print("Admin already exists. Updating password...")
            user.hashed_password = hashed
            user.role = Role.ADMIN
        else:
            print("Creating new admin...")
            user = User(
                full_name="Admin User",
                email="admin@test.com",
                phone_number="7777777777",
                hashed_password=hashed,
                city="Hyderabad",
                role=Role.ADMIN
            )
            db.add(user)
        db.commit()
        print("Admin ready: admin@test.com / admin1234")
    finally:
        db.close()

if __name__ == "__main__":
    seed_admin()