const express = require('express');
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
    res.render('C:\\Users\\ajayd\\Downloads\\bib test\\views\\pages\\admin-login', {
        title: 'Admin Login - QUIZZICLES',
        error:null
    });
});

// Handle admin login
router.post('/login', (req, res) => {
    const { username, password } = req.body;

    // Simple hardcoded admin credentials (in production, use proper authentication)
    if (username === 'admin' && password === 'hello') {
        req.session.admin = true;
        res.redirect('/admin/dashboard');
    } else {
        res.render('pages/admin-login', {
            title: 'Admin Login - QUIZZICLES',
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
