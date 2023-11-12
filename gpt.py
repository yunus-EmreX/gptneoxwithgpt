import openai

# OpenAI API anahtarınızı buraya girin
openai.api_key = 'ur key'

def is_generated_by_ai(text):
    prompt = text + " sence bu bir yapay zeka tarafından mı oluşturulmuş evet veya hayır gibi kısa kelimeler kullanarak cevapla"

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=3000,
        n=1,
        stop=None,
        temperature=0.0,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    answer = response.choices[0].text.strip().lower()
    return answer

# Kullanıcıdan metni alın
text = input("Bir metin girin: ")

# Metni ChatGPT'ye ileterek sonucu alın
result = is_generated_by_ai(text)

# Sonucu kullanıcıya gösterin
print("Bu metin bir yapay zeka tarafından mı oluşturulmuş?", result)
