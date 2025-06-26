# Create models for database operations
announcement_model = """const pool = require('../db/database');

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
"""

team_model = """const pool = require('../db/database');

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
"""

sponsor_model = """const pool = require('../db/database');

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
"""

question_model = """const pool = require('../db/database');

class Question {
    static async getAll() {
        try {
            const result = await pool.query(
                'SELECT * FROM sample_questions WHERE active = true ORDER BY subject, class_level, created_at ASC'
            );
            return result.rows;
        } catch (error) {
            console.error('Error fetching questions:', error);
            return [];
        }
    }

    static async getBySubject(subject) {
        try {
            const result = await pool.query(
                'SELECT * FROM sample_questions WHERE active = true AND subject = $1 ORDER BY class_level, created_at ASC',
                [subject]
            );
            return result.rows;
        } catch (error) {
            console.error('Error fetching questions by subject:', error);
            return [];
        }
    }

    static async getByClass(classLevel) {
        try {
            const result = await pool.query(
                'SELECT * FROM sample_questions WHERE active = true AND class_level = $1 ORDER BY subject, created_at ASC',
                [classLevel]
            );
            return result.rows;
        } catch (error) {
            console.error('Error fetching questions by class:', error);
            return [];
        }
    }

    static async create(data) {
        try {
            const { 
                subject, class_level, question_text, option_a, option_b, 
                option_c, option_d, correct_answer, explanation, difficulty_level = 1 
            } = data;
            const result = await pool.query(
                `INSERT INTO sample_questions 
                 (subject, class_level, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level) 
                 VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10) RETURNING *`,
                [subject, class_level, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level]
            );
            return result.rows[0];
        } catch (error) {
            console.error('Error creating question:', error);
            return null;
        }
    }
}

module.exports = Question;
"""

contact_model = """const pool = require('../db/database');

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
"""

# Write model files
with open('./quizzicles/models/Announcement.js', 'w') as f:
    f.write(announcement_model)

with open('./quizzicles/models/TeamMember.js', 'w') as f:
    f.write(team_model)

with open('./quizzicles/models/Sponsor.js', 'w') as f:
    f.write(sponsor_model)

with open('./quizzicles/models/Question.js', 'w') as f:
    f.write(question_model)

with open('./quizzicles/models/Contact.js', 'w') as f:
    f.write(contact_model)

print("✅ Model files created:")
print("   📄 models/Announcement.js")
print("   📄 models/TeamMember.js")
print("   📄 models/Sponsor.js")
print("   📄 models/Question.js")
print("   📄 models/Contact.js")