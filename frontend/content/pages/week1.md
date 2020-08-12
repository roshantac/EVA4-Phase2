Title: Week1 Mobilenet V2
Javascripts: main.js

In this week we deployed our model inference code to S3. The network is mobile net v2 trained on imagenet dataset.


  <section>
    <div class="row gtr-uniform">
      <div class="col-6 col-12-xsmall">
        <ul class="actions">
          <li>
            <input class="row" id="getFile" type="file" accept="image/jpg"/>
          </li>
        </ul>
        <ul class="actions">
          <li>
            <input class="row" id="classifyImage" type="button" value="Classify"/>
          </li>
        </ul>
      </div>
      <div class="col-6 col-12-xsmall">
        <span class="image fit"><img id="upImage" src="#" alt=""></span>
        <span id="imgClass"></span>
      </div>
    </div>
  </section>
