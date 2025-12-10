#!/bin/bash

# Navigate to the Django project directory
cd biblioteca_virtual

# Run migrations
echo "Running database migrations..."
python manage.py makemigrations
python manage.py migrate

# Create superuser if it doesn't exist
echo "Creating superuser if it doesn't exist..."
python manage.py shell -c "
from usuarios.models import Usuario
if not Usuario.objects.filter(username='admin').exists():
    Usuario.objects.create_superuser('admin', 'admin@example.com', 'admin')
    print('Superuser created: admin/admin')
else:
    print('Superuser already exists')
"

# Start server
echo "Starting Django server..."
if [ $# -eq 0 ]; then
    # Default command if no arguments provided
    exec python manage.py runserver 0.0.0.0:8000
else
    # Execute the provided command from the biblioteca_virtual directory
    exec "$@"
fi