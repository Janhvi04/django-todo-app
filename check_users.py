"""
Quick script to check if users are being created in the database.
Run this with: python manage.py shell < check_users.py
Or run: python manage.py shell and then paste the code below.
"""

from django.contrib.auth.models import User

# Check all users
all_users = User.objects.all()
print(f"\nTotal users in database: {all_users.count()}\n")

if all_users.exists():
    print("Users found:")
    for user in all_users:
        print(f"  - Username: {user.username}, Email: {user.email}, Date Joined: {user.date_joined}")
else:
    print("No users found in database!")
    print("\nThis could mean:")
    print("1. No one has signed up yet")
    print("2. Signup is failing silently (check for errors)")
    print("3. Database migrations haven't been run")






