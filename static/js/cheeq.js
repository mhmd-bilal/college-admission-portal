const text =
  "We are delighted to have you here as you embark on your journey towards advanced learning and academic excellence. Explore our offerings, discover your potential, and take the first step towards a rewarding future with CIT. We wish you the best of luck in your pursuit of higher education.";
let index = 0;

function typeWriter() {
  if (index < text.length) {
    document.getElementById("typing-text1").innerHTML += text.charAt(index);
    index++;
    setTimeout(typeWriter, 10);
  }
}
typeWriter();
function submitForm() {
  var form = document.getElementById("marks");
  var formData = new FormData(form);
  fetch("/", {
    method: "POST",
    body: formData,
  }).then(response => {
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    return response.json();
  });
}
function checkRange(input) {
  var total = document.getElementById((parseInt(input.id) + 1).toString());
  if (input.value < 1 || input.value > parseInt(total.value)) {
    input.value = "";
  }
}

function eligible(status) {
  var elg = document.getElementById("eligibility");
  var link = document.getElementById("myLink");
  var outer = document.getElementById("pdbutton");
  var eligib = document.getElementById("eligib");

  if (status == true) {
    elg.innerText = "You are eligible to apply";
    link.classList.remove("disabled-link");
    link.classList.add("active-link");
    outer.style.background = "black";
    eligib.value = "Yes";
  } else {
    var reason = "";
    fetch("/eligibility_api", {
      method: "POST",
      body: formData,
    })
      .then(response => {
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        return response.json();
      })
      .then(data => {
        reason = data.data;
      })
      .catch(error => {
        console.error("There was a problem with the fetch operation:", error);
      });
    elg.innerText = "You are not eligible to apply" + reason;
    link.classList.add("disabled-link");
    link.classList.remove("active-link");
    outer.style.background = "grey";
    eligib.value = "No";
  }
  submitForm();
}
function checkValues(event) {
  event.preventDefault();
  var numbers = [];
  for (var i = 0; i < 15; i = i + 3) {
    var num =
      parseInt(document.getElementById((i + 2).toString()).value) /
      parseInt(document.getElementById((i + 3).toString()).value);
    if (num < 0.5) {
      eligible(false);
      return;
    }
    numbers.push(num);
  }
  if (document.getElementById("10".toString()).value == "Computer Science") {
    numbers[2] = Math.max(numbers[2], numbers[3]);
  }
  for (var i = 0; i < 3; i++) {
    if (numbers[i] < 0.75) {
      eligible(false);
      return;
    }
  }
  eligible(true);
}

function toggleColor(stream) {
  var pills = document.querySelectorAll(".pill");
  var scienceCourses = document.getElementById("scienceCourses");
  var artsCourses = document.getElementById("artsCourses");

  if (stream === "Arts") {
    scienceCourses.style.display = "none";
    artsCourses.style.display = "block";
    pills[0].classList.add("white");
    pills[0].classList.remove("black");
    pills[1].classList.add("black");
    pills[1].classList.remove("white");
    var subjectOptions = [
      '<select id="1" name="first_subject" class="form-contrl" required><option value="" selected disabled>Select Subject</option> <option value="Mathematics">Mathematics</option><option value="Statistics">Statistics</option><option value="Business Mathematics">Business Mathematics</option><option value="Applied Mathematics">Applied Mathematics</option><option value="Business Mathematics and Statistics">Business Mathematics and Statistics</option></select>',
      '<select id="4" name="second_subject" class="form-contrl" required><option value="" selected disabled>Select Subject</option> <option value="Commerce">Commerce</option><option value="Economics">Economics</option><option value="Accountancy">Accountancy</option></select>',
      '<select id="7" name="third_subject" class="form-contrl" required><option value="" selected disabled>Select Subject</option> <option value="Commerce">Commerce</option><option value="Economics">Economics</option><option value="Accountancy">Accountancy</option></select>',
    ];
  } else {
    scienceCourses.style.display = "block";
    artsCourses.style.display = "none";
    pills[0].classList.add("black");
    pills[0].classList.remove("white");
    pills[1].classList.add("white");
    pills[1].classList.remove("black");
    var subjectOptions = [
      '<input id="1" name="first_subject" type="text" class="form-contrl" value="Maths" readonly />',
      '<input id="4" class="form-contrl" type="text" name="second_subject" value="Physics" readonly />',
      '<input id="7" class="form-contrl" type="text" name="third_subject" value="Chemistry" readonly />',
    ];
  }

  for (var i = 0; i < subjectOptions.length; i++) {
    var parentElement = document.getElementById((i + 13).toString());
    parentElement.innerHTML = subjectOptions[i];
  }
}
