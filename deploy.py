#!/usr/bin/env python
"""
Deployment helper script for Railway
"""
import os
import subprocess
import sys

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"Running: {description}")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✓ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ {description} failed: {e}")
        print(f"Error output: {e.stderr}")
        return False

def main():
    """Main deployment function"""
    print("Railway Deployment Helper")
    print("=" * 30)
    
    # Set production environment
    os.environ['ENVIRONMENT'] = 'production'
    os.environ['DEBUG'] = 'False'
    
    print("\n1. Collecting static files...")
    if not run_command("python manage.py collectstatic --noinput", "Collecting static files"):
        print("Failed to collect static files")
        sys.exit(1)
    
    print("\n2. Running migrations...")
    if not run_command("python manage.py migrate", "Running migrations"):
        print("Failed to run migrations")
        sys.exit(1)
    
    print("\n3. Checking deployment...")
    if not run_command("python manage.py check --deploy", "Checking deployment settings"):
        print("Deployment check failed")
        sys.exit(1)
    
    print("\n" + "=" * 30)
    print("✓ Deployment preparation completed!")
    print("\nNext steps:")
    print("1. Push your code to GitHub")
    print("2. Deploy on Railway")
    print("3. Set environment variables in Railway dashboard")
    print("4. Run migrations: railway run python manage.py migrate")

if __name__ == '__main__':
    main()
