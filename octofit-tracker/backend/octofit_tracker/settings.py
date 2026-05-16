# Custom user model
AUTH_USER_MODEL = 'octofit_tracker.User'


# Database configuration for Djongo and MongoDB
DATABASES = {
	'default': {
		'ENGINE': 'djongo',
		'NAME': 'octofit_db',
		'ENFORCE_SCHEMA': False,
		'CLIENT': {
			'host': 'localhost',
			'port': 27017,
			'username': '',
			'password': '',
			'authSource': 'admin',
			'authMechanism': 'SCRAM-SHA-1',
		},
	}
}

# Application definition
INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'octofit_tracker',
	'rest_framework',
	'djongo',
	'corsheaders',
]

MIDDLEWARE = [
	'corsheaders.middleware.CorsMiddleware',
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# CORS settings
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = ['*']
CORS_ALLOW_METHODS = ['*']

# Allow all hosts, but prefer explicit codespace and localhost
import os
codespace_name = os.environ.get('CODESPACE_NAME')
allowed_hosts = ['localhost', '127.0.0.1']
if codespace_name:
	allowed_hosts.append(f"{codespace_name}-8000.app.github.dev")
ALLOWED_HOSTS = allowed_hosts

