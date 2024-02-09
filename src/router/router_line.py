import json

from fastapi import FastAPI, Request
from typing import Optional
from fastapi.responses import JSONResponse
from fastapi import APIRouter

from linebot.v3 import (
    WebhookHandler
)
from linebot.v3.exceptions import (
    InvalidSignatureError
)
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage,
    StickerMessage,
)
from linebot.v3.webhooks import (
    MessageEvent,
    TextMessageContent,
    StickerMessageContent
)

linebot = APIRouter()

configuration = Configuration(access_token='nCL0aFCoNRLSYBotzVl8kLvMaIyKGFjYEx745u3vYSLvcZTD72CcdRjgFXN6OegMW32oT7bcUOX8Ly/8rD+rO0MR69B6CTVeeslnV776n0y04+9F56UydjquUF8OhhIEgkckbWzwhMBNs5rY452oCAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('f9857c3161f0e204f7cf590633b29ba9')

@linebot.post("/callback")
async def callback(request: Request):
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = await request.body()

    body = body.decode('utf-8')
    print("Request body: " + body)

    # handle webhook body
    try:
        print("try")
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        return JSONResponse(content='error', status_code=400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=[TextMessage(text=event.message.text)]
            )
        )


@handler.add(MessageEvent, message=StickerMessageContent)
def handle_sticker_message(event):
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=[StickerMessage(
                    package_id=event.message.package_id,
                    sticker_id=event.message.sticker_id
                )]
            )
        )


# def reply_text_handler(reply_token: str, text: str):
#     with ApiClient(configuration) as api_client:
#         line_bot_api = MessagingApi(api_client)
#         line_bot_api.reply_message_with_http_info(
#             ReplyMessageRequest(
#                 reply_token=reply_token,
#                 messages=[TextMessage(text=text)]
#             )
#         )
#
#
# def _intent_to_text(intent: str, text: Optional[str] = None) -> str:
#     if intent == 'hello':
#         text = "สวัสดีจ้าคุณ" + text
#     # elif intent == 'add_revenue':
#     #     text = "สวัสดีจ้าคุณ" + text
#     return text



# @linebot.post("/callback")
# async def callback(request: Request):
#     req = await request.json()
#     print(req)
#     # get X-Line-Signature header value
#     # signature = request.headers['X-Line-Signature']
#
#     # get request body as text
#     # body = await request.body()
#     #
#     # body = body.decode('utf-8')
#     # print("Request body: " + body)
#     #
#     # # handle webhook body
#     # try:
#     #     print("try")
#     #     handler.handle(body, signature)
#     # except InvalidSignatureError:
#     #     print("Invalid signature. Please check your channel access token/channel secret.")
#     #     return JSONResponse(content='error', status_code=400)
#
#     intent = req["queryResult"]["intent"]["displayName"]
#     text = req['originalDetectIntentRequest']['payload']['data']['message']['text']
#     reply_token = req['originalDetectIntentRequest']['payload']['data']['replyToken']
#     id = req['originalDetectIntentRequest']['payload']['data']['source']['userId']
#     disname = MessagingApi(ApiClient(configuration)).get_profile(user_id=id).display_name
#
#     print('id = ' + id)
#     print('name = ' + disname)
#     print('text = ' + text)
#     print('intent = ' + intent)
#     print('reply_token = ' + reply_token)
#     reply_text_handler(reply_token=reply_token, text=_intent_to_text(intent, disname))
#
#     return 'OK'


# def reply_text_handler(reply_token: str, text: str):
#     with ApiClient(configuration) as api_client:
#         line_bot_api = MessagingApi(api_client)
#         line_bot_api.reply_message_with_http_info(
#             ReplyMessageRequest(
#                 reply_token=reply_token,
#                 messages=[TextMessage(text=text)]
#             )
#         )
#
#
# def _intent_to_text(intent: str, text: Optional[str] = None) -> str:
#     if intent == 'hello':
#         text = "สวัสดีจ้าคุณ" + text
#     # elif intent == 'add_revenue':
#     #     text = "สวัสดีจ้าคุณ" + text
#     return text