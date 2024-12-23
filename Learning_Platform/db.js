const mongoose = require('mongoose');

const connectDb = async () => {
    try {
        const conn = await mongoose.connect("mongodb://root:example@localhost:27017/learningapp?authSource=admin");
        console.log(`Connected to MongoDB: ${conn.connection.host}`);
    } catch (err) {
        console.error("Failed to connect to MongoDB", err);
        process.exit(1);
    }
};

module.exports = connectDb;