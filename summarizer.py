import nltk
from nltk import sent_tokenize
import re
import heapq

article_text = 'It’s been just over a decade since Marvel Studios launched its flagship franchise of interconnected comics-inspired movies with 2008’s Iron Man, and even now it’s difficult to begin to evaluate how much that franchise has changed the face of filmmaking. After 10 years, 21 films, nearly a dozen television shows, countless tie-in comics and games and merchandising options and viral videos, and billions upon billions of dollars in earnings, the Marvel Cinematic Universe has become the Holy Grail that every major studio is questing after, usually with little success. The MCU films have set off a mania for interconnected multi-platform franchises and multi-film arcs, not to mention a still-growing tide of superhero stories in every possible medium.    But while Marvel has expressly laid out a number of formulas that its competitors have struggled to imitate — from its highly specific mix of action and fast-paced snippy humor to its frequent, unapologetic visual and narrative nods to the most obsessive fans in its midst — it’s also beginning to break those formulas. Spider-Man: Homecoming followed up on the international hero-on-hero warfare of Captain America: Civil War with a personal little neighborhood story that dialed the MCU stakes way back and reset expectations for the franchise. Thor: Ragnarok placed its story in the hands of Taika Waititi, a comedian with a distinctively deadpan sensibility, and introduced indie-style emotional improv to the superhero world. Avengers: Infinity War let the heroes lose, and lose big — even killing off many of the series’ flagship characters at the end.  Inevitably, not everyone gets an examination worth having, or a storyline that lives up to the 10-year buildup. Sidekick characters like Rocket Raccoon (Bradley Cooper) and James Rhodes (Don Cheadle) get plenty of screentime without doing anything new. Primary characters like Black Widow (Scarlett Johansson) and Ant-Man (Paul Rudd) are key to the action in ways that become actively frustrating as they don’t develop past their familiar baselines. And the most-changed character, Bruce Banner (Mark Ruffalo), goes through yet another significant evolution in his Hulk history, without ever contending with what the latest changes mean in this story, or could mean in future stories. And yet. The shadow of Infinity War is a stark, dark one, and Endgame only has one real job: to move the MCU forward past Infinity War’s climactic horror. Every moment of Endgame feels like it was made with that in mind — to convey the audience past the shock and into grief, anger, hope, and tremendous excitement. It was made for the kind of fans that will collectively gasp in shock at every significant twist (and there are a few huge ones), then cheer in relief at every climactic blow for the future integrity of the Marvel Cinematic Universe. With that in mind, Endgame doesn’t just play as a wild tangle of interacting plotlines and self-indulgent personal rabbit holes for these characters. It plays as an endless series of payoffs, in some cases for long arcs — like Tony Stark’s standoffish, dismissive relationship with Spider-Man (Tom Holland), whom he starts the film mourning in a passionate, personal way — and in other cases, for the tiniest of passing jokes from other MCU movies. The entire film is constructed of callbacks, references, reminders, and reminiscences. It’s full of catharsis for its characters and its audience, sometimes through immense battles, sometimes through elaborate low-key conversations between characters, and sometimes through tiny, abrupt moments. It feels like an anniversary project, a look back through the ol’ MCU scrapbook, and a big collective group hug after Infinity War.'

article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)  
article_text = re.sub(r'\s+', ' ', article_text)

formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text )  
formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)  

sentence_list = nltk.sent_tokenize(article_text)

stopwords = nltk.corpus.stopwords.words('english')

word_frequencies = {}  
for word in nltk.word_tokenize(formatted_article_text):  
    if word not in stopwords:
        if word not in word_frequencies.keys():
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1


maximum_frequncy = max(word_frequencies.values())

for word in word_frequencies.keys():  
    word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)


sentence_scores = {}  
for sent in sentence_list:  
    for word in nltk.word_tokenize(sent.lower()):
        if word in word_frequencies.keys():
            if len(sent.split(' ')) < 30:
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word]
                else:
                    sentence_scores[sent] += word_frequencies[word]


summary_sentences = heapq.nlargest(3, sentence_scores, key=sentence_scores.get)

summary = ' '.join(summary_sentences)  
print(summary) 