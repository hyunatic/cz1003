function getBotResponse() {
  console.log("fn fired")
  var rawText = $("#textInput").val();
  var userHtml = '<br/><p class="userText"><span>' + rawText + "</span></p>";
  $("#textInput").val("");
  $("#chatbox").append(userHtml);
  document.getElementById("userInput").scrollIntoView({ block: "start", behavior: "smooth" });
  $.get("/chatbot", { msg: rawText }).done(function (data) {
    var botHtml = '<br/><p class="botText"><span>' + data + "</span></p>";
    $("#chatbox").append(botHtml);
    document
      .getElementById("userInput")
      .scrollIntoView({ block: "start", behavior: "smooth" });
  });
}
$("#textInput").keypress(function (e) {
  if (e.which == 13) {
    e.preventDefault();
    getBotResponse();
  }
});