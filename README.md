<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
<!-- [![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url] -->




<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/clstaudt/audiomariner">
    <img src="images/logo-big.png" alt="Logo" width="280" height="280">
  </a>

  <h3 align="center">audiomariner</h3>

  <p align="center">
    AI-powered navigation in spoken word audio content for humans and machines
    <!-- <br />
    <a href="https://github.com/clstaudt/audiomariner"><strong>Explore the docs »</strong></a>
    <br /> -->
    <br />
    <!-- <a href="https://github.com/clstaudt/audiomariner">View Demo</a>
    ·
    <a href="https://github.com/clstaudt/audiomariner/issues">Report Bug</a>
    · -->
    <a href="https://github.com/clstaudt/audiomariner/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project


Podcasts and other long-form audio formats are more popular than ever, but their content remains less accessible than to other media on the web: Established search engines work with titles and descriptions, but not the spoken word itself. You may remember an interesting segment from an episode or talk, but it's cumbersome to retrieve it again and refer others to it. 

Thanks to current progress in AI, navigating speech audio content could become much easier: Automatic transcription, speaker recognition and diarization, detection of structure and topics - examples of functions enabled by state of the art machine learning models.

The audiomariner project aims to provide an open source toolkit of machine learning solutions for transcribing and indexing spoken-word audio files. Going beyond transcription, it focuses on extracting rich metadata that maps the content and form of podcast episodes, interviews, talks, voice memos and similar content. This is the basis for advanced search features over audio content, which can power a variety of end user applications: Imagine an audio player with a search field for your queries. Imagine a chatbot that enables you to ask questions about a long talk. Imagine a true podcast search and recommendation engine that knows large volumes of episodes and point you to the most relevant segments, or suggest new content based on the topic that you are listening to.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

<!-- 
This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

* [![Next][Next.js]][Next-url]
* [![React][React.js]][React-url]
* [![Vue][Vue.js]][Vue-url]
* [![Angular][Angular.io]][Angular-url]
* [![Svelte][Svelte.dev]][Svelte-url]
* [![Laravel][Laravel.com]][Laravel-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]
* [![JQuery][JQuery.com]][JQuery-url]

<p align="right">(<a href="#top">back to top</a>)</p> -->



<!-- GETTING STARTED -->
<!-- ## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```

### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/your_username_/Project-Name.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
 ## Usage (Vision)

### Querying a spoken word audio file by keywords

```python
audio = Audio("../data/audio/ozymandias.mp3")
audio.process()
result_segments = audio.search(query="mighty", top=3)

top_segment = result_segments[0]

print(top_segment.transcript)
```

```
  And on the pedestal these words appear:
  "My name is Ozymandias, King of Kings:
  Look on my works, ye Mighty, and despair!"
```

### Extracting and identifying speakers


### Diarization

### Search over collection of spoken word audio files

<!--
Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#top">back to top</a>)</p>
 -->


<!-- ROADMAP -->
## Roadmap

- [ ] R&D: Evaluation and integration of transcription / speech-to-text models, with focus on local, open models => select best models, trading off transcript quality with cost and scalability
- [ ]  R&D: Evaluation and integration of AI methods for content analysis (segmentation by speakers, Q&A segments, chapters...) => rich metadata extraction
- [ ] R&D: Evaluation and integration of relevant search engine technology for indexing and accessing audio content => query engine over the content
- [ ] User Research & Requirements Discovery: connect with potential application developers and gather requirements 
- [ ] Development: Creation of an API exposing the verified functionality to application developers
- [ ] Demo Applications: Development and deployment of a demo application with search mask and audio player => showcase the audio navigation capabilities of the library

See the [open issues](https://github.com/clstaudt/audiomariner/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
<!-- ## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)

<p align="right">(<a href="#top">back to top</a>)</p>
 -->


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

<!-- Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)
* [React Icons](https://react-icons.github.io/react-icons/search) -->

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/clstaudt/audiomariner.svg?style=for-the-badge
[contributors-url]: https://github.com/clstaudt/audiomariner/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/clstaudt/audiomariner.svg?style=for-the-badge
[forks-url]: https://github.com/clstaudt/audiomariner/network/members
[stars-shield]: https://img.shields.io/github/stars/clstaudt/audiomariner.svg?style=for-the-badge
[stars-url]: https://github.com/clstaudt/audiomariner/stargazers
[issues-shield]: https://img.shields.io/github/issues/clstaudt/audiomariner.svg?style=for-the-badge
[issues-url]: https://github.com/clstaudt/audiomariner/issues
[license-shield]: https://img.shields.io/github/license/clstaudt/audiomariner.svg?style=for-the-badge
[license-url]: https://github.com/clstaudt/audiomariner/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 