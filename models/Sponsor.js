const pool = require('../db/database');

class Sponsor {
    static async getAll() {
        try {
            const result = await pool.query(
                'SELECT * FROM sponsors WHERE active = true ORDER BY sponsor_type, name ASC'
            );
            return result.rows;
        } catch (error) {
            console.error('Error fetching sponsors:', error);
            return [];
        }
    }

    static async getByType(type) {
        try {
            const result = await pool.query(
                'SELECT * FROM sponsors WHERE active = true AND sponsor_type = $1 ORDER BY name ASC',
                [type]
            );
            return result.rows;
        } catch (error) {
            console.error('Error fetching sponsors by type:', error);
            return [];
        }
    }

    static async create(data) {
        try {
            const { name, logo_url, website_url, sponsor_type = 'general', description } = data;
            const result = await pool.query(
                `INSERT INTO sponsors (name, logo_url, website_url, sponsor_type, description) 
                 VALUES ($1, $2, $3, $4, $5) RETURNING *`,
                [name, logo_url, website_url, sponsor_type, description]
            );
            return result.rows[0];
        } catch (error) {
            console.error('Error creating sponsor:', error);
            return null;
        }
    }
}

module.exports = Sponsor;
