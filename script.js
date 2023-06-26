// Example POST method implementation:
async function postData(url = "", data = {}) {
    const response = await fetch(url, {
      method: "POST", 
      headers: {
        "Content-Type": "application/json",
       
      },
      body: JSON.stringify(data), 
    });
    return response.json(); 
  }


sendbutton.addEventListener("click",async ()=>{
    // alert("Hey you clicked")
    questionInput = document.getElementById("questionInput").value;
    document.getElementById("questionInput").value = "";
    document.querySelector(".right2").style.display = "block";
    document.querySelector(".right-1").style.display = "none";

    question1.innerHTML = questionInput;
    question2.innerHTML = questionInput; // Whatever user enters as a question will get replaced by our default question made in frontend that is "what is your work?"

    // Get the answer and populate it
    let result = await postData("/api",{"question":questionInput})
    solution.innerHTML = result.answer
   


})