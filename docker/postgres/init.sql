CREATE USER develops_today_user WITH PASSWORD 'develops_today_password';

CREATE DATABASE develops_today_db;
GRANT ALL PRIVILEGES ON DATABASE develops_today_db TO develops_today_user;