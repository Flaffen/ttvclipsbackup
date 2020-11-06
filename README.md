# ttvclipsbackup

This script will download **all** clips you've made into an archive called *clips.zip*. You need to install Python 3 in order to run the script. You can download it here: https://www.python.org/downloads/

After you have downloaded Python you should open up the Windows Command Prompt and type
```
pip3 install requests
```
If you have any difficulties or questions, you can DM me on [twitter](https://twitter.com/fakeflaffen) and I will try to help you.
# Instructions
- Open a new tab in Google Chrome. Hit F12 to open the developer tools. For conveniece you can pop out the console to a separate window by clicking here

![dock](https://i.imgur.com/hfSmYHy.png)

- Click on the "Network" tab. Then click on the "XHR" tab. You should now see a red "recording" circle and a mostly empty log of network requests.

![network](https://i.imgur.com/qp438P0.png)

- Get back to the main tab. Go to https://dashboard.twitch.tv/u/YOUR_USERNAME/content/clips where YOUR_USERNAME is your username, or login, on twitch. This will open the page with clips you've made.
- Return to the developer tools. Hit the red circle to stop recording network activity. After that, your circle will turn grey and your network tab will look something like this.

![network full](https://i.imgur.com/z5GfZ2T.png)

- Now click on the first row with **gql** in it. That should open a panel like this

![gql](https://i.imgur.com/QgkoZCj.png)

- Scroll down the panel until you see **Request Payload**. There you have to find a line which contains `{operationName: "ClipsManager_User", variables:...` If you can't find it, click on the next row with **gql** in it until you find the necessary line.

![theline](https://i.imgur.com/lcs5uI7.png)

- Now find the **Authorization** line above. It will look something like `Authorization: OAuth xh4f1df7jfxxad43ctdkffufafn847e`. Copy the gibberish after *OAuth* **without** any trailing or leading spaces.

- Double click the downloaded script. Enter your twitch name. When it asks for *Token* paste the gibberish you just copied and click enter. Then it will ask you for ID. To get it, get back to the Developer Tools.
- Click on the **Preview** tab and find `{id: "12345678912"}` Copy the number between the quotes.

![id](https://i.imgur.com/D3bBGxb.png)

- Paste it into the script and click enter.

Congratulations! Now the script will start to download all clips into an archive with the name **clips.zip**. I found that the typical size for a clip with 1080p quality is around 20MB. A very rough estimate is **1GB per 100 clips** with that quality.
