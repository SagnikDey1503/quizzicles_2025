const express = require('express');
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
