const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const session = require('express-session');
require('dotenv').config();

// Import routes
const homeRoutes = require('./routes/home');
const aboutRoutes = require('./routes/about');
const questionsRoutes = require('./routes/questions');
const teamRoutes = require('./routes/team');
const contactRoutes = require('./routes/contact');
const adminRoutes = require('./routes/admin');

const app = express();

// View engine setup
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

// Static files
app.use(express.static(path.join(__dirname, 'public')));

// Body parser middleware
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

// Session middleware
app.use(session({
    secret: process.env.SESSION_SECRET || 'quizzicles-secret-key',
    resave: false,
    saveUninitialized: false,
    cookie: { secure: false }
}));

// Make environment variables available to views
app.use((req, res, next) => {
    res.locals.siteName = process.env.SITE_NAME || 'QUIZZICLES';
    res.locals.competitionYear = process.env.COMPETITION_YEAR || '2025';
    res.locals.editionNumber = process.env.EDITION_NUMBER || '2';
    next();
});

// Routes
app.use('/', homeRoutes);
app.use('/about', aboutRoutes);
app.use('/questions', questionsRoutes);
app.use('/team', teamRoutes);
app.use('/contact', contactRoutes);
app.use('/admin', adminRoutes);

// 404 Error handler
app.use((req, res) => {
    res.status(404).render('pages/404', { 
        title: '404 - Page Not Found',
        message: 'The page you are looking for does not exist.'
    });
});

// Error handler
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).render('pages/error', { 
        title: 'Error',
        message: 'Something went wrong! Please try again later.'
    });
});

// Start server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`🚀 QUIZZICLES server running on port ${PORT}`);
    console.log(`🌐 Visit: http://localhost:${PORT}`);
    console.log(`📚 Competition Year: ${process.env.COMPETITION_YEAR || '2025'}`);
    console.log(`🏆 Edition: ${process.env.EDITION_NUMBER || '2nd'}`);
});
