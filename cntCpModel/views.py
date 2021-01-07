from django.shortcuts import render, redirect
from subprocess import run, PIPE
from sys import executable, argv
from .printResult import ClassificationModel

model = ClassificationModel()
def getClas(a):
    if a>0.65:
        return "Positive"
    elif a>0.35:
        return "Neutral"
    return "Negative"

def getRate(a):
    if a>0.8:
        return "11111"
    elif a>0.6:
        return "1111"
    elif a>0.4:
        return "111"
    elif a>0.26:
        return "11"
    return "1"

lst = []
def getRet(text):
    tp = model.getResult(text)[0]
    lst.insert(0, {'text': text, 'rating': getRate(tp), 'clas':getClas(tp)})

someRev = ["This was an absolutely terrible movie. Don't be lured in by Christopher Walken or Michael Ironside. Both are great actors, but this must simply be their worst role in history. Even their great acting could not redeem this movie's ridiculous storyline. This movie is an early nineties US propaganda piece. The most pathetic scenes were those when the Columbian rebels were making their cases for revolutions. Maria Conchita Alonso appeared phony, and her pseudo-love affair with Walken was nothing but a pathetic emotional plug in a movie that was devoid of any real meaning. I am disappointed that there are movies like this, ruining actor's like Christopher Walken's good name. I could barely sit through it.",
"This is the kind of film for a snowy Sunday afternoon when the rest of the world can go ahead with its own business as you descend into a big arm-chair and mellow for a couple of hours. Wonderful performances from Cher and Nicolas Cage (as always) gently row the plot along. There are no rapids to cross, no dangerous waters, just a warm and witty paddle through New York life at its best. A family film in every sense and one that deserves the praise it received.",
"I have been known to fall asleep during films, but this is usually due to a combination of things including, really tired, being warm and comfortable on the sette and having just eaten a lot. However on this occasion I fell asleep because the film was rubbish. The plot development was constant. Constantly slow and boring. Things seemed to happen, but with no explanation of what was causing them or why. I admit, I may have missed part of the film, but i watched the majority of it and everything just seemed to happen of its own accord without any real concern for anything else. I cant recommend this film at all.",
"Very Good"]

for i in someRev:
    getRet(i)

def home(request):
    text = request.POST.get('text') if request.POST.get('text')!=None else ""
    if len(text)>0:
        getRet(text)
    return render(request, 'cntCpModel/index.html', {'lst': lst})
