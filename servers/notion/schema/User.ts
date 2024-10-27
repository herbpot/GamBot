import { Schema, model } from 'mongoose'

const userSchema = new Schema({
    _id: {
        type: String,
        required: true,
        unique: true, // 중복검사
    },
    DBId: {
        type:String,
        required: true
    }
});

// User 모델 생성
/**@type { mongoose.Model } */
export const User = model('user', userSchema, 'user');