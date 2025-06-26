const pool = require('../db/database');

// Database tables creation
const createTables = async () => {
    try {
        // Create announcements table
        await pool.query(`
            CREATE TABLE IF NOT EXISTS announcements (
                id SERIAL PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                message TEXT NOT NULL,
                priority INTEGER DEFAULT 1,
                active BOOLEAN DEFAULT true,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        `);

        // Create team members table
        await pool.query(`
            CREATE TABLE IF NOT EXISTS team_members (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                role VARCHAR(100) NOT NULL,
                bio TEXT,
                image_url VARCHAR(255),
                email VARCHAR(100),
                linkedin_url VARCHAR(255),
                order_priority INTEGER DEFAULT 1,
                active BOOLEAN DEFAULT true,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        `);

        // Create sponsors table
        await pool.query(`
            CREATE TABLE IF NOT EXISTS sponsors (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                logo_url VARCHAR(255),
                website_url VARCHAR(255),
                sponsor_type VARCHAR(50) DEFAULT 'general',
                description TEXT,
                active BOOLEAN DEFAULT true,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        `);

        // Create sample questions table
        await pool.query(`
            CREATE TABLE IF NOT EXISTS sample_questions (
                id SERIAL PRIMARY KEY,
                subject VARCHAR(50) NOT NULL,
                class_level VARCHAR(20) NOT NULL,
                question_text TEXT NOT NULL,
                option_a VARCHAR(255),
                option_b VARCHAR(255),
                option_c VARCHAR(255),
                option_d VARCHAR(255),
                correct_answer CHAR(1),
                explanation TEXT,
                difficulty_level INTEGER DEFAULT 1,
                active BOOLEAN DEFAULT true,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        `);

        // Create contact submissions table
        await pool.query(`
            CREATE TABLE IF NOT EXISTS contact_submissions (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                email VARCHAR(100) NOT NULL,
                phone VARCHAR(20),
                subject VARCHAR(255),
                message TEXT NOT NULL,
                status VARCHAR(20) DEFAULT 'new',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        `);

        // Create registrations table
        await pool.query(`
            CREATE TABLE IF NOT EXISTS registrations (
                id SERIAL PRIMARY KEY,
                student_name VARCHAR(100) NOT NULL,
                email VARCHAR(100) NOT NULL,
                phone VARCHAR(20),
                school_name VARCHAR(200),
                class_level VARCHAR(20) NOT NULL,
                subjects JSON,
                guardian_name VARCHAR(100),
                guardian_phone VARCHAR(20),
                status VARCHAR(20) DEFAULT 'pending',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        `);

        console.log('✅ All database tables created successfully!');

        // Insert sample data
        await insertSampleData();

    } catch (error) {
        console.error('❌ Error creating tables:', error);
    }
};

// Insert sample data
const insertSampleData = async () => {
    try {
        // Insert sample announcements
        await pool.query(`
            INSERT INTO announcements (title, message, priority) VALUES
            ('QUIZZICLES 2nd Edition Registration Open!', 'Registration for QUIZZICLES 2025 is now open. Register before [DATE] to secure your spot!', 1),
            ('Sample Questions Available', 'Check out our sample questions to prepare for the competition.', 2),
            ('New Sponsors Joined!', 'We welcome our new sponsors who are supporting young talent in Math and Physics.', 3)
            ON CONFLICT DO NOTHING
        `);

        // Insert sample team members
        await pool.query(`
            INSERT INTO team_members (name, role, bio, order_priority) VALUES
            ('Dr. Sarah Johnson', 'Competition Director', 'PhD in Mathematics, passionate about nurturing young mathematical minds.', 1),
            ('Prof. Michael Chen', 'Physics Coordinator', 'Professor of Physics with expertise in competitive physics training.', 2),
            ('Emma Williams', 'Operations Manager', 'Organizing competitions and events for students nationwide.', 3),
            ('Alex Rodriguez', 'Technical Lead', 'Developing digital platforms for seamless competition experience.', 4)
            ON CONFLICT DO NOTHING
        `);

        // Insert sample sponsors
        await pool.query(`
            INSERT INTO sponsors (name, sponsor_type, description) VALUES
            ('MathTech Solutions', 'title', 'Leading provider of educational technology solutions'),
            ('Physics Academy', 'gold', 'Premier physics education institute'),
            ('STEM Foundation', 'silver', 'Supporting STEM education across the country'),
            ('Future Scientists Club', 'bronze', 'Encouraging young scientists and mathematicians')
            ON CONFLICT DO NOTHING
        `);

        // Insert sample questions
        await pool.query(`
            INSERT INTO sample_questions (subject, class_level, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation) VALUES
            ('Math', '10', 'If x² - 5x + 6 = 0, what are the values of x?', 'x = 2, 3', 'x = 1, 6', 'x = -2, -3', 'x = 0, 5', 'A', 'Factoring: (x-2)(x-3) = 0, so x = 2 or x = 3'),
            ('Physics', '11', 'What is the SI unit of force?', 'Joule', 'Newton', 'Watt', 'Pascal', 'B', 'Newton is the SI unit of force, defined as kg⋅m⋅s⁻²'),
            ('Math', '12', 'What is the derivative of sin(x)?', 'cos(x)', '-cos(x)', 'sin(x)', '-sin(x)', 'A', 'The derivative of sin(x) with respect to x is cos(x)')
            ON CONFLICT DO NOTHING
        `);

        console.log('✅ Sample data inserted successfully!');

    } catch (error) {
        console.error('❌ Error inserting sample data:', error);
    }
};

// Run the setup
if (require.main === module) {
    createTables().then(() => {
        console.log('🎯 Database setup completed!');
        process.exit(0);
    });
}

module.exports = { createTables };
