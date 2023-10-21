import g4f


def gpt(text_pars: str, len_word: int):
    
    g4f.logging = False  # enable logging
    g4f.check_version = False  # Disable automatic version checking
    
    # Pars text
    content = f'Привет, я хочу чтобы ты взял на себя роль журналиста и перефразировал данный мною текст в журналистический формат, количество слов в тексте должно быть не меньше {len_word}, так чтобы он проходил проверку на плагиат, а также в конце текста выделил ключевые слова, которые могут быть заголовками. Вот текст:\n{text_pars} '
    # Automatic selection of provider
    # response
    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"content": content}],
            )
 
    return response
   
if __name__ == '__main__':
    gpt('Hello', 1)
