const express = require('express');
const connectDb = require('./db');
const Food = require('./models/testModel');

connectDb()
const app = express();
app.use(express.json());

app.get('/api', (req, res) => {
    res.json('Hello, API Server!');
})

app.get('/api/foods', async (req, res) => { 
    try {
        const foods = await Food.find();
        res.json(foods);
    } catch (err) {
        console.error(err);
        res.status(500).json({ message: 'Server Error' });
    }
})

app.post('/api/foods', async (req, res) => { 
    const food = new Food(req.body);
    if (!food.name || !food.price || !food.category)
        return res.status(400).json({
        message: 'Please provide all required fields'
    });

    try {
        await food.save();
        res.status(201).json(food);
    } catch (err) {
        console.error(err);
        res.status(400).json({ message: 'Invalid request' });
    }
})

app.delete('/foods/:id', async (req, res) => {
    try {
        const food = await Food.findByIdAndDelete(req.params.id);
        if (!food) return res.status(404).json({ message: 'Food not found' });
        res.json("food deleted successfully");
    } catch (err) { 
        console.error(err);
        res.status(500).json({ message: 'Server Error' });
    }
})

app.listen(8800, () => {
    console.log('Server is running on port 8800');
})