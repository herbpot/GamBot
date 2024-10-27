import { Router } from 'express'
import { setDataBase } from '../controllers/settings'

export const setting = Router()

setting.post('/verificate', setDataBase)
setting.get('/', () => {console.log("fesdfs")})