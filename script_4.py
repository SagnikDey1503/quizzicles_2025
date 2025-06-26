# Create route files

# Home routes
home_routes = """const express = require('express');
const router = express.Router();
const Announcement = require('../models/Announcement');
const Sponsor = require('../models/Sponsor');

// Home page
router.get('/', async (req, res) => {
    try {
        const announcements = await Announcement.getAll();
        const sponsors = await Sponsor.getAll();
        
        res.render('pages/home', {
            title: 'QUIZZICLES - Annual Math & Physics Competition',
            announcements,
            sponsors,
            currentPage: 'home'
        });
    } catch (error) {
        console.error('Error loading home page:', error);
        res.render('pages/error', { 
            title: 'Error',
            message: 'Failed to load home page' 
        });
    }
});

// Registration page
router.get('/register', (req, res) => {
    res.render('pages/register', {
        title: 'Register - QUIZZICLES',
        currentPage: 'register'
    });
});

// Handle registration form submission
router.post('/register', async (req, res) => {
    try {
        // Registration logic would go here
        res.render('pages/register-success', {
            title: 'Registration Successful - QUIZZICLES',
            currentPage: 'register'
        });
    } catch (error) {
        console.error('Error processing registration:', error);
        res.render('pages/register', {
            title: 'Register - QUIZZICLES',
            currentPage: 'register',
            error: 'Registration failed. Please try again.'
        });
    }
});

module.exports = router;
"""

# About routes
about_routes = """const express = require('express');
const router = express.Router();

// About page
router.get('/', (req, res) => {
    res.render('pages/about', {
        title: 'About QUIZZICLES - Competition Details',
        currentPage: 'about'
    });
});

// Competition format
router.get('/format', (req, res) => {
    res.render('pages/format', {
        title: 'Competition Format - QUIZZICLES',
        currentPage: 'about'
    });
});

// Rules and regulations
router.get('/rules', (req, res) => {
    res.render('pages/rules', {
        title: 'Rules & Regulations - QUIZZICLES',
        currentPage: 'about'
    });
});

// Timeline
router.get('/timeline', (req, res) => {
    res.render('pages/timeline', {
        title: 'Competition Timeline - QUIZZICLES',
        currentPage: 'about'
    });
});

module.exports = router;
"""

# Questions routes
questions_routes = """const express = require('express');
const router = express.Router();
const Question = require('../models/Question');

// Sample questions page
router.get('/', async (req, res) => {
    try {
        const questions = await Question.getAll();
        
        // Group questions by subject and class
        const groupedQuestions = questions.reduce((acc, question) => {
            const key = `${question.subject}_${question.class_level}`;
            if (!acc[key]) {
                acc[key] = {
                    subject: question.subject,
                    class_level: question.class_level,
                    questions: []
                };
            }
            acc[key].questions.push(question);
            return acc;
        }, {});

        res.render('pages/questions', {
            title: 'Sample Questions - QUIZZICLES',
            groupedQuestions: Object.values(groupedQuestions),
            currentPage: 'questions'
        });
    } catch (error) {
        console.error('Error loading questions:', error);
        res.render('pages/error', { 
            title: 'Error',
            message: 'Failed to load sample questions' 
        });
    }
});

// Questions by subject
router.get('/subject/:subject', async (req, res) => {
    try {
        const questions = await Question.getBySubject(req.params.subject);
        res.render('pages/questions-by-subject', {
            title: `${req.params.subject} Questions - QUIZZICLES`,
            questions,
            subject: req.params.subject,
            currentPage: 'questions'
        });
    } catch (error) {
        console.error('Error loading questions by subject:', error);
        res.render('pages/error', { 
            title: 'Error',
            message: 'Failed to load questions' 
        });
    }
});

// Questions by class
router.get('/class/:class', async (req, res) => {
    try {
        const questions = await Question.getByClass(req.params.class);
        res.render('pages/questions-by-class', {
            title: `Class ${req.params.class} Questions - QUIZZICLES`,
            questions,
            classLevel: req.params.class,
            currentPage: 'questions'
        });
    } catch (error) {
        console.error('Error loading questions by class:', error);
        res.render('pages/error', { 
            title: 'Error',
            message: 'Failed to load questions' 
        });
    }
});

module.exports = router;
"""

