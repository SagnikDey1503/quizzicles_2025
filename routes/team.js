const express = require('express');
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
