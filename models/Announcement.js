const pool = require('../db/database');

class Announcement {
    static async getAll() {
        try {
            const result = await pool.query(
                'SELECT * FROM announcements WHERE active = true ORDER BY priority ASC, created_at DESC'
            );
            return result.rows;
        } catch (error) {
            console.error('Error fetching announcements:', error);
            return [];
        }
    }

    static async getById(id) {
        try {
            const result = await pool.query('SELECT * FROM announcements WHERE id = $1', [id]);
            return result.rows[0];
        } catch (error) {
            console.error('Error fetching announcement:', error);
            return null;
        }
    }

    static async create(data) {
        try {
            const { title, message, priority = 1 } = data;
            const result = await pool.query(
                'INSERT INTO announcements (title, message, priority) VALUES ($1, $2, $3) RETURNING *',
                [title, message, priority]
            );
            return result.rows[0];
        } catch (error) {
            console.error('Error creating announcement:', error);
            return null;
        }
    }
}

module.exports = Announcement;