# Team routes
team_routes = """const express = require('express');
const router = express.Router();
const TeamMember = require('../models/TeamMember');

// Team page
router.get('/', async (req, res) => {
    try {
        const teamMembers = await TeamMember.getAll();
        
        res.render('pages/team', {
            title: 'Meet Our Team - QUIZZICLES',
            teamMembers,
            currentPage: 'team'
        });
    } catch (error) {
        console.error('Error loading team page:', error);
        res.render('pages/error', { 
            title: 'Error',
            message: 'Failed to load team information' 
        });
    }
});

module.exports = router;
"""

# Contact routes
contact_routes = """const express = require('express');
const router = express.Router();
const Contact = require('../models/Contact');

// Contact page
router.get('/', (req, res) => {
    res.render('pages/contact', {
        title: 'Contact Us - QUIZZICLES',
        currentPage: 'contact'
    });
});

// Handle contact form submission
router.post('/', async (req, res) => {
    try {
        const { name, email, phone, subject, message } = req.body;
        
        // Basic validation
        if (!name || !email || !message) {
            return res.render('pages/contact', {
                title: 'Contact Us - QUIZZICLES',
                currentPage: 'contact',
                error: 'Please fill in all required fields.'
            });
        }

        // Save to database
        const contact = await Contact.create({
            name,
            email,
            phone,
            subject,
            message
        });

        if (contact) {
            res.render('pages/contact-success', {
                title: 'Message Sent - QUIZZICLES',
                currentPage: 'contact'
            });
        } else {
            throw new Error('Failed to save contact submission');
        }
    } catch (error) {
        console.error('Error processing contact form:', error);
        res.render('pages/contact', {
            title: 'Contact Us - QUIZZICLES',
            currentPage: 'contact',
            error: 'Failed to send message. Please try again.'
        });
    }
});

module.exports = router;
"""

# Admin routes
admin_routes = """const express = require('express');
const router = express.Router();
const Contact = require('../models/Contact');
const Announcement = require('../models/Announcement');

// Simple admin authentication middleware
const requireAuth = (req, res, next) => {
    if (req.session.admin) {
        next();
    } else {
        res.redirect('/admin/login');
    }
};

// Admin login page
router.get('/login', (req, res) => {
    res.render('pages/admin-login', {
        title: 'Admin Login - QUIZZICLES',
        currentPage: 'admin'
    });
});

// Handle admin login
router.post('/login', (req, res) => {
    const { username, password } = req.body;
    
    // Simple hardcoded admin credentials (in production, use proper authentication)
    if (username === 'admin' && password === 'quizzicles2025') {
        req.session.admin = true;
        res.redirect('/admin/dashboard');
    } else {
        res.render('pages/admin-login', {
            title: 'Admin Login - QUIZZICLES',
            currentPage: 'admin',
            error: 'Invalid credentials'
        });
    }
});

// Admin dashboard
router.get('/dashboard', requireAuth, async (req, res) => {
    try {
        const contacts = await Contact.getAll();
        const announcements = await Announcement.getAll();
        
        res.render('pages/admin-dashboard', {
            title: 'Admin Dashboard - QUIZZICLES',
            contacts,
            announcements,
            currentPage: 'admin'
        });
    } catch (error) {
        console.error('Error loading admin dashboard:', error);
        res.render('pages/error', { 
            title: 'Error',
            message: 'Failed to load admin dashboard' 
        });
    }
});

// Admin logout
router.get('/logout', (req, res) => {
    req.session.destroy();
    res.redirect('/admin/login');
});

module.exports = router;
"""

# Write route files
with open('./quizzicles/routes/home.js', 'w') as f:
    f.write(home_routes)

with open('./quizzicles/routes/about.js', 'w') as f:
    f.write(about_routes)

with open('./quizzicles/routes/questions.js', 'w') as f:
    f.write(questions_routes)

with open('./quizzicles/routes/team.js', 'w') as f:
    f.write(team_routes)

with open('./quizzicles/routes/contact.js', 'w') as f:
    f.write(contact_routes)

with open('./quizzicles/routes/admin.js', 'w') as f:
    f.write(admin_routes)

print("✅ Route files created:")
print("   📄 routes/home.js")
print("   📄 routes/about.js")
print("   📄 routes/questions.js")
print("   📄 routes/team.js")
print("   📄 routes/contact.js")
print("   📄 routes/admin.js")