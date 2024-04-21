const subjects = {
  science: [
    "Physics",
    "Chemistry",
    "Biology",
    "Mathematics",
    "Computer Science",
    "Biotechnology",
    "Environmental Science",
    "Geology",
    "Astronomy",
    "Statistics",
    "Agriculture Science",
    "Electronics",
    "Psychology",
    "Home Science",
    "Geography",
    "Engineering Drawing",
    "Nutrition and Dietetics",
    "Forensic Science",
    "Industrial Chemistry",
    "Bioinformatics",
    "Anthropology",
    "Sociology",
    "Home Economics",
    "Applied Mathematics",
    "Biochemistry",
    "Microbiology",
    "Genetics",
    "Pharmacology",
    "Oceanography",
    "Physics with Astrophysics",
    "Food Technology",
    "Polymer Science",
    "Textile Technology",
    "Meteorology",
    "Immunology",
    "Nanotechnology",
    "Remote Sensing",
    "Virology",
    "Biophysics",
    "Applied Geology",
    "Animal Husbandry and Veterinary Science",
    "Horticulture",
    "Dairy Technology",
    "Fisheries Science",
    "Sericulture",
    "Aquaculture",
    "Forestry",
    "Entomology",
    "Plant Pathology",
    "Agronomy",
    "English",
    "Hindi",
    "Sanskrit",
    "Bengali",
    "Telugu",
    "Marathi",
    "Tamil",
    "Urdu",
    "Gujarati",
    "Kannada",
    "Odia",
    "Punjabi",
  ],
  commerce: [
    "Accountancy",
    "Business Studies",
    "Economics",
    "Entrepreneurship",
    "Mathematics (optional)",
    "Informatics Practices (optional)",
    "Statistics (optional)",
    "Finance",
    "Marketing",
    "Human Resource Management",
    "Financial Management",
    "Cost Accounting",
    "Company Law",
    "Auditing",
    "Taxation",
    "Banking and Insurance",
    "International Business",
    "Retail Management",
    "Supply Chain Management",
    "Financial Markets",
    "Business Communication",
    "Organizational Behavior",
    "Management Accounting",
    "Business Law",
    "Corporate Governance",
    "E-commerce",
    "Risk Management",
    "Investment Management",
    "Strategic Management",
    "Public Finance",
    "Microeconomics",
    "Macroeconomics",
    "English",
    "Hindi",
    "Sanskrit",
    "Bengali",
    "Telugu",
    "Marathi",
    "Tamil",
    "Urdu",
    "Gujarati",
    "Kannada",
    "Odia",
    "Punjabi",
  ],
};

function generateSubjectRow(labelNumber, subjectOptions, index) {
  return `<div class="form-row subject-row">
                    <div class="col-md-6 mb-3">
                        <label>Subject ${labelNumber}</label>
                        <select class="form-control subject-select"  name="_12th_subject${index}">
                            <option value="Select Subject" selected disabled>Select Subject</option>
                            ${subjectOptions}
                        </select>
                    </div>
                    <div class="col-md-3 mb-3">
                        <label>Marks Obtained</label>
                        <input type="number" class="form-control marks-obtained" placeholder="Marks" name="_12th_subject${
                          index + 1
                        }_marks_obtained">
                    </div>
                    <div class="col-md-3 mb-3">
                        <label>Maximum Marks</label>
                        <input type="number" class="form-control max-marks" placeholder="Maximum" name="_12th_subject${
                          index + 1
                        }_total_marks">
                    </div>
                </div>`;
}

function addSubjectRows(subjectType) {
  const subjectRowsContainer = $("#subjectRows");
  subjectRowsContainer.empty();
  const selectedSubjects = subjects[subjectType]; // This retrieves the selected subject type
  for (let i = 0; i < 5; i++) {
    const subjectOptions = selectedSubjects
      .map(subject => `<option value="${subject}">${subject}</option>`)
      .join("");
    const subjectRowHTML = generateSubjectRow(i + 1, subjectOptions, i + 1);
    subjectRowsContainer.append(subjectRowHTML);
  }
}

document.addEventListener("DOMContentLoaded", function () {
  addSubjectRows("science");
  const autosavedFormData =
    JSON.parse(localStorage.getItem("autosavedFormData")) || {};
  for (const key in autosavedFormData) {
    if (Object.hasOwnProperty.call(autosavedFormData, key)) {
      const value = autosavedFormData[key];
      const inputElement = document.querySelector(`[name="${key}"]`);
      if (inputElement) {
        inputElement.value = value;
      }
    }
  }
});

const inputElements = document.querySelectorAll("input, select, textarea");
inputElements.forEach(function (input) {
  input.addEventListener("input", function () {
    const formData = {};
    inputElements.forEach(function (input) {
      formData[input.name] = input.value;
    });
    localStorage.setItem("autosavedFormData", JSON.stringify(formData));
  });
});
