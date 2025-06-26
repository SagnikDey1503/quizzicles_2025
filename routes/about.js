const express = require('express');
const router = express.Router();

// About page
router.get('/about', (req, res) => {
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
