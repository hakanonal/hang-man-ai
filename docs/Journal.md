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

#### 01.09.2021

- Today I want to at least start to create an agent that has a regresion network.
  - I am distracted though before begening the job I wanted to create a result report until now. [Here](https://wandb.ai/hakanonal/hang-man-ai/reports/Comparison-of-Non-Neural-Networkds--Vmlldzo5ODQ1NDA) it is.
  - So where were we?
  - Now when first think of this kind of agent. It is going to be different from others, hence I will need to train them first. And the trained agent will be playing in tournament. Maybe I can train it on a notebook and then put them on tournament. However while training I am pretty sure that I will need to compare bunch of same agents. So I need to design that also. Let's begin to train one and then we can figure it out the rest later.
    - I am thinking of to input the state of the board and spit out the hot encoded of all letters.

#### 02.09.2021

- Go on...
  - readinig the last sentence...
  - reading [this](https://www.tensorflow.org/tutorials/keras/regression?hl=en) article

#### 17.09.2021

- Another big break and we are here...

  - Very good article. so what features can I extract from my data. I had thought to input the board but I am fuzzy about that right now. At least I need to find a way to represent the board as input of the network. output is pretty straight forward it is hot encoded of the alphabet. (I mean 29 nodes sigmoid)
  - So the input features may be. Only brain storming...
    - I have the length of the board
    - number of try
    - number of guessed letters? or
      - number of unknown letters
      - number of known letters
    - It feels very exciting. Becuase non of these features has any signicance to guess the correct letters on minimum try, nevertheless that's beuty of the neural networks.
    - I may write a function that decodes the game state
  - I also need to design how am I going to train with the dictionary. since if there is the above features I need to play the game to obtain the try, known etc... features.
    - Hmmm! this complicates the training process. do I have to train via reinforcement. I am not very interested to do that.
    - Wait! maybe I can harvest the dictionary and create the all possible combinations of a word and its game state.
      - Not that much easy though, It is easy to expand the length and known letters which the dataset will be expanded with number of words multiplied with length of each word. which I think tolerabile however, putting unknown letters would expanded it enormous.
      - However what if I create a altenative game environment that the game is made for each word in dictionary (maybe it is done more than once) and in the game I can save each step as seperate datpoint for my dataset. I know it is going to take long time but I will only do this once and use that dataset to train. hmmm?? basiclly I am generating the list of different game states from the dictionary. I like that I will move on this.

- Createing and agentRND which will guess the letters in random order in each game. reading [this](https://note.nkmk.me/en/python-random-shuffle/) article

  - No surprise there it is the worst agent. Here is an example [run](https://wandb.ai/hakanonal/hang-man-ai/runs/sc9lc3cm) However I am going to use it to generate training dataset mentioned above. However would it be wise to generate states the plays of a random agent. Since it is going to be trained with best posiblle games to play It would be logical to use my best agent to accomplish this task.

- I am having trouble to call the classes from the notebook. reading [this](https://newbedev.com/import-py-file-in-another-directory-in-jupyter-notebook) article says you can not do it.

  - [this](https://www.py4u.net/discuss/159176) helped!

  #### 24.09.2021

  - Going on from where we left off. I was having trouble calling classes from notebook...
    - so my current side problem is my class calls the dictionary data however executing the script from notebook and console behaves different. I knew this problem, there are some notes above. now it is time to solve it once for all.
      - I am considering to dynamclly change the current directory by explictlly calling system commands. [this](https://stackoverflow.com/questions/15680463/change-ipython-jupyter-notebook-working-directory) hepled
      - It seems that it is not possible to dynamiclly get the curent path of the working notebook. explained [here](https://github.com/ipython/ipython/issues/10123)
      - So I have solved via documentation. You need to execute first cell only once.
    - So I am playing bunch of games, what would be my traing data file format?
      - well I have figure it out a format. I amplaning to anaylze it in [bigML](https://bigml.com)
    - So generation seems to be working fine. However I may need to execute in a server. Because it is taking long time.
      - I have executed for decent amount of time. I had to interrupt it. I came up only to letter ı. (we are going on alphabetically.) so - I will put it in server.
    - the states.csv is pretty big. I gave up to put it in github. So you may need to execute for your self.

#### 02.11.2021

- Antoher huge break and here we are...
  - reading and remembering where I had left off...
- well eventhough I do not have complete list of states before putting this code to server and generate the full list, I will be able to analyze it in bigml? let's see...
  - My limit for bigml is not enough. Eventhugh the file is not the full file. neverthless I will crop the file and try to do what I can.
  - BigMl is helping a lot I am trying lot's different parameters without writing single line of code. determining the model parameters this way is much more convienent.
  - Currentlly logistic regression and deep net models are not performing very good. guessing a is easy for both of them but others are not much of a difference.acuracy, precsion, recall is below %40 for both of them. So I have started an OptiML run which I bealive it is going to take long time.

#### 03.11.2021

- Continue on working bigml
  - optiml gave some kind of a error.
  - I am continuing to fiddle arround the app. I am trying to tokenize the board and guessed words better. It seems that they have more relevance among others.
  - I have tried dicision tree, deepnet and logistic regression models. they are giving all similar results which are performing very bad except guessing the letter a.
  - I have noticed few problems with my dataset,
    - the board state is being shown after the action is played. Should I exclude the action to play from the board? I think yes. this brings that I need to modify my generator program. I very happy that I have found this problem at this stage.
    - I want to also use the topic clasifer however it requeres text field as input. should I remove commos from the gurssed_letters and board and use space instead of it to properlly tokenize it? well I can not get use of topic modeling in this case. As far as I understood there is no recurent neteorks in bigml??
  - By the way when I set the guessed letters and board fields as "items", the performance got above %60. still not enough though
  - Another by the way yersterday I was wathich video and bumped to a ad called dataiku. It seems an app that is very similar to bigml. I fidileing with it now.
    - Well this app looks great, you can do any kind of analyze and manupulation of data and also train and evalute models all from a dashboard without righting a single line of code. And it is also fairlly easy to use. I love it. I may use this tool inthe future also. [https://www.dataiku.com](https://www.dataiku.com)
    - I have started a trial account with 14 day period.
    - You can also use in premse environment which I will also consider to use it in the future.

#### 08.11.2021

- So we have a good sense of how we can quickly trainf varius AI algorithms on our data. For now we know:

  - I am wondering if full training data would do difference? because in our sample data class "a" has the most results. other results may make some difference.
  - In order to game predict right we need to remove the predicted class from the board. The board should be in a state that the prediction is not played yet.
  - bigml will not help us in full data. it is too big. dataiku is very helpful I will continue with that.
  - dataiku can be run in local but when the data is big I am assuming it is not going to help either. I need to install it in a server.
  - and of course before all of that I need to generate the full training data in a server.
  - So I am replaning my project board.

- Fix [bug](https://github.com/hakanonal/hang-man-ai/projects/1#card-72111459).

  - It is done!

- Now I will deploy it to the server
  - I need to remember How I was doing that...
  - I have remembered my deployment advantures from my previous projetcs [here](https://github.com/hakanonal/mastermind/blob/main/docs/journal.md#13122020)
  - Ok I have remembered a lot. However I have relized that I have written my training data generation code in to notebook. Is there a way to execute code in notebook unattended.
    - [This](https://towardsdatascience.com/keep-jupyter-notebook-running-even-after-browser-is-closed-9a1937b7c615) has some decent different methods to use. I will try runipy or nbconvert methods. yep! It seems to be working great.
  - So to create server? where? how?
    - I have decided to move with my jump computer.
    - Some doc about ubuntu [netplan](https://netplan.io)
    - a weird error while installing the requirements via pip "PyObjC requires macOS to build"
      - since the requirements should be indepentdent from the OS It should not goes into requirements.txt, So they are suggesting to include only top level requirements. [here](https://stackoverflow.com/questions/46816430/how-to-list-freeze-only-the-python-modules-imported-required-by-my-project)
      - installing pipdeptree
        - However pyobjc is installed in top level.
        - well I do not know how that module is got there. I have uninstall it. assuming that it does not require in my project if it does I will look it up later.
    - so my training data generation notebook started to run on my local ml computer I will leave it as it is. Probally It will take hours to work.
      - It is finished
    - I have also installed dataiku to my local jump computer. and started a new logistic regression on the full dataset.

#### 09.11.2021

- Now the tricky part is begening. The quick result for a regression is almost same with the previous sessions. a is signifcantlly performing good however other calsses are very poor.
  - I am changing some parameters and fidilleing arround with it.
  - Love this app! ı have created a NN analyses which I can freely configure the model and I do not have to read and feed it iinto model. And the results are being showed in detail. It also seems that I can run these trainings in GPU. which is seems to be quite straight forward.
  - However I have lack of ability to create a proper model for this dataset. I need to switch my mind from coder to data analiyst for this task.
  - Besides dataiku free version does not allow me to export the trained model out so that I can integrate it to my app. It somehow serves it in from the dss itself but it also requires to pay for the licence. However whey I dig down a little bit [dss_data_path]/analysis-data/HANGMANAI/aTuarmer/2Kur8F7X/sessions/s3/pp1/m1 I found the keras model file here maybe I can use that file on my aplication?
    - well I did not figure out the input but it seems to be usable. at least the program did not get eror. In theory if I get the right version of keras and tensorflow It will do great.
