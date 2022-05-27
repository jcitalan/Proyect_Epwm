//selecting all required elements
const dropArea = document.querySelector(".drag-area"),
  dragText = dropArea.querySelector("header"),
  button = dropArea.querySelector("button"),
  dragToUploadForm = document.querySelector("#dragToUploadForm"),
  input = dropArea.querySelector("#inputFile");
let files; //this is a global variable and we'll use it inside multiple functions

dragToUploadForm.addEventListener("submit", (e) => {
  e.preventDefault();
  console.log("Me ejecute")
  if (files) {
    e.submit();
  }
});

button.addEventListener("click", (e) => {
  input.click(); //if user click on the button then the input also clicked
});

input.addEventListener("change", function () {
  //getting user select file and [0] this means if user select multiple files then we'll select only the first one
  files = this.files[0];
  dropArea.classList.add("active");
  showFile(files); //calling function
});

//Si el usuario arrastra el archivo sobre el DropArea
dropArea.addEventListener("dragover", (event) => {
  event.preventDefault(); //evitar el comportamiento por defecto
  dropArea.classList.add("active");
  dragText.textContent = "Suelta para cargar tu archivo";
});

//If user leave dragged File from DropArea
dropArea.addEventListener("dragleave", () => {
  dropArea.classList.remove("active");
  dragText.textContent = "Arrastra para cargar tu archivo";
});

//If user drop File on DropArea
dropArea.addEventListener("drop", (event) => {
  event.preventDefault(); //preventing from default behaviour
  //getting user select file and [0] this means if user select multiple files then we'll select only the first one
  files = event.dataTransfer.files;
  showFile(files); //calling function
  dropArea.classList.remove("active");
});

function showFile(files) {
  [...files].forEach((file) => {
    let fileType = file.type; //getting selected file type
    console.log(fileType)
    let validExtensions = ["application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"]; //adding some valid image extensions in array
    if (validExtensions.includes(fileType)) {
      
      var data = new FormData();
      data.append('file',file,file.name);
      console.log("si")
      console.log(file.name)
      console.log(data)

      let url = "http://localhost:5000/recibe"
      fetch(url,{
        method:"POST",
        // body: {files:files[0]}, // wrong
        body: data,
      })
      .then(function(response){
        return response.json()
      })
      // .then(function(data){ // use different name to avoid confusion
      .then(function(res){
        console.log('success')
        console.log(res)
      })

    } else {
      // alert("Adjunta unicamente un archivo excel"); 
      Swal.fire('Solo se permite un archivo de excel')
      dragText.textContent = "Drag & Drop to Upload File";
    }
  });
}