Title: Week1 Mobilenet V2
date: 2020-07-25
Javascripts: main.js

In this week we deployed our model inference code to S3. The network is mobile net v2 trained on imagenet dataset.


  <section>
    <div class="row gtr-uniform">
      <div class="col-3 col-12-xsmall">
        <ul class="actions">
          <li><input id="getFile" type="file" accept="image/jpg"/></li>
        </ul>
        <ul class="actions">
          <li><input id="classifyImage1" type="button" value="Classify"/></li>
        </ul>
      </div>
      <div class="col-6 col-12-xsmall">
        <span class="image fit">
          <img id="upImage" src="#" alt="">
        </span>
        <h3 id="imgClass" style="text-align:center" ></h3>
      </div>
    </div>
  </section>
