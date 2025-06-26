const pool = require('../db/database');

class Contact {
    static async create(data) {
        try {
            const { name, email, phone, subject, message } = data;
            const result = await pool.query(
                `INSERT INTO contact_submissions (name, email, phone, subject, message) 
                 VALUES ($1, $2, $3, $4, $5) RETURNING *`,
                [name, email, phone, subject, message]
            );
            return result.rows[0];
        } catch (error) {
            console.error('Error creating contact submission:', error);
            return null;
        }
    }

    static async getAll() {
        try {
            const result = await pool.query(
                'SELECT * FROM contact_submissions ORDER BY created_at DESC'
            );
            return result.rows;
        } catch (error) {
            console.error('Error fetching contact submissions:', error);
            return [];
        }
    }

    static async updateStatus(id, status) {
        try {
            const result = await pool.query(
                'UPDATE contact_submissions SET status = $1 WHERE id = $2 RETURNING *',
                [status, id]
            );
            return result.rows[0];
        } catch (error) {
            console.error('Error updating contact submission status:', error);
            return null;
        }
    }
}

module.exports = Contact;
