---

---

<style>
    body {
      animation: fadeInAnimation ease 3s;
      animation-iteration-count: 1;
      animation-fill-mode: forwards;
  }

   body { background-color: #121212; color: #ffffff; } 
  hr{background-color: #7289da;}
  .color{color:#7289da;}
  body {
    padding: 25px;
    background-color: #121212;
    color: #ffffff;
    transition-duration: 0.2s;
    font-family: Monospace;
  }
  hr{background-color: #7289da;}

  h1 {
    color: cyan;
  }

  h2 {
    color: cyan;
  }

  code {
    color: cyan;
  }
</style>

## Week 0 Documentation
Week 0 was the first week of our AP CSP Journey, we met multiple issues regarding the installation processes, GIT, VScode, and much more. We'll be documenting every issue we faced thoroughly throughout this document

## VSCode, GitHub Pages Setup




Installing WSL was our first step in our project, to explain what WSL is:

The Windows Subsystem for Linux (WSL) represents an innovative compatibility layer within the Windows operating system environment. It enables the seamless coexistence of Windows and Linux applications by providing a Linux-compatible kernel interface atop the Windows NT kernel. WSL effectively bridges the historically distinct realms of Windows and Linux, fostering an environment where users can harness the power of both ecosystems simultaneously.

<img src="https://cdn.discordapp.com/attachments/909947635715153952/1146673423330857010/Screenshot_2023-08-30_215546.png" alt="Alternative text" />
<em>An example of a Linux WSL terminal</em>

<hr>
After we installed our WSL, we downloaded VSCode, VSCode stands as a prominent exemplar in the realm of integrated development environments (IDEs) and source code editors.

<img src="https://cdn.discordapp.com/attachments/909947635715153952/1146675205553532989/image.png" alt="Alternative text" float="left" align="left" />

<em> What our Student Repository looks like on VSCode </em>
<hr>

After getting the Software setup, we cloned the Teacher Repository, named "Teacher", and a forked Repository named "Student"
<img src="https://cdn.discordapp.com/attachments/909947635715153952/1146678779813560340/image.png" alt="Alternative text" float="left" align="left" />
<br>
<em> Cloning into both Repositories </em>
<hr>

After we had our Repositories ready, I completed the Installation Process with Ruby, Jekyll, etc.

Our first problem arised when our "Make" command didn't work as intended, and would return the following Error Message:
<img src="https://cdn.discordapp.com/attachments/909947635715153952/1146679963014135808/image.png" alt="Alternative text" float="left" align="left" />

<br>

Researching the code a little, I came across a Stack Overflow page that had a similar problem to mine. Their code would would face a similar error code where the Makefile claims that a file doesn't exist. 

<img src="https://cdn.discordapp.com/attachments/909947635715153952/1146681792213028924/image.png" alt="Alternative text" float="left" align="left" />

Following the Discussion, we would be able to narrow down the problem to the Shellflags, which was the main breaking point of the Makefile. Therefore commenting out the Shellflags would fix this problem. After we did so, we would be able to run "Make" normally.

<img src="https://cdn.discordapp.com/attachments/909947635715153952/1146683203625685052/image.png" alt="Alternative text" float="left" align="left" />

<hr>

The next supposed step was to setup the VSCode push to Github feature. However, I decided to use CMD Git as I was more familiar with it than VSCode GUI. So first I set the Github Email and Username.

From here, I expected running the "git push" command would function as intended, but it instead gave me this error message:

<img src="https://cdn.discordapp.com/attachments/909947635715153952/1146684556477464656/image.png" alt="Alternative text" float="left" align="left" />

Having dealt with CyberSecurity concepts before, I was able to guess that I needed a Pubkey. Researching a little more into how to authenticate, I found out I had to set up a SSH key. 

Essentially I simply followed the steps given by Github [here](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)

Doing this, I ran into another problem, Github was still prompting me for my Github password, and not my SSH key password. The problem was actually fairly simple. 

When I ran the command:

<code>
git clone http://github.com/Be1uga4life/student.git
</code>

This was still trying to authenticate over HTTP, and what we wanted to do was authenticate through SSH, therefore the new command would be:

<code>
git clone git@github.com:Be1uga4life/student.git
</code>

After this, my installation process was finished
