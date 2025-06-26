const express = require('express');
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
