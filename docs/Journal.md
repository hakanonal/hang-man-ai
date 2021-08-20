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
- I did the environment but I want to paramitize the maximum try as config.
  - May later
- I have completed the console game interface. you can call

  ```
  python main.py
  ```

  - I did also play notebook and integrated to be played in google colab. Read the readme.

- Ok! now I got an idea when I was cheking [this](<https://en.wikipedia.org/wiki/Hangman_(game)>) page there was saying about the recourence of the english letters. So I thought maybe I can experiment the histogram of the letters in the word-list data that I have created.

  - Yes the histogram is ready. as expected a e i words are very popular but suprasinglly oöuü is way below the list. also l is the 3rd most use letter. Very interestinig. Should I implement my standart agent just in porder with the letters appeared here?

  #### 02.08.2021

  - Let's begin to construct the metrics.
    - config parameter has been added to environment
    - My doughter poped up. will be back...
    - I am back...
    - for the first time I have removed the environment from the AI. That's why I need a seperate class to automate the game rounds and multiple games among with paramitized different agent types.
      - ok I have created initial ai game environment using the environment class. However I am having trouble to cross reference classes. I think I need to put all command calls ini the root and all other cllass inito modules/folders.
        - The new module diir structure is worling fine but it is not working good in notebooks so I aplied one of the solutions [here](https://stackoverflow.com/questions/34478398/import-local-function-from-a-module-housed-in-another-directory-with-relative-im)
        - Weirdlly when execute from the command the data dir accaesble but it is not accessible from the notebook executions. I have removed direct module calls from the global notebook. But I will need to solve this propblem if I want to discover more via notebook.

#### 17.08.2021

- Today I want to continue where I left off. I have 1 hour or something so.
  - I needed to spent some time to remember the code.
  - Great! I have fixed several bugs. I have started to observe the metrics in wandb her is the [link](https://wandb.ai/hakanonal/hang-man-ai)
  - Yes I have added one more agent. Instead of guessing letters alphabeticllay everytime, The new agent agentFREQ guessies the letters in the order of occerance in the word list data. So the immediate result is improved dramaticlly. it was 17,8 now it is close to 13,5
  - by the way the main metric is avarage try. we are tyring to dcrease it. If we manage to create an agent that avg_try metric is below 10 then in avarage that agent will be able to win normal games.
  - So this two agent is not good enough.
- I am thinking to change the train.py code's name. Because I will train the Noural agent seperatelly. So this is the entry code that plays with the given agent. continue on this topic next time.

#### 18.08.2021

- Ok let's start with some script file name changes.
  - changed the main script name to play
  - whatt about the name tournament instead of train.
  - and we are done with that!
- I want to create several more agents that may be more cllever that we have created so far.
  - Well! the strategy we follow with my doughter was, first we were guessing the vowels until we are convinced that there should be no more vowels (note that we do not have to guess all vowels since every cylable has at least one vowel we educated guess that there is no omre vowel to guess to save our try count.)
    - However, what if we tweak frequency agent first into vowels than others according to frequency.
      - well the frequency agent seems to be aproximatelly 1 try better on avarage.
    - so if we go back to original stragety we may use the frequency order as well as memorizing word list. Since when we play with my dpughter we search thorugh our brain what words are known by us and try them with the board.
      - what about the agentMEM. changed it to agentMEMFREQ siince I think I will create couple of more agents uses memory.
      - what if this agent gets the length of the board and norrows down the options from the memory and extracts the frequancy of the letters of the norrowed list and guesses that new order?
        - I have done the norrowing down however I am not sure how it is going to behave if hte word to guess has space in it? It should not make any difference.
        - Let's give it a try... Well! it just a tiny little bit better than plain frequency agent. However it is much more slower. as expected..
      - well one more addtion to this agent may be on each guess it should try to match with its narrowed list? However would it make any difference? on each guess it is going to noarrowed the list even more. It would be definatelly much more slower.
        - I think this strategy is the best startegy however there is some bug I need to fix. It is fixed
        - Well! this agent outperforms all other agents. in ~2600 steps on avaarage it knows the workd on 2,6 tries on avarage. This agent has still room to improve for exmample. It norrows down the words according the letters on the board but for example it does not norrow down accordiing to the previous guessed letters if they are apeeared or not. However, if I apply this logic it will bring more performance issue which would be needless hence the current performance is way better.
- Well It seems that I need additional metrics like max try min try and speed.
  - I do not how to implement speed sinice every environment that has executed the script will measure different speed. this seems to be a little bit more research
- Will continue on implementing new metrics and renew the all runs swith sweep.

#### 20.08.2021

- Hello! Let's get on with this new metrics and sweep.
  - created the [sweep](https://wandb.ai/hakanonal/hang-man-ai/sweeps/v0l2e7i3) It is sweeping only different agents only.
