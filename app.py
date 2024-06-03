#we are going to create oyur first flask app using pythoon 
#adding aa couple more libraries to the requirments.txt file
from flask import Flask, send_file, render_template,render_template_string

# we need to create  an instance of the Flask
#This is to create an object that we can use
#we are going to use the __name__ variable to determine the root path of the application
#A root path is the maon directory of the application, think of this as the defualt route.
app = Flask(__name__)

#we are going to tcreate a routre that will be the main page f the application
#a route is a URL that the application wil respond to our client browser request.
#we are going to ise a route decorator to creaate aroute.

@app.route('/')
@app.route('/home')
def index():
    #whatever we return from this function will be displayed on the browser
    #now we will send the HTML template to the client browser
    return render_template("index.html")
#Let's create another route to read anfd download a short story
#we are going to call the story route trial
#one story per file to keep it maintanable
@app.route("/download_trial")
def download_trial():
    #create a path to the file
    file_path ="trial.txt"
    #now we will send the file to the client browser for downlaod
    return send_file(file_path, as_attachment=True)

#this is for the background of the author
@app.route('/Back_story')
@app.route('/back_story')
def back_story():
    #create an HTML template that will display the download link
    html_content = """
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The Enigmatic Author: Alexis</title>
    <style>
                body {
            font-family: 'Georgia', serif;
            background-color: #2c2c2c;
            color: #f0f0f0;
            margin: 20px;
        }
        header {
            text-align: center;
            margin-bottom: 20px;
        }
        .content {
            background-color: #383838;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 15px rgba(0,0,0,0.5);
            max-width: 800px;
            margin: auto;
        }
        h1 {
            color: #e0b3b3;
            font-size: 2.5em;
            margin-bottom: 0.5em;
        }
        p {
            line-height: 1.6;
            margin-bottom: 1em;
        }
        .image {
            text-align: center;
            margin-top: 20px;
        }
        .image img {
            width: 300px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.5);
        }
    </style>
        </head>
        <body>
            <header>
                <h1>The Enigmatic Author: Alexis</h1>
            </header>
            <div class="content">
                <p>In the small, fog-enshrouded town of Ravenwood, whispers of the mysterious author Alexis had long intrigued its residents. Known for her bone-chilling stories that seemed to materialize out of nowhere on various internet forums and websites, Alexis had earned a reputation as the phantom writer of the digital age. The most curious aspect of her tales was not just their terrifying content, but the seemingly impossible way they were disseminated—without the use of any modern technology.</p>
                <p>Alexis was a reclusive figure who lived in an old, ivy-covered manor at the edge of Ravenwood Forest. The manor, a gothic structure with towering spires and stained-glass windows, had been in her family for generations. Local legends claimed it was haunted, a notion that Alexis never refuted. In fact, some said she embraced it.</p>
                <p>Born into a lineage of storytellers, Alexis possessed an uncanny ability to weave narratives that could stir the deepest fears of her readers. Her great-grandmother, Eliza, was rumored to have been a witch who used her dark arts to communicate with the spirit world. Alexis, inheriting this mystical gift, developed a unique method of channeling her stories.</p>
                <p>Instead of using a computer or any conventional writing tool, Alexis employed an ancient quill made from the feather of a raven. It was said that this quill was enchanted, capable of transcribing her thoughts directly onto the internet. She would sit in her candle-lit study, the quill poised over a blank sheet of parchment. As she began to write, the words would vanish from the page, appearing instantly on various online platforms, as if carried by an unseen force.</p>
                <p>Residents of Ravenwood often speculated about how Alexis managed this feat. Some believed she had a pact with the spirits of the forest, who acted as her messengers. Others thought she possessed an extraordinary telepathic connection with the digital world, an ability that defied the laws of nature.</p>
                <p>Her stories, each more frightening than the last, captivated and horrified audiences worldwide. Tales of vengeful spirits, cursed objects, and haunted places were her specialty. Readers would often find themselves drawn into her dark world, unable to escape the grip of her words until the final, chilling sentence.</p>
                <p>Despite her eerie talents, Alexis was seldom seen outside her manor. She would occasionally venture into the town at dusk, her presence marked by a long, flowing cloak and a wide-brimmed hat that concealed her face. Those who caught a glimpse of her swore they could see a faint glow in her eyes, an otherworldly light that hinted at her supernatural abilities.</p>
                <p>As time passed, Alexis' fame grew, and so did the curiosity about her true nature. Journalists, bloggers, and fans attempted to contact her, but their efforts were always in vain. The few who dared to approach her manor often returned with strange tales of ghostly apparitions and unexplained phenomena.</p>
                <p>In the end, the enigma of Alexis remained unsolved. Her stories continued to haunt the internet, spreading fear and fascination in equal measure. The legend of the author who wrote without a computer became a part of the fabric of Ravenwood, a town forever entwined with the mysterious and macabre talents of its most infamous resident.</p>
            </div>
            
        </body>
        """
    #now we will send the HTML template to the client browser
    return render_template_string(html_content)
