import tkinter as tk
import random, time
from tkinter.constants import FLAT, GROOVE, RAISED, RIDGE, SUNKEN

# Game Variables
score = 0
xBox = 50
yBox = 50
sizeBox = 50
startTime = time.time()
timeTaken = 0

#Settings
Theme = '1'
testNo  = 10

def popUp(title = 'Notice', Message = 'Empty Message'):
    global Theme
    popUpWindow = tk.Tk()
    popUpWindow.title(title)

    if Theme == '1':
        tk.Label(popUpWindow, text='NOTICE', font=('arial', 10, 'bold')).pack(ipadx=50, pady=5)
        tk.Label(popUpWindow, text=('\n' + Message + '\n')).pack()
        tk.Button(popUpWindow, text='Ok', command=popUpWindow.destroy, relief=GROOVE).pack(ipadx=20, pady=5)
    else:
        tk.Label(popUpWindow, text='NOTICE', font=('arial', 10, 'bold'), bg='black', fg='white').pack(ipadx=50, pady=5)
        tk.Label(popUpWindow, text=('\n' + Message + '\n'), bg='black', fg='white').pack()
        tk.Button(popUpWindow, text='Ok', command=popUpWindow.destroy, bg='black', fg='white', relief=GROOVE).pack(ipadx=20, pady=5)
        popUpWindow.configure(bg='black')

    popUpWindow.mainloop()
    pass


def game():
    global score, c, scoreLabel, box, xBox, yBox, startTime, timeTaken, gameWindow, Theme, testNo
    gameWindow = tk.Tk()
    gameWindow.title('Bad Clicker Game')
    gameWindow.geometry('500x500')
    gameWindow.resizable(0, 0)

    scoreLabel = tk.Label(gameWindow, text='Score: 0', font=('arial', 20))
    if Theme == '2':
        scoreLabel.configure(bg='black', fg='white')
        gameWindow.configure(bg='black')
    scoreLabel.place(x=10, y=0)
    c = tk.Canvas(gameWindow, width=500, height=500, bg='cyan')
    if Theme == '2':
        c.configure(bg='grey')
    c.place(x=0, y=30)

    xBox = random.randint(1, 500 - sizeBox - (sizeBox / 2))
    yBox = random.randint(1, 500 - sizeBox - (sizeBox / 2))

    box = c.create_rectangle(xBox, yBox, xBox + sizeBox, yBox + sizeBox, fill='yellow')

    def m1Click(event):
        global score, c, scoreLabel, box, xBox, yBox, startTime, timeTaken
        if (event.x >= xBox and event.x <= xBox + sizeBox) and (event.y >= yBox and event.y <= yBox + sizeBox):
            score += 1
            scoreLabel.configure(text=('Score: ' + str(score)))
            newx, newy = random.randint(1, 500 - sizeBox - (sizeBox / 2)), random.randint(1, 500 - sizeBox - (sizeBox / 2))
            c.move(box, newx - xBox, newy - yBox)
            xBox, yBox = newx, newy
            if score == 1:
                startTime = time.time()
            if score == testNo:
                timeTaken = round(time.time() - startTime, 2)
                print(timeTaken)
                score = 0
                startTime = time.time()
                popUp(str(testNo) + ' Shots Completed', 'You Clicked ' + str(testNo) + ' targets in \n' + str(timeTaken) + ' sec\nThe Avg. is ' + str(round(timeTaken / testNo * 1000, 2)) + ' ms')
                scoreLabel.config(text='Score: ' + str(score))

        pass

    def keyP(event):
        if event.keysym == 'x':
            global score, c, scoreLabel, box, xBox, yBox, startTime, timeTaken
            if (event.x >= xBox and event.x <= xBox + sizeBox) and (event.y >= yBox + 30 and event.y <= yBox + sizeBox + 30):
                score += 1
                scoreLabel.config(text=('Score: ' + str(score)))
                newx, newy = random.randint(1, 500 - sizeBox - (sizeBox / 2)), random.randint(1, 500 - sizeBox - (sizeBox / 2))
                c.move(box, newx - xBox, newy - yBox)
                xBox, yBox = newx, newy
                if score == testNo:
                    timeTaken = round(time.time() - startTime, 2)
                    print(timeTaken)
                    score = 0
                    startTime = time.time()
                    popUp(str(testNo) + ' Shots Completed', 'You Clicked ' + str(testNo) + ' targets in \n' + str(timeTaken) + ' sec\nThe Avg. is ' + str(round(timeTaken / testNo * 1000, 2)) + ' ms')
                    scoreLabel.configure(text='Score: ' + str(score))


    gameWindow.bind('<Key>', keyP)

    c.bind('<1>', m1Click)

    def ctrlW(event):
        gameWindow.destroy()

    gameWindow.bind('<Control-w>', ctrlW)
    gameWindow.mainloop()

