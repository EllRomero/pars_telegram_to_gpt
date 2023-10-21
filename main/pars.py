import snscrape.modules.telegram
from datetime import datetime, time, date
from freegpt import gpt
from pytz import utc
from group_load import load_txt
from remove_emoj import remove_telegram_emoj
from repeat import chek_repeat
from create_folder import create_fold

# Get the current date and time
now_time = datetime.now()
# Set the beginning and end of today
start_of_day = utc.localize(datetime.combine(now_time.date(), time.min))
end_of_day = utc.localize(datetime.combine(now_time.date(), time.max))

# Name group
name = load_txt()
# Create folder
create_fold('text')
# Number of posts read

for names in name:
    count=0
    scraper = snscrape.modules.telegram.TelegramChannelScraper(f'{names}')
    for i, item in enumerate(scraper.get_items()):
        if count > 2:
            print(f'\nБыли прочитаны 3 последние поста в группе:{names}')
            break
        print(f'Cмотрим группу: {names}')
        # Check actual news for today
        if start_of_day <= item.date <= end_of_day:
            print('Читаем пост:')
            # Delete telegram emoj
            print(item.content)
            if item.content:
                text_pars = remove_telegram_emoj(item.content)
                if chek_repeat(text_pars[:8], date.today(), names):
                    print('Такой пост уже был!')
                    count+=1
                    continue
                len_word = len(text_pars)
                print(text_pars)
                len_word = len(text_pars)
                # Connect gpt, return str
                print('\nИдет процесс перефразирования текста...')
                response = gpt(text_pars, len_word)
                # Save file
                # Path save files
                create_fold(f'text\{date.today()}\{names}')
                with open(f'text\{date.today()}\{names}\{text_pars[:8]}.txt', 'w', encoding='utf-8') as f:
                    f.write(f'ОРИГИНАЛ:\n{text_pars}')
                    f.write(f'\n\nОТФОРМИОТИРОВАНЫНЙ ВИД:\n{response}')
                    print(f'\nФайл сохранен - {text_pars[:8]}.txt')
        count+=1
        
   
