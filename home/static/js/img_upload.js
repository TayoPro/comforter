function showPreview(event){
    if(event.target.files.length > 0){
        var src = URL.createObjectURL(event.target.files[0]);
        var preview = document.getElementById("file-ip-1-preview");
        var flip_img = document.getElementById("flip_img");
        preview.src = src;
        preview.style.display = "block";
        preview.classList.add("flip");
        preview.style.maxHeight = "8rem";
        flip_img.style.maxHeight = "8rem";
    }
  }