def settings():
    global x, Theme
    settingsWindow = tk.Tk()

    settingsWindow.title('Settings')
    
    settingsTitleFrame = tk.Frame(settingsWindow)
    settingsLabel = tk.Label(settingsWindow, text='Settings', font=('Arial', 20, 'bold'))

    # Main Frame
    settingsMainFrame = tk.Frame(settingsWindow)

    # Theme
    themeLabel = tk.Label(settingsMainFrame, text='Theme: ')

    x = tk.StringVar(master=settingsWindow, value=Theme)

    def updateTheme():
        global Theme
        Theme=x.get()
        pass
    
    lightRadio = tk.Radiobutton(settingsMainFrame, text='Light', variable = x, value='1', command=updateTheme)
    darkRadio = tk.Radiobutton(settingsMainFrame, text='Dark', variable=x, value='2', command=updateTheme)
    

    settingsLabel.pack(padx=100, pady=10)
    themeLabel.grid(row=0, column=0)
    lightRadio.grid(row=1, column=0)
    darkRadio.grid(row=1, column=1)

    #=========================

    # Number of targets per round
    global testNo
    testNoVar = tk.IntVar(master=settingsWindow, value=testNo)

    targetNoLabel = tk.Label(settingsMainFrame, text='Number of Targets per Round: ')
    targetNoSlider = tk.Scale(settingsMainFrame, from_=5, to=30, tickinterval=5, orient='horizontal', variable=testNoVar, relief=FLAT)

    targetNoLabel.grid(row=2, column=0, columnspan=2)
    targetNoSlider.grid(row=3, column=0, columnspan=2, ipadx=75)

    # Apply
    def applyFunction():
        global testNo
        print(targetNoSlider.get())
        testNo = targetNoSlider.get()
        root.destroy()
        settingsWindow.destroy()
        rootWindow()
        pass

    applyButton = tk.Button(settingsMainFrame, text='Apply', command=applyFunction, relief=GROOVE)


    applyButton.grid(row=4, column=0, columnspan=2, ipadx=30, ipady=10, pady=10)

    settingsTitleFrame.pack(side='top')
    settingsMainFrame.pack()
    

    settingsWindow.mainloop()
    pass


def rootWindow():
    global Theme, root
    root = tk.Tk()
    root.title('Tic Tac Toe')
    
    # Title
    titleFrame = tk.Frame(root)

    titleLabel = tk.Label(titleFrame, text='Tic Tac Toe', font=('arial', 20, 'bold'))
    versionLabel = tk.Label(titleFrame, text='V 1.0')

    # Theme
    if Theme == '2':
        titleLabel.configure(bg='black', fg='white')
        versionLabel.configure(bg='black', fg='white')
        titleFrame.configure(bg='black')
        root.configure(bg='black')

    # Display
    titleLabel.pack()
    versionLabel.pack()
    titleFrame.pack(pady=10, side='top')
    
    # Main
    mainFrame = tk.Frame(root)

    playButton = tk.Button(mainFrame, text='Play ►', font=('arial', 20, 'bold'), command=game, relief=GROOVE, bg='grey85')
    exitButton = tk.Button(mainFrame, text='Exit |←', font=('arial', 20, 'bold'), command=root.destroy, relief=GROOVE, bg='grey85')

    settingsButton = tk.Button(mainFrame, text='Settings ☼', font=('arial', 20, 'bold'), command=settings, relief=GROOVE, bg='grey85')

    creditsLabel = tk.Label(mainFrame, text='by Tanish M')

    # Theme
    if Theme == '2':
        playButton.configure(bg='black', fg='white')
        exitButton.configure(bg='black', fg='white')
        settingsButton.configure(bg='black', fg='white')
        creditsLabel.configure(bg='black', fg='white')
        mainFrame.configure(bg='black')

    # Display
    playButton.grid(row=0, column=0, ipadx=10, ipady=20)
    exitButton.grid(row=0, column=1, ipadx=10, ipady=20)
    settingsButton.grid(row=1, column=0, columnspan=2, ipadx=54)
    creditsLabel.grid(row=3, column=1, pady=5, sticky='e')

    mainFrame.pack()

    tk.mainloop()

if __name__ == '__main__':
    rootWindow()