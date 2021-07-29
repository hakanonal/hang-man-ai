# Journal

This document is my journal about this project. I am writing all my thoughts trials and errors. This is my way of thinking process. My mind is open-soured in a way. Please note that I am writing this document very fast and there may be too many typos like tis one.

#### 27.07.2021

- Heyoo! Repo is being created. Waw I've missed this. I wasn't doing that for a long time. Now here we are.
- So first I need to figure it out what output am I going to accomplish with this project?
  - Well I think I need a game environment.
  - I need the list of words? How can find them? Maybe downbload from a online public dictionary. Also I need the list of letters :D Sorry it is going to be in turkish. I want my doughter to be able to play this game. Too a look to [this](https://sozluk.gov.tr)
  - Should I seperate the API from interface? It would be very flexiable.
  - Ok and the hot part. What the AI is going to do exactlly?
    - Well can it guess the probabilty of the next letter? Maybe this is a good posibility to experiment how this NLP thing works out huh?
    - On the other hand that may be is a little bit overkill. Since the pattern that had arrised with the experience with my doughter is first call the vowels and then call any other consonant letter. The key point to not to hang the man of course we are continouslly skimming our words in our memory if it matches with the state of the board. That would be mercilessly give competitive advantage to this agent of course. You oow computers have a far more better way to manage memory than human's (well at least most of the humans).
    - May be I can create two different agents and compare their avarage guessed letters for each game. I do not have to put kill/end of the game (I may never hang the man) or I will define a parameter that at which guess the man will be hanged. If I assign the number of the letters in a alphabet then technically it would be imposible to loose ther game.
    - Should I measurre the game win and loose? I am not sure yet.
- I need to put these thoughts to in order and convert into cards. [Here](https://github.com/hakanonal/hang-man-ai/projects/1) it is.

- I am looking how can I find the list of all words? There many applications but I need the raw data. Here is the [card](https://github.com/hakanonal/hang-man-ai/projects/1#card-65714026)

  - I have wondered how many turkish words. A little bit google search...
  - I have bumped into [this](https://www.kelimetre.com/kelime-listeleri) page. However we need a crowler to extract all words from this web site.
    - Well I have listed all words by thier letter numbers from [here](https://www.kelimetre.com/harf-sayisina-gore-kelimeler). I have summed up all words and it is 60675. Well I am not convinced yet there should much more words. If it was easy to extract all words I would have start with it but I will search more.
  - well what about [this](https://tr.wiktionary.org/wiki/Vikisözlük:Sözcük_listesi) one.
    - this one also needs a crawler but at least it is only 2 levels.
  - Ok [this](https://github.com/CanNuhlar/Turkce-Kelime-Listesi) one is easier to start with. I have downloaded posted text it is only 870kb. which I think it won't be a problem in terms of memory. So research has completed.

- Let's begin with game environment.

  - I need python right? Why not...
  - Of course I have forgot the pyenv again. Need to remember...
    - I am inistalling 3.9.0 via pyenv. will also create virtualenv. pofff it gave error. It is so lame that my first moves ends up with error. I do not want to stuck with this error so I am going to try older versions.
      - error again. maybe I should upgrade pyenv. Yihuuu! it worked. Moreover I have mananged to install latest version 3.9.6
    - viirtualenv hand-man-ai is created.
  - Next start to code. I have forgat my experiiment notebook. I will add the link [here](../experiment.ipynb). Hopefully I will not move it to another place so that this link is not broken. If it is sorry in advance. But if you look after the code base I am sure you will find it pretty quicklly.

    - my virtual environment does not work properlly. even though I have activated the environment the python version does not points to the version it is suppose to.

      - checked [this](https://github.com/pyenv/pyenv-virtualenv/issues/343) issue.
      - Bumped [this](https://stackoverflow.com/questions/56462518/virtualenv-with-pyenv-gives-wrong-python-version) I will recreate the virtualenv.
      - Stucked. These things were working smoothyly now it is pain.
      - [This](https://github.com/pyenv/pyenv/issues/1342) page suggested to remove pyenv and reinstall.
      - It seems to be fixed when I iniclude the .python-version file.

    - I am considering to create a environment class so that it can store the game state,init and play.
      - I have created environment class I am thinking about the data struture of the state

#### 29.07.2021

- continue working on environment:
  - so initial implementation of envirronment has finished I have.
  - Ups I have forgot to retreive the words from the word list.
