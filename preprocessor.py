from textblob import TextBlob

def spellcorrect(input):
    payload = TextBlob(input)
    spell_correction_text = payload.correct()

    print(spell_correction_text)

    sentimental_analysis_text = spell_correction_text.sentiment

    print(sentimental_analysis_text)

    return spell_correction_text

