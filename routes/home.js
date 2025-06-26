const express = require('express');
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
        currentPage: 'register',
        error:null
    });
});

// Handle registration form submission
const Registration = require('../models/Registration');

router.post('/register', async (req, res) => {
  const {
    student_name,
    email,
    phone,
    school_name,
    class_level,
    guardian_name,
    guardian_phone,
    subjects
  } = req.body;

  try {
    await Registration.create({
      student_name,
      email,
      phone,
      school_name,
      class_level,
      guardian_name,
      guardian_phone,
      subjects
    });

    res.render('pages/register-success', {
      title: 'Registration Successful - QUIZZICLES',
      currentPage: 'register',
      error: null
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
