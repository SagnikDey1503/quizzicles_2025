const { Pool } = require('pg');
require('dotenv').config();

// Database connection pool
const pool = new Pool({
    host: process.env.DB_HOST || 'localhost',
    port: process.env.DB_PORT || 5432,
    database: process.env.DB_NAME || 'quizzicles_db',
    user: process.env.DB_USER,
    password: process.env.DB_PASSWORD,
    max: 20,
    idleTimeoutMillis: 30000,
    connectionTimeoutMillis: 2000,
});

// Test connection
pool.on('connect', () => {
    console.log('🔗 Connected to PostgreSQL database');
});

pool.on('error', (err) => {
    console.error('💥 Database connection error:', err);
    process.exit(-1);
});

module.exports = pool;
