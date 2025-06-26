const pool = require('../db/database');

class TeamMember {
    static async getAll() {
        try {
            const result = await pool.query(
                'SELECT * FROM team_members WHERE active = true ORDER BY order_priority ASC, created_at ASC'
            );
            return result.rows;
        } catch (error) {
            console.error('Error fetching team members:', error);
            return [];
        }
    }

    static async getById(id) {
        try {
            const result = await pool.query('SELECT * FROM team_members WHERE id = $1', [id]);
            return result.rows[0];
        } catch (error) {
            console.error('Error fetching team member:', error);
            return null;
        }
    }

    static async create(data) {
        try {
            const { name, role, bio, email, linkedin_url, image_url, order_priority = 1 } = data;
            const result = await pool.query(
                `INSERT INTO team_members (name, role, bio, email, linkedin_url, image_url, order_priority) 
                 VALUES ($1, $2, $3, $4, $5, $6, $7) RETURNING *`,
                [name, role, bio, email, linkedin_url, image_url, order_priority]
            );
            return result.rows[0];
        } catch (error) {
            console.error('Error creating team member:', error);
            return null;
        }
    }
}

module.exports = TeamMember;
