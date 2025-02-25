from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import talk_hhm as tk


TOKEN = '810383631597354834:AAFwJSTkk8fUhvrjB5vydJSpzBfmXpKrHEg'

# TRIGGER_WORDS = {
#    "안녕":"안녕하세요! 저는 혜미봇입니다!!😊",
#    "정보":"어떤 정보가 필요하세요??😁",
#    "기분":"저는 기분이 좋아요!!👍"
#}

async def start(update, context):
    await update.message.reply_text("안녕하세요! 저는 헬로카봇 입니다. 무엇을 도와드릴까요?")
    
async def monitor_chat(update, context):
    user_text = update.message.text # 감지된 메세지들
    chat_id = update.message.chat_id # 메세지가 온 채팅방

    for key, res in tk.TRIGGER_WORDS.items():
        if key in user_text:
            await context.bot.send_message(chat_id=chat_id, text=res)
            break  # 한 개의 키워드에만 반응
    
def main():
    app = Application.builder().token(TOKEN). build()

    # 명령어 핸들러 추가
    app.add_handler(CommandHandler("start",start))

    # 응답 핸들러 추가
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, monitor_chat))

    print("텔레그램 봇이 실행중입니다. 모니터링 중...")
    app.run_polling()

if __name__=='__main__':
    main()