#we are going to create another route that will be the about page of the application
#we are going to use a route decorator to createe a  route
@app.route('/Characters')
@app.route('/characters')
def read_tiral():
    #create an HTML template that will display the download link
    html_content = """
            <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Character Descriptions</title>
            <style>
                        body {
                            font-family: 'Times New Roman', serif;
                            background-color: #1e1e1e;
                            color: #f3f3f3;
                            margin: 20px;
                        }
                        header {
                            text-align: center;
                            margin-bottom: 40px;
                        }
                        .content {
                            background-color: #333;
                            padding: 20px;
                            border-radius: 10px;
                            box-shadow: 0 0 15px rgba(0,0,0,0.5);
                        }
                        h1 {
                            color: #e5e5e5;
                            text-shadow: 2px 2px 5px #000;
                        }
                        h2 {
                            color: #c0c0c0;
                        }
                        h3 {
                            color: #a9a9a9;
                        }
                        p {
                            line-height: 1.8;
                        }
                        .character {
                            margin-bottom: 30px;
                        }
            </style>
        </head>
        <body>
            <h1>Character Descriptions</h1>

            <div class="character">
                <h2>Story 1: "The Endless Stairs"</h2>
                <h3>Character: Sam</h3>
                <p><strong>Height:</strong> 5'10" (178 cm)</p>
                <p><strong>Weight:</strong> 160 lbs (73 kg)</p>
                <p><strong>Age:</strong> 27</p>
                <p><strong>Secret:</strong> Sam has a phobia of elevators, which is why he prefers exploring staircases despite the dangers.</p>
            </div>

            <div class="character">
                <h2>Story 2: "The Rat's Revenge"</h2>
                <h3>Character: Jerey</h3>
                <p><strong>Height:</strong> 5'8" (173 cm)</p>
                <p><strong>Weight:</strong> 175 lbs (79 kg)</p>
                <p><strong>Age:</strong> 34</p>
                <p><strong>Secret:</strong> Jerey once worked as a chef and was fired for a kitchen accident involving a rat, which he never disclosed to anyone.</p>
            </div>

            <div class="character">
                <h2>Story 3: "The Whispering Shadows of Ravenwood"</h2>
                <h3>Character: Sarah</h3>
                <p><strong>Height:</strong> 5'6" (168 cm)</p>
                <p><strong>Weight:</strong> 130 lbs (59 kg)</p>
                <p><strong>Age:</strong> 18</p>
                <p><strong>Secret:</strong> Sarah has always had a fascination with the occult and secretly practices Wicca in her spare time.</p>
                <h3>Character: Eliza (the ghost)</h3>
                <p><strong>Height:</strong> 5'4" (163 cm)</p>
                <p><strong>Weight:</strong> Unknown (ghostly form)</p>
                <p><strong>Age:</strong> Appears to be in her late 70s</p>
                <p><strong>Secret:</strong> Eliza was not only a witch but also the guardian of a hidden treasure buried somewhere in Ravenwood Forest, which no one has found yet.</p>
            </div>

            <div class="character">
                <h2>Story 4: "The Sleepless Curse"</h2>
                <h3>Character: Lydia</h3>
                <p><strong>Height:</strong> 5'5" (165 cm)</p>
                <p><strong>Weight:</strong> 140 lbs (64 kg)</p>
                <p><strong>Age:</strong> 29</p>
                <p><strong>Secret:</strong> Lydia moved into the new apartment to escape a troubled past involving a restraining order against an obsessive ex-partner.</p>
                <h3>Character: Evelyn (the previous tenant)</h3>
                <p><strong>Height:</strong> 5'3" (160 cm)</p>
                <p><strong>Weight:</strong> Unknown (ghostly form)</p>
                <p><strong>Age:</strong> Appears to be in her late 30s</p>
                <p><strong>Secret:</strong> Evelyn's insomnia began after she witnessed a traumatic event that she never shared with anyone, and her spirit is bound to the apartment seeking solace.</p>
            </div>
        </body>"""
    #now we will send the HTML template to the client browser
    return render_template_string(html_content)


@app.route('/greet/<name>')
def greet(name):
    #whatever we return from this function will be displayed 
    return f"<h1> Greetings {name} </h1><p> We are so glad you are here today!</p> "
#Start the application
#this is the entry point of the application for python.
#this has not much to do with flask, but itis a good practice to havve this in your code.

if __name__== "__main__":
#now it is time for the fun part, we get to start the flask application server
#and listen fro incoming requests from the client brrowser
#if there are no errors this wil keep running untill we stop it.
    app.run()