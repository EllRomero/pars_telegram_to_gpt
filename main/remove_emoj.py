import re


def remove_telegram_emoj(text):
    # Паттерн для поиска телеграм-смайликов
    pattern = re.compile("["
                                u"\U0001F600-\U0001F64F"  # эмодзи смайликов
                                u"\U0001F300-\U0001F5FF"  # эмодзи символов и пиктограмм
                                u"\U0001F680-\U0001F6FF"  # эмодзи транспорта и картинок
                                u"\U0001F1E0-\U0001F1FF"  # эмодзи флагов стран (iOS)
                                u"\U00002500-\U00002BEF"  # chinese char
                                u"\U00002702-\U000027B0"  # эмодзи дополнительных символов
                                u"\U000024C2-\U0001F251"
                                u"\U0001f926-\U0001f937"
                                u"\U00010000-\U0010ffff"
                                u"\u2640-\u2642" 
                                u"\u2600-\u2B55"
                                u"\u200d"
                                u"\u23cf"
                                u"\u23e9"
                                u"\u231a"
                                u"\ufe0f"  # dingbats
                                u"\u3030"
                    "]+", flags=re.UNICODE)
    # Удаляем все смайлики из текста
    return pattern.sub(r'', text)
  
  