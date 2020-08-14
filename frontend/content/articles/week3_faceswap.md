Title: Week3 Face Swap
date: 2020-08-15
Javascripts: main.js

In this week we deployed our model inference code to S3. The network is mobile net v2 trained on custom drone dataset.


  <section>
    <div class="row gtr-uniform">
      <div class="col-3 col-12-xsmall">
        <ul class="actions">
          <li><input id="getFile" type="file" accept="image/jpg" name="files[]" multiple/></li>
        </ul>
        <ul class="actions">
          <li><input id="faceSwap" type="button" value="Face Swap"/></li>
        </ul>
      </div>
      <div class="col-6 col-12-xsmall">
        <span class="image fit">
          <img id="upImage" src="#" alt="">
        </span>
        <h3 id="imgClass" style="text-align:center" ></p>
      </div>
    </div>
    <div class="row gtr-uniform">
      <div class="col-4">
        <span class="image fit"><img id="file1" src="#" alt=""></span>
      </div>
      <div class="col-4">
        <span class="image fit"><img id="file2" src="#" alt=""></span>
      </div>
      <div class="col-4">
        <span class="image fit"><img src="images/pic03.jpg" alt=""></span>
      </div>
    </div>
  </section>
