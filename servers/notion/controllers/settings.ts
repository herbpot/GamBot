import { Request, Response } from 'express'
import { APIResponseError, APIErrorCode } from '@notionhq/client'
import { client } from '../schema/Notion'


export const setDataBase = async (req: Request,res: Response) => {
    const {dId} = req.body
    try{
        await client.databases.query({
            database_id: dId
        })
        res.send(true)
    }catch (e: unknown){
        if (e instanceof APIResponseError){
            if (e.code == APIErrorCode.ValidationError)
                res.send(false)
        }
    }
}