<!-- #region -->
<style>
* {
  box-sizing: border-box;
}

.column {
  float: left;
  width: 33.33%;
  padding: 5px;
}

/* Clearfix (clear floats) */
.row::after {
  content: "";
  clear: both;
  display: table;
}
</style>



<div class="row">
  <div class="column">  
      <a href="https://champsproject.com/">
          <img src="demo/champsbook/content/images/logo/champs_logo.jpg" style="width:15%">
      </a>    
  </div>
  <div class="column">
    <a href="http://www.bristol.ac.uk/maths/">
        <img src="demo/champsbook/content/images/logo/uob-logo.png" style="width:10%">
    </a>
  </div>
</div>

<!-- #endregion -->

# CHAMPS Book-Sprint Planning Repo

Repo created to store example and test notebooks for book building using [`jupyter-book`](https://github.com/jupyter/jupyter-book) 
 


## TO-DO's


* Add a [logfile](https://github.com/github-changelog-generator/github-changelog-generator) (In progress)
* Find out how to render `R Markdown`-native hyperlinks for cross-reference tables and figures 
* Find out how to render `R Markdown`-native captions for tables and figures
* Make a script to automatically turn `R Markdown` citation syntax to [`jekyll-scholar`](https://github.com/inukshuk/jekyll-scholar) syntax
* Test `python` API to run anti-plagiarism tool in a scriptable way. Alternative, add notes for use of software via [Balckboard](https://www.ole.bris.ac.uk/). 
