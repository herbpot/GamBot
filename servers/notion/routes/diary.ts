import { Router } from 'express'
import { setDiary } from '../controllers/diary'

export const diary = Router()

diary.post('/set', setDiary)
diary.get('/', () => {console.log("fesdfs")})