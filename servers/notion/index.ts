import dotenv from 'dotenv'
import express from 'express'
import { setting } from './routes/setting'
import { diary } from './routes/diary'
import mongoose from 'mongoose'

dotenv.config()
const app = express()

app.use(express.json());

app.use('/setting', setting)
app.use('/diary', diary)

mongoose.connect(process.env.MONGO_URI!!).then(() => {
    console.log('MongoDB connected');
  }).catch((err) => {
    console.error('MongoDB connection error:', err);
  });

app.listen(process.env.PORT, () => {
    console.log(`server is on localhost:${process.env.PORT}`)
})