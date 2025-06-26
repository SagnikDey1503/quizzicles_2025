const pool = require('../db/database');

const Registration = {
  async create(data) {
    const {
      student_name,
      email,
      phone,
      school_name,
      class_level,
      guardian_name,
      guardian_phone,
      subjects,
      status = 'pending'  // optional default status
    } = data;

    const query = `
      INSERT INTO registrations 
      (student_name, email, phone, school_name, class_level, guardian_name, guardian_phone, subjects, status)
      VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9)
      RETURNING *;
    `;

    const values = [
      student_name,
      email,
      phone,
      school_name,
      class_level,
      guardian_name || null,
      guardian_phone || null,
      subjects || null,
      status
    ];

    const { rows } = await pool.query(query, values);
    return rows[0];
  }
};

module.exports = Registration;
