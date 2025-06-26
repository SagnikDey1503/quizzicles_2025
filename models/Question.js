const pool = require('../db/database');

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
