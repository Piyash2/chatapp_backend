# Railway Deployment Guide

## Prerequisites
- Railway account
- GitHub repository with your code
- PostgreSQL database already set up on Railway

## Deployment Steps

### 1. Connect Repository to Railway
1. Go to [Railway.app](https://railway.app)
2. Click "New Project"
3. Select "Deploy from GitHub repo"
4. Choose your ChatApp repository
5. Select the `backend` folder as the root directory

### 2. Set Environment Variables
In Railway dashboard, go to your project → Variables tab and add:

```
ENVIRONMENT=production
DEBUG=False
SECRET_KEY=your-super-secret-key-here
ALLOWED_HOSTS=your-railway-domain.railway.app
PG_HOST=metro.proxy.rlwy.net
PG_PORT=36222
PG_PASSWORD=rhGgMVGBxeCWiYuAbniPhqdsOtoaunga
CORS_ALLOWED_ORIGINS=https://your-frontend-domain.com
```

### 3. Deploy
1. Railway will automatically detect the `Procfile` and `requirements.txt`
2. The deployment will start automatically
3. Wait for the build to complete

### 4. Run Migrations
After deployment, run migrations:
1. Go to Railway dashboard → Deployments
2. Click on your deployment
3. Go to "Logs" tab
4. Click "Open Shell" or use Railway CLI:
```bash
railway run python manage.py migrate
```

### 5. Create Superuser (Optional)
```bash
railway run python manage.py createsuperuser
```

## Environment Variables Reference

| Variable | Development | Production | Description |
|----------|-------------|------------|-------------|
| `ENVIRONMENT` | `development` | `production` | Controls database selection |
| `DEBUG` | `True` | `False` | Django debug mode |
| `SECRET_KEY` | `django-insecure-...` | `your-secret-key` | Django secret key |
| `ALLOWED_HOSTS` | `localhost,127.0.0.1` | `your-domain.railway.app` | Allowed hosts |
| `PG_HOST` | Not needed | `metro.proxy.rlwy.net` | PostgreSQL host |
| `PG_PORT` | Not needed | `36222` | PostgreSQL port |
| `PG_PASSWORD` | Not needed | `your-password` | PostgreSQL password |
| `CORS_ALLOWED_ORIGINS` | `http://localhost:5173` | `https://your-frontend.com` | CORS origins |

## Database Configuration

- **Development**: Uses SQLite (`db.sqlite3`)
- **Production**: Uses PostgreSQL on Railway

The database is automatically selected based on the `ENVIRONMENT` variable.

## Static Files

Static files are served using WhiteNoise middleware in production.

## Troubleshooting

### Common Issues:
1. **Database connection failed**: Check PostgreSQL environment variables
2. **Static files not loading**: Ensure WhiteNoise is properly configured
3. **CORS errors**: Update `CORS_ALLOWED_ORIGINS` with your frontend URL
4. **Migration errors**: Run migrations manually in Railway shell

### Useful Commands:
```bash
# Check deployment logs
railway logs

# Open shell
railway shell

# Run migrations
railway run python manage.py migrate

# Collect static files
railway run python manage.py collectstatic --noinput
```

## Security Notes

- Never commit `.env` files to version control
- Use strong, unique secret keys in production
- Keep your PostgreSQL credentials secure
- Regularly update dependencies
