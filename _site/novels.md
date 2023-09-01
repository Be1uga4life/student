<style> 
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
  .dark-mode {
    background-color: white;
    color: black;
    transition-duration: 0.2s;
  }
  .bar-dark{background-color: black}
  
  .border-dark {
    border: 2px solid black;
  }
  .cells-dark {
    width: 100px;
      height: 100px;
      border: 1px solid black;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 24px;
      cursor: pointer;
  }
  .board {
      display: grid;
      grid-template-columns: repeat(3, 100px);
      grid-gap: 2px;
    }
    .cell {
      width: 100px;
      height: 100px;
      border: 1px solid #7289da;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 24px;
      cursor: pointer;
    }

    th {
        color: cyan;
    }
</style>

<table border='1'><tr><th>Title</th><th>Author</th><th>Rating</th><th>Emoji</th></tr><tr><td>To Kill a Mockingbird</td><td>Harper Lee</td><td>4.26</td><td>❤</td></tr><tr><td>1984</td><td>George Orwell</td><td>4.19</td><td>❤</td></tr><tr><td>The Lord of the Rings</td><td>J.R.R. Tolkien</td><td>4.52</td><td>❤</td></tr><tr><td>The Catcher in the Rye</td><td>J.D. Salinger</td><td>3.8</td><td>👍</td></tr><tr><td>The Great Gatsby</td><td>F. Scott Fitzgerald</td><td>3.93</td><td>👍</td></tr><tr><td>The Lion, the Witch and the Wardrobe (Chronicles of Narnia, #1)</td><td>C.S. Lewis</td><td>4.23</td><td>❤</td></tr><tr><td>Lord of the Flies</td><td>William Golding</td><td>3.69</td><td>👍</td></tr><tr><td>Animal Farm</td><td>George Orwell</td><td>3.98</td><td>👍</td></tr><tr><td>Catch-22</td><td>Joseph Heller</td><td>3.99</td><td>👍</td></tr><tr><td>The Grapes of Wrath</td><td>John Steinbeck</td><td>4.0</td><td>❤</td></tr><tr><td>Gone with the Wind</td><td>Margaret Mitchell</td><td>4.3</td><td>❤</td></tr><tr><td>Slaughterhouse-Five</td><td>Kurt Vonnegut Jr.</td><td>4.09</td><td>❤</td></tr><tr><td>One Flew Over the Cuckoo's Nest</td><td>Ken Kesey</td><td>4.2</td><td>❤</td></tr><tr><td>A Clockwork Orange</td><td>Anthony Burgess</td><td>4.0</td><td>❤</td></tr><tr><td>Lolita</td><td>Vladimir Nabokov</td><td>3.88</td><td>👍</td></tr><tr><td>Are You There God? It's Me, Margaret</td><td>Judy Blume</td><td>3.94</td><td>👍</td></tr><tr><td>Atonement</td><td>Ian McEwan</td><td>3.93</td><td>👍</td></tr><tr><td>Watchmen</td><td>Alan Moore</td><td>4.38</td><td>❤</td></tr><tr><td>Never Let Me Go</td><td>Kazuo Ishiguro</td><td>3.84</td><td>👍</td></tr><tr><td>Things Fall Apart (The African Trilogy, #1)</td><td>Chinua Achebe</td><td>3.73</td><td>👍</td></tr><tr><td>Invisible Man</td><td>Ralph Ellison</td><td>3.91</td><td>👍</td></tr><tr><td>Mrs. Dalloway</td><td>Virginia Woolf</td><td>3.79</td><td>👍</td></tr><tr><td>Beloved</td><td>Toni Morrison</td><td>3.94</td><td>👍</td></tr><tr><td>On the Road</td><td>Jack Kerouac</td><td>3.61</td><td>👍</td></tr><tr><td>The Sun Also Rises</td><td>Ernest Hemingway</td><td>3.8</td><td>👍</td></tr><tr><td>The Big Sleep (Philip Marlowe, #1)</td><td>Raymond Chandler</td><td>3.96</td><td>👍</td></tr><tr><td>Possession. A romance</td><td>A.S. Byatt</td><td>3.89</td><td>👍</td></tr><tr><td>A Passage to India</td><td>E.M. Forster</td><td>3.68</td><td>👍</td></tr><tr><td>I, Claudius (Claudius, #1)</td><td>Robert Graves</td><td>4.24</td><td>❤</td></tr><tr><td>Their Eyes Were Watching God</td><td>Zora Neale Hurston</td><td>3.98</td><td>👍</td></tr><tr><td>The Sound and the Fury</td><td>William Faulkner</td><td>3.86</td><td>👍</td></tr><tr><td>All the King's Men</td><td>Robert Penn Warren</td><td>4.09</td><td>❤</td></tr><tr><td>The Blind Assassin</td><td>Margaret Atwood</td><td>3.96</td><td>👍</td></tr><tr><td>Native Son</td><td>Richard Wright</td><td>4.02</td><td>❤</td></tr><tr><td>Ragtime</td><td>E.L. Doctorow</td><td>3.89</td><td>👍</td></tr><tr><td>Light in August</td><td>William Faulkner</td><td>3.94</td><td>👍</td></tr><tr><td>To the Lighthouse</td><td>Virginia Woolf</td><td>3.8</td><td>👍</td></tr><tr><td>The French Lieutenant's Woman</td><td>John Fowles</td><td>3.88</td><td>👍</td></tr><tr><td>The Spy Who Came In from the Cold (George Smiley, #3)</td><td>John le Carré</td><td>4.08</td><td>❤</td></tr><tr><td>The Heart Is a Lonely Hunter</td><td>Carson McCullers</td><td>3.99</td><td>👍</td></tr><tr><td>Blood Meridian, or, the Evening Redness in the West</td><td>Cormac McCarthy</td><td>4.16</td><td>❤</td></tr><tr><td>White Noise</td><td>Don DeLillo</td><td>3.86</td><td>👍</td></tr><tr><td>Naked Lunch</td><td>William S. Burroughs</td><td>3.46</td><td>👍</td></tr><tr><td>Infinite Jest</td><td>David Foster Wallace</td><td>4.26</td><td>❤</td></tr><tr><td>Brideshead Revisited</td><td>Evelyn Waugh</td><td>4.01</td><td>❤</td></tr><tr><td>Snow Crash</td><td>Neal Stephenson</td><td>4.02</td><td>❤</td></tr><tr><td>Revolutionary Road</td><td>Richard Yates</td><td>3.92</td><td>👍</td></tr><tr><td>Midnight's Children</td><td>Salman Rushdie</td><td>3.98</td><td>👍</td></tr><tr><td>The Prime of Miss Jean Brodie</td><td>Muriel Spark</td><td>3.71</td><td>👍</td></tr><tr><td>Death Comes for the Archbishop</td><td>Willa Cather</td><td>3.95</td><td>👍</td></tr><tr><td>The Bridge of San Luis Rey</td><td>Thornton Wilder</td><td>3.79</td><td>👍</td></tr><tr><td>American Pastoral</td><td>Philip Roth</td><td>3.94</td><td>👍</td></tr><tr><td>The Power and the Glory</td><td>Graham Greene</td><td>3.98</td><td>👍</td></tr><tr><td>The Crying of Lot 49</td><td>Thomas Pynchon</td><td>3.69</td><td>👍</td></tr><tr><td>Portnoy’s Complaint</td><td>Philip Roth</td><td>3.7</td><td>👍</td></tr><tr><td>Wide Sargasso Sea</td><td>Jean Rhys</td><td>3.59</td><td>👍</td></tr><tr><td>Neuromancer (Sprawl, #1)</td><td>William Gibson</td><td>3.9</td><td>👍</td></tr><tr><td>The Corrections</td><td>Jonathan Franzen</td><td>3.83</td><td>👍</td></tr><tr><td>Red Harvest (The Continental Op #1)</td><td>Dashiell Hammett</td><td>3.96</td><td>👍</td></tr><tr><td>Gravity's Rainbow</td><td>Thomas Pynchon</td><td>4.0</td><td>❤</td></tr><tr><td>Under the Volcano</td><td>Malcolm Lowry</td><td>3.77</td><td>👍</td></tr><tr><td>The Painted Bird</td><td>Jerzy Kosiński</td><td>3.91</td><td>👍</td></tr><tr><td>Go Tell It on the Mountain</td><td>James Baldwin</td><td>4.04</td><td>❤</td></tr><tr><td>A House for Mr Biswas</td><td>V.S. Naipaul</td><td>3.81</td><td>👍</td></tr><tr><td>Play It As It Lays</td><td>Joan Didion</td><td>3.91</td><td>👍</td></tr><tr><td>Lucky Jim</td><td>Kingsley Amis</td><td>3.75</td><td>👍</td></tr><tr><td>Ubik</td><td>Philip K. Dick</td><td>4.1</td><td>❤</td></tr><tr><td>Rabbit, Run (Rabbit Angstrom, #1)</td><td>John Updike</td><td>3.58</td><td>👍</td></tr><tr><td>White Teeth</td><td>Zadie Smith</td><td>3.79</td><td>👍</td></tr><tr><td>The Golden Notebook</td><td>Doris Lessing</td><td>3.76</td><td>👍</td></tr><tr><td>The Heart of the Matter</td><td>Graham Greene</td><td>3.97</td><td>👍</td></tr><tr><td>Pale Fire</td><td>Vladimir Nabokov</td><td>4.16</td><td>❤</td></tr><tr><td>The Moviegoer</td><td>Walker Percy</td><td>3.65</td><td>👍</td></tr><tr><td>The Confessions of Nat Turner</td><td>William Styron</td><td>3.96</td><td>👍</td></tr><tr><td>Tropic of Cancer (Tropic, #1)</td><td>Henry Miller</td><td>3.67</td><td>👍</td></tr><tr><td>Appointment in Samarra</td><td>John O'Hara</td><td>3.82</td><td> 👍</td></tr><tr><td>Money</td><td>Martin Amis</td><td>3.69</td><td>👍</td></tr><tr><td>Deliverance</td><td>James Dickey</td><td>3.89</td><td>👍</td></tr><tr><td>The Day of the Locust</td><td>Nathanael West</td><td>3.72</td><td>👍</td></tr><tr><td>Housekeeping</td><td>Marilynne Robinson</td><td>3.81</td><td>👍</td></tr><tr><td>The Man Who Loved Children</td><td>Christina Stead</td><td>3.57</td><td>👍</td></tr><tr><td>The Sot-Weed Factor</td><td>John Barth</td><td>4.1</td><td>❤</td></tr><tr><td>The Adventures of Augie March</td><td>Saul Bellow</td><td>3.84</td><td>👍</td></tr><tr><td>Herzog</td><td>Saul Bellow</td><td>3.76</td><td>👍</td></tr><tr><td>At Swim-Two-Birds</td><td>Flann O'Brien</td><td>3.86</td><td>👍</td></tr><tr><td>Call It Sleep</td><td>Henry Roth</td><td>3.81</td><td>👍</td></tr><tr><td>The Sheltering Sky</td><td>Paul Bowles</td><td>3.9</td><td>👍</td></tr><tr><td>A Handful of Dust</td><td>Evelyn Waugh</td><td>3.9</td><td>👍</td></tr><tr><td>The Sportswriter (Frank Bascombe, #1)</td><td>Richard Ford</td><td>3.7</td><td>👍</td></tr><tr><td>The Berlin Stories</td><td>Christopher Isherwood</td><td>4.04</td><td>❤</td></tr><tr><td>A Death in the Family</td><td>James Agee</td><td>3.89</td><td>👍</td></tr><tr><td>The Recognitions</td><td>William Gaddis</td><td>4.2</td><td>❤</td></tr><tr><td>Dog Soldiers: A National Book Award Winner</td><td>Robert  Stone</td><td>3.7</td><td>👍</td></tr><tr><td>The Assistant</td><td>Bernard Malamud</td><td>3.9</td><td>👍</td></tr><tr><td>Loving</td><td>Henry Green</td><td>3.53</td><td>👍</td></tr><tr><td>Under the Net</td><td>Iris Murdoch</td><td>3.77</td><td>👍</td></tr><tr><td>A Dance to the Music of Time: 1st Movement (A Dance to the Music of Time, #1-3)</td><td>Anthony Powell</td><td>3.94</td><td>👍</td></tr><tr><td>An American Tragedy</td><td>Theodore Dreiser</td><td>3.96</td><td>👍</td></tr><tr><td>Falconer</td><td>John Cheever</td><td>3.65</td><td>👍</td></tr><tr><td>The Death of the Heart</td><td>Elizabeth Bowen</td><td>3.66</td><td>👍</td></tr></table>
Traceback (most recent call last):