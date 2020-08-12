'use strict';

(function($) {

  $(document).ready(function () {
    // Check for FileReader API (HTML5) support.
    if (!window.FileReader) {
      alert('This browser does not support the FileReader API.');
    }
  });


  var url = {
    "week1": "<url>",
    "week2": "<url>"
  };

  // Utils

  function getFileReader(imgId) {
    let reader = new FileReader();
    reader.onload = function(e) {
      $("#"+imgId).attr('src', e.target.result);
    };
    return reader;
  };
  var reader = getFileReader("upImage")

  function showImage(input) {
    if (input.files && input.files[0]) {
      $("#imgClass").text("");
      reader.readAsDataURL(input.files[0]);
    }
  }

  $("input#getFile").change(function(){
    showImage(this);
  });

  $("#classifyImage").click(function(){
    classifyWeek1()
  });

  function classifyWeek1() {

    var documentData = new FormData();

    // Post the file to url and get response
    documentData.append("body", $('input#getFile')[0].files[0]);
      $.ajax({
          url: url.week1,
          type: 'POST',
          data: documentData,
          async: false,
          cache: false,
          contentType: false,
          processData: false,
          success: function (response) {
              $("#imgClass").text(response.predicted)
          },
          error: function(e) {
            alert(e.responseText)
          }
      });

      return false;
  }
  // Display error messages.
  function onError(error) {
    alert(error.responseText);
  }

})(jQuery)
