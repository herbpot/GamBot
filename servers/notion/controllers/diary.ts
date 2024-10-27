import { Request, Response } from 'express'
import { APIResponseError, APIErrorCode } from '@notionhq/client'
import { client } from '../schema/Notion'
import { User } from '../schema/User'
import { BlockObjectRequest } from '@notionhq/client/build/src/api-endpoints'


export const setDiary = async (req: Request,res: Response) => {
    const {userId, title, context, files}: {userId: string, title: string, context: string, files: Array<string>} = req.body
    console.log(userId)
    const user = await User.findOne({})
    console.log("user")
    console.log(user)
    try{
        await client.pages.create({
            parent: {
                database_id: user!!.DBId
            },
            properties: {
		        "이름": {
                    "title": [
                        {
                            "text": {
                                "content": title
                            }
                        }
                    ]
                }
        	},
        	children: [
                ...context.split('\n').map((t) => ({
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {
                        "rich_text": [
                            {
                                "type": "text",
                                "text": {
                                    "content": t,
                                }
                            }
                        ]
                    }
                }))!!,
                ...files.map((l) => ({
                    "object": "block",
                    "type": "image",
                    "image": {
                        "type": "external",
                        "external": {
                               "url": l
                        }
                    }
                }))!!
            ] as BlockObjectRequest[]
        })
        res.send(true)
    }catch (e: unknown){
        if (e instanceof APIResponseError){
            if (e.code == APIErrorCode.ValidationError)
                res.send(false)
        }else
        throw(e)
    }
}