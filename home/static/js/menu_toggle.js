// change navbar color 
$(document).ready(function(){
    $(window).scroll(function(){
        var scroll = $(window).scrollTop();
        if(scroll>150){
            $('.navbar').css('background', '#222');
            $('.navbar').css('box-shadow', 'rgba(0,0,0,0.1) 0px 4px 12px');
        }
        else{
            $('.navbar').css('background', 'transparent');
            $('.navbar').css('box-shadow', 'none');
        }

    })
})




const toggleBtn = document.querySelector('.toggle_btn')
const toggleBtnIcon = document.querySelector('.toggle_btn i')
const dropdownMenu = document.querySelector('.dropdown_menu')

toggleBtn.onclick = function(){
    dropdownMenu.classList.toggle('open');

    const isOpen = dropdownMenu.classList.contains('open');
    toggleBtnIcon.classList = isOpen
    ? 'fa fa-times'
    : 'fa fa-bars'
    
